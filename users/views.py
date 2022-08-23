from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registter a new user"""
    if request.method != 'POST':
        # Display a  regestraion form
        form = UserCreationForm()
    else:
        # Process Completed Form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
