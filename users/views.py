from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from todoapp.models import Entry


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = False
            new_user.save()
            UserProfile.objects.create(user=new_user)
            send_verification_email(request, new_user)
            return redirect('users:registration_check_email')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def send_verification_email(request, user):
    current_site = get_current_site(request)
    mail_subject = 'Activate your account'
    message = render_to_string('registration/confirm_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()


def register_confirm_view(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('users:registration_success')
    else:
        return redirect('users:registration_error')


def registration_success(request):
    return render(request, 'registration/registration_success.html')


def registration_check_email(request):
    return render(request, 'registration/registration_check_email.html')


def registration_error(request):
    return render(request, 'registration/registration_error.html')


@login_required
def profile(request):
    user_profile = request.user.userprofile
    user = request.user
    completed_tasks = Entry.objects.filter(date__owner=user, is_done=True).count()
    total_tasks = Entry.objects.filter(date__owner=user).count()
    if user_profile.profile_image:
        photo_url = user_profile.profile_image.url
    else:
        photo_url = None
    context = {
        'photo_url': photo_url,
        'user': user,
        'completed_tasks': completed_tasks,
        'total_tasks': total_tasks,
    }
    return render(request, 'user_profile/profile.html', context)



@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('users:profile')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'user_profile/profile_update.html', {'profile_form': profile_form})


