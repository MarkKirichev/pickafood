from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account with {username} has now been created! You\'re now able to log in!')
            return redirect('http://127.0.0.1:8080/login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/index.html', {'form': form})

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
