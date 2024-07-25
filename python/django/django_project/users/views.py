from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.urls import reverse


"""
message.debug
message.info
message.success
message.warning
message.error
"""

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account with usename : {username} has been created ! \n You are now able to login")
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})




def custom_logout_view(request):
    logout(request)
    # Redirect to a success page or home page
    return redirect(reverse('login'))  # or use 'login' if you want to redirect to the login page

@login_required
def profile(request):
    return render(request, 'users/profile.html')


