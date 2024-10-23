from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings


def homepage(request):
    return render(request, 'index/index.html', {})


def send_email(request):
    if request.method == 'POST':
        services = request.POST.get('services')
        name = request.POST.get('name')
        vehicle = request.POST.get('vehicle')
        email = request.POST.get('email')  # Get sender's email
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

        # Compose the email content
        subject = f"New Consultation Request from {name}"
        email_message = f"""
        Services Requested: {services}
        Name: {name}
        Vehicle: {vehicle}
        Email: {email}
        Date: {date}
        Time: {time}
        Message: {message}
        """

        # Send the email
        send_mail(
            subject,
            email_message,
            email,  # Sender's email (using this as the sender)
            ['marianopinca@gmail.com'],  # Recipient email
            fail_silently=False,
        )
        return redirect('homepage')  # Redirect to a success page after submission
    return render(request, 'consultation_form.html')
