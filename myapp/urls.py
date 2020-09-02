from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('logout/', views.UserLogOut.as_view(), name='logout'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('album/', views.AlbumView.as_view(), name='album'),
    path('photo/', views.PhotoView.as_view(), name='photo'),
]