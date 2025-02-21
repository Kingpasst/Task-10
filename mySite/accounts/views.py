from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    """
    Render the home page.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template for the home page.
    """
    return render(request, 'home.html')


def register(request):
    """
    Handle user registration.

    If the user is already authenticated, redirect to the home page.
    If the request is a POST, process the registration form.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template for the registration page.
    """
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error in registration. Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """
    Handle user login.

    If the user is already authenticated, redirect to the home page.
    If the request is a POST, process the login form.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template for the login page.
    """
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """
    Log out the user and redirect to the home page.

    Args:
        request: The HTTP request object.

    Returns:
        Redirect to the home page after logging out.
    """
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def profile(request):
    """
    Render the user's profile page.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template for the user's profile page.
    """
    return render(request, 'accounts/profile.html')
