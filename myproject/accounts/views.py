from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import User
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']
            user.save()
            messages.success(request, "Signup successful! Please login.")
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                request.session['username'] = user.username
                return redirect('home')
            except User.DoesNotExist:
                messages.error(request, "Invalid credentials. Try again.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def home_view(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    return render(request, 'accounts/home.html', {'username': username})

def logout_view(request):
    request.session.flush()
    return redirect('login')
