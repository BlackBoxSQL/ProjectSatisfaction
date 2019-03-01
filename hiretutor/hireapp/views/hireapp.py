from django.shortcuts import redirect, render
from django.contrib import messages


def index(request):
    if request.user.is_authenticated:
        if request.user.is_tutor:
            return redirect('tutor:tutor_homepage')
        else:
            return redirect('guardian:guardian_homepage')
    return render(request, 'hireapp/home.html')
