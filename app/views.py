from django.shortcuts import render 
# Create your views here.
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import *
import random
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.urls import reverse

class Template(TemplateView):
    template_name='dummy.html'

def User_form(request):
    pf=Profile_form()
    uf=User_Form()
    d={'uf':uf,'pf':pf}

    global otp,USO
    if request.method=='POST' and request.FILES:
        UD=User_Form(request.POST)
        PD=Profile_form(request.POST,request.FILES)
        if UD.is_valid() and PD.is_valid():
            pw=UD.cleaned_data['password']
            USO=UD.save(commit=False)
            USO.set_password(pw)
            USO.save()
            
            PD.save(commit=False)
            PD.user=USO
            PD.save()
            otp=''
            for i in range(6):
                x=random.randrange(0,9)
                otp+=str(x)

            send_mail("OTP for register your account",otp,'rsu191912@gmail.com',[USO.email],fail_silently=False)

            return HttpResponseRedirect(reverse('otp'))    
               
    return render(request,'home.html',d)


def otp(request):
    if request.method=='POST':
        VOTP=request.POST['otp']
        if VOTP==otp:
            return HttpResponseRedirect(reverse('Template'))
    return render(request,'otp.html')
