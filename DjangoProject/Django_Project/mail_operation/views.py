from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

def send_email(request):  

   res = send_mail("hello Jas", "How are you", "jesmensultana@gmail.com", ["jaslifezone@gmail.com", "rahmanasadur24@gmail.com"])
   return HttpResponse('%s'%res)
