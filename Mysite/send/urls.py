from django.urls import path
from .views import view,good,add_and_save,Msgdelete,UserReg,UserLog
from .models import messages
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('view/',view,name='view'),
    path('good',good,name='good'),
    path('send/',add_and_save,name='send'),
    path('<int:pk>/',Msgdelete.as_view(),name='dl'),
    path('create/',UserReg.as_view(),name='create'),
    path('login/',UserLog.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]
