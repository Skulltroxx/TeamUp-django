from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib import messages
from .models import UserModel
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        p_form = UserProfileForm(request.POST)
        if p_form.is_valid():
            p_form.save()
            username = p_form.cleaned_data.get('username')
            lat = p_form.cleaned_data.get('lat')
            long = p_form.cleaned_data.get('long')
            messages.success(request, 'Account successfully created! You can now log in.')
            user = User.objects.get(username = username)
            UserModel.objects.create(user=user, lat=lat, long=long)

            return redirect('site-login')
        else:
            return render(request, 'users/register.html', {'p_form': p_form})
    else:
        p_form = UserProfileForm()
    return render(request, 'users/register.html', {'p_form': p_form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')
