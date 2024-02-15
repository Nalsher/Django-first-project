from django.urls import path
from .views import view,add_and_save,Msgdelete,UserCreation,UserLog
from .models import messages
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('',view,name='view'),
    path('send/',add_and_save,name='send'),
    path('<int:pk>/',Msgdelete.as_view(),name='dl'),
    path('create/',UserCreation,name='create'),
    path('login/',UserLog.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]
