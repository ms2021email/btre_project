from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Contact
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

# NOTE: when settings file has "USE_TZ=True", then need to use timezone code instead
# change datetime.datetime.now() to timezone.now()
#from datetime import datetime
from django.utils import timezone


"""
# Send email
#send_mail(
#    'Subject here',
#    'Here is the message.',
#    'from@example.com',
#    ['to@example.com'],
#    fail_silently=False,
#)
#EMAIL_HOST_USER,
#    send_mail(
#      'Property Listing Inquiry',
#      'There has been an inquiry for ' + listing + '. Sign into the admin panel for #more info.',
#      'ms2021email@gmail.com',
#      [realtor_email, 'ms2021email@gmail.com'],
#      fail_silently=False
#    )
#    text_content = f"date:{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}, listing_id:
# {listing_id}"
#    subject, from_email, to = text_content, 'ms2021email@gmail.com', #'ms2021email@gmail.com'
#    #text_content = 'This is an important message.'
#    html_content = '<p>This is an <strong>important</strong> message.</p>'
#    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#    msg.attach_alternative(html_content, "text/html")
#    msg.send()
#    print("Hello contact sent")
  
#    print(f"date:{datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}, listing_id:
# {listing_id}")

"""

# Create your views here.
def contact(request):
  if request.method == 'POST':
    print("Hello contact POST")
    listing_id = request.POST['listing_id']
    listing = request.POST['listing']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    realtor_email = request.POST['realtor_email']

    subject = f"Property Listing Inquiry, listing_id:{listing_id}, date:{timezone.now().strftime('%m/%d/%Y, %H:%M:%S')}"
    print(subject)
    
    if request.user.is_authenticated:
      user_id = request.user.id
      had_contacted = Contact.objects.all().filter(listing_id=listing_id,       user_id=user_id)

      if had_contacted:
        messages.error(
            request, 'You have already made an inquiry for this listing')
        return redirect('/listings/'+listing_id)

      print('logged-in user sent inquiry')
      contact = Contact(listing=listing, listing_id=listing_id, name=name,
                        email=email, phone=phone, message=message, user_id=user_id)
      contact.save()

      messages.success(
          request, 'Your request has been submitted, a realtor will get back to you soon')

      send_mail(
          subject,
          'There has been an inquiry for ' + listing + '. From user ' + name +
          '. With email ' + email + '. With user id ' + str(user_id) + '. Sign into the admin panel for more info.',
          'ms2021email@gmail.com',
          ['ms2021email@gmail.com', realtor_email],
          fail_silently=False
      )
    else:
      print('Non logged-in user sent inquiry')
      contact = Contact(listing=listing, listing_id=listing_id, name=name,
                        email=email, phone=phone, message=message, user_id=user_id)
      contact.save()

      messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')

      send_mail(
          subject,
          'There has been an inquiry for ' + listing + '. From user ' + name +
          '. With email ' + email + '. Sign into the admin panel for more info.',
          'ms2021email@gmail.com',
          ['ms2021email@gmail.com', realtor_email],
          fail_silently=False
      )

    return redirect('/listings/'+listing_id)
  
