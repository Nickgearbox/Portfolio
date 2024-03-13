from django.shortcuts import render
from . models import Email
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage

def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        query=Email(name=name,email=email,message=message)
        query.save()
        
        #Email sends
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        #this is the email for the admin
        email_message=mail.EmailMessage(f'Email from {name}',f'{email}\n\n\n {message}',from_email,['nicolesonmuhalia@gmail.com'],connection=connection)
        connection.send_messages([email_message])
        connection.close()
        email_client=mail.EmailMessage(f'Nicoleson Response','Thanks for reaching us\n\nnicoleson.tech\n0758820022\nnicolesonmuhalia@gmail.com',from_email,[email],connection=connection)
        connection.send_messages([email_message,email_client])
        connection.close()
    return render(request,'index.html')
