from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.messages.api import get_messages

# Where the user is redirected after successful authentication
@login_required
def complete(request): 
    return render(request, 'auth/complete.html', {})

# Since the logged in user is a normal Django user instance, we logout the user the natural Django way:
def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')
    
def error(request):
    """Error view"""
    messages = get_messages(request)
    return render(request, 'auth/error.html', {'messages': messages})

@login_required
def account_profile(request):
    return render(request, 'profile/account_profile.html', {})