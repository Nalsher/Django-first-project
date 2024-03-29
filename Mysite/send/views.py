from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import messages,imagesend
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.generic.edit import DeleteView
from .forms import Userreg,Msgform
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView,LogoutView
from django import forms
from django.forms.widgets import *
#Create your project here
def view(request):
    images = imagesend.objects.all()
    mesage = messages.objects.all()
    paginator = Paginator(mesage,4)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'page':page,'mesage':page.object_list}
    return render(request,'send/view.html',context)


def sample_view(request):
    currentuser = request.user
    return currentuser.id

def add_and_save(request):

    if request.method == 'POST':
        msgform = Msgform(request.POST)
        if msgform.is_valid():
            msg = msgform.save(commit=False)
            messages.objects.create(text=msg.text,written_by = request.user)
            return HttpResponseRedirect(reverse('view'))
        else:
            context = {'form':msgform}
            return render(request,'send/send.html',context)
    else:
        msgform = Msgform()
        context = {'form':msgform}
        return render(request,'send/send.html',context)

# class Msgview(CreateView):
#     template_name = 'send/send.html'
#     form_class = Msgform
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['usr'] = User.objects.get(pk=sample_view)
#     def get_success_url(self):
#         return reverse('view')

class Msgdelete(DeleteView):
    template_name = 'send/Delete.html'
    context_object_name = 'msg'
    model = messages
    def get_success_url(self):
        return reverse('view')

# class UserReg(CreateView):
#     template_name = 'send/reg.html'
#     form_class = Userreg
#     success_url = reverse_lazy('view')

def UserCreation(request):
    if request.method == 'POST':
        userreg = Userreg(request.POST)
        if userreg.is_valid():
            userreg.save()
            return HttpResponseRedirect(reverse('view'))
        else:
            context = {'form':userreg}
            return render(request,'send/reg.html',context)
    else:
        userreg = Userreg()
        context = {'form':userreg}
        return render(request,'send/reg.html',context)
class UserLog(LoginView):
    template_name = 'send/log.html'
    redirect_authenticated_user = False


class Logout(LogoutView):
    template_name = 'send/good.html'