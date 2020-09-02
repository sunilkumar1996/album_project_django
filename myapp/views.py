from django.shortcuts import render, HttpResponseRedirect
from .forms import UserSignUpForm, UserLoginForm, AlbumForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Album, Photo


class UserLoginView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = AuthenticationForm()
            return render(request, 'myapp/login.html', {'form': form})
        else:
            return HttpResponseRedirect('/home/')

    def post(self, request):
        if not request.user.is_authenticated:
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged In Successfully !!')
                    return HttpResponseRedirect('/home/')
        else:
            return HttpResponseRedirect('/home/')

class HomePageView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = AlbumForm()
            # username = request.user
            return render(request, 'myapp/home.html', {'form': form, 'username': request.user})
        else:
            return HttpResponseRedirect('/login/')

class UserLogOut(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/home/')

class UserSignUpView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            form = UserSignUpForm()
            return render(request, 'myapp/signup.html', {'form': form})
        else:
            return HttpResponseRedirect('/home/')

        def post(self, request):
            form = UserSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully !!')
                return HttpResponseRedirect('/login/')

class AlbumView(View):
    def get(self, request):
        if request.user.is_authenticated:
            album = Album.objects.filter(user=request.user)
            return render(request, "myapp/album.html", {'albums': album})
        else:
            return HttpResponseRedirect('/login/')

class PhotoView(View):
    def get(self, request):
        if request.user.is_authenticated:
            photo = Photo.objects.all()
            return render(request, "myapp/photo.html", {'photos': photo})
        else:
            return HttpResponseRedirect('/login/')