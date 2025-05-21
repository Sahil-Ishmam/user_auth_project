
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def register_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')
    else:
        serializer = RegisterSerializer()
    return render(request, 'user_auth/register.html', {'serializer': serializer})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'user_auth/login.html')




def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def profile_view(request):
    return render(request, 'user_auth/profile.html', {'user': request.user})


def home_view(request):
    return render(request, 'user_auth/home.html')

