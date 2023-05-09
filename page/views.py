from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm,MeetingForm
from .models import Produck,Announcement

def index(request):
    context = {
        'produck':Produck.objects.all(),
        'announcement':Announcement.objects.all().order_by("-id")[:3],
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            email= form.cleaned_data['email']
            phone= form.cleaned_data['phone']
            subject= form.cleaned_data['subject']
            content= form.cleaned_data['content']
            html = render_to_string("contactform.html",{
                'name':name,
                'email':email,
                'phone':phone,
                'subject':subject,
                'content':content,
            })
            send_mail("Yeni Gönderi","başlık",settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER,],html_message=html)
            send_mail("Talebiniz Hk.",f"""Sayın {name.title()} 
            \nFirmamıza göstermiş olduğunuz ilgiden dolayı teşekkür ederiz.
                      \n Talebiniz alınmıştır en kısa sürede geri dönüş yapılacaktır.
                      \n Sağlıklı günler dileriz.
                      \n Hisar Grup Medikal
                     """,settings.EMAIL_HOST_USER,[email,],)
            return redirect("home")
    else:
        form = ContactForm()
    return render(request,'contact.html',{'form':form})

def produck(request):
    context = {
        'produck':Produck.objects.all().order_by("-id"),
    }
    return render(request,'produck.html',context)

def single_produck(request,id):
    context = {
    "item" : Produck.objects.get(id=id),
    "produck":Produck.objects.all().order_by("-id")[:4]
    }
    return render(request,'single_produck.html',context)

def meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name'].title()
            email= form.cleaned_data['email']
            phone= form.cleaned_data['phone']
            subject= "Randevu Talebi"
            date_time= str(form.cleaned_data['date']) +" , "+str(form.cleaned_data['time'])
            html = render_to_string("contactform.html",{
                'name':name,
                'email':email,
                'phone':phone,
                'subject':subject,
                'date_time':date_time,
            })
            send_mail("Randevu","başlık",settings.EMAIL_HOST_USER,[settings.EMAIL_HOST_USER,],html_message=html,)
            send_mail("Randevu Hk.",f"""Sayın {name} 
            \nFirmamıza göstermiş olduğunuz ilgiden dolayı teşekkür ederiz.
                      \n Randevu talebiniz alınmıştır.{date_time} tarihinde görüşmek dileğiyle sağlıklı günler dileriz.
                      \n Hisar Grup Medikal
                     """,settings.EMAIL_HOST_USER,[email,],)
            return redirect("home")
    else:
        form = MeetingForm()
    return render(request,'meeting.html',{'form':form})

def announcement(request):
    context = {
        'announcement':Announcement.objects.all().order_by("-id"),
    }
    return render(request,'announcement.html',context)

def single_announcement(request,id):
    context = {
    "item" : Announcement.objects.get(id=id),
    "announcement":Announcement.objects.all().order_by("-id")[:5]
    }
    return render(request,'single_announcement.html',context)
