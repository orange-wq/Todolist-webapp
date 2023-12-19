from django.shortcuts import render, redirect
from .models import Date, Entry
from .forms import DateForm, EntryForm, ImageUploadForm
from django.db.models import Case, When, Value, IntegerField
from django.contrib.auth.decorators import login_required
from django.http import Http404


def check_date_owner(date, request):
    if date.owner != request.user:
        raise Http404


def sort_dates(dates, sort_key=False):
    date_list = []
    for date in dates:
        entries = Entry.objects.filter(date=date)
        if sort_key:
            if entries.exists() and all(entry.is_done for entry in entries):
                date_list.append(date)
        else:
            if not entries.exists() or any(not entry.is_done for entry in entries):
                date_list.append(date)

    return date_list


def index(request):
    return render(request, 'todoapp/index.html')


@login_required
def dates(request):
    dates = Date.objects.filter(owner=request.user).order_by('-date_added')
    uncompleted_dates = sort_dates(dates)
    context = {'dates': uncompleted_dates}
    return render(request, 'todoapp/dates.html', context)


@login_required
def completed_dates(request):
    dates = Date.objects.filter(owner=request.user).order_by('date_added')
    completed_dates = sort_dates(dates, sort_key=True)
    context = {'dates': completed_dates}
    return render(request, 'todoapp/completed_dates.html', context)


@login_required
def date(request, date_id):
    date = Date.objects.get(id=date_id)
    check_date_owner(date, request)
    entries = date.entry_set.order_by(
        Case(
            When(priority='High', then=Value(1)),
            When(priority='Medium', then=Value(2)),
            When(priority='Low', then=Value(3)),
            default=Value(2),
            output_field=IntegerField()
        )
    )

    context = {'date': date, 'entries': entries}
    return render(request, 'todoapp/date.html', context)


@login_required
def new_date(request):
    errors = False
    if request.method != 'POST':
        form = DateForm()
    else:
        form = DateForm(data=request.POST)
        if form.is_valid():
            date_title = form.cleaned_data['title']
            existing_date = Date.objects.filter(title=date_title, owner=request.user)
            if existing_date:
                errors = True
            else:
                new_topic = form.save(commit=False)
                new_topic.owner = request.user
                new_topic.save()
                return redirect('todoapp:dates')

    context = {'form': form, 'errors': errors}
    return render(request, 'todoapp/new_date.html', context)


@login_required
def new_entry(request, date_id):
    date = Date.objects.get(id=date_id)
    check_date_owner(date, request)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.date = date
            new_form.save()
            return redirect('todoapp:date', date_id=date_id)

    context = {'date': date, 'form': form}
    return render(request, 'todoapp/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    date = entry.date
    check_date_owner(date, request)
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todoapp:date', date_id=date.id)

    context = {'entry': entry, 'date': date, 'form': form}
    return render(request, 'todoapp/edit_entry.html', context)


@login_required
def update_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    date = entry.date
    check_date_owner(date, request)
    if request.method == 'POST':
        is_done = request.POST.get('is_done') == 'True'
        entry.is_done = is_done
        entry.save()

    return redirect('todoapp:date', date_id=date.id)


@login_required
def upload_image(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    if entry.image:
        context = {'entry': entry, 'image': entry.image}
        return render(request, 'todoapp/display_entry_image.html', context)
    else:
        date = entry.date
        check_date_owner(date, request)
        form = ImageUploadForm(instance=entry)
        if request.method == 'POST':
            form = ImageUploadForm(request.POST, request.FILES, instance=entry)
            if form.is_valid():
                if 'image' in request.FILES:
                    form.save()
                    entry.is_done = True
                    entry.save()
                    return redirect('todoapp:date', date_id=date.id)
                else:
                    form.add_error(None, 'Please select an image to upload')

        context = {'form': form}
        return render(request, 'todoapp/upload_image.html', context)


def delete_image(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    date = entry.date
    check_date_owner(date, request)
    if request.method == 'POST':
        entry.image.delete()
        entry.is_done = False
        entry.save()

    return redirect('todoapp:date', date_id=date.id)


@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    date = entry.date
    check_date_owner(date, request)
    if request.method == 'POST':
        entry.delete()

    return redirect('todoapp:date', date_id=date.id)


@login_required
def delete_date(request, date_id):
    date = Date.objects.get(id=date_id)
    check_date_owner(date, request)
    if request.method == 'POST':
        date.delete()

    return redirect('todoapp:dates')

