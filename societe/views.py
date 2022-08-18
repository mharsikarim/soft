from django.contrib import messages

from account.models import User
from projet import settings
from .models import Services, Category
from django.core.paginator import Paginator


from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse




# Create your views here.
def index(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'societe/index.html', context)


def collectionsviews(request, name):
    if (Category.objects.filter(name=name, status=0)):
        service = Services.objects.filter(category__name=name)
        category_name = Category.objects.filter(name=name).first()
        context = {'service': service, 'category_name': category_name}
        return render(request, 'societe/service/index.html', context)
    else:
        messages.warning(request, 'cette category est introuvable pour le moment')
        return redirect('index')


def serviceviews(request, cat_name, ser_title):
    if (Category.objects.filter(name=cat_name, status=0)):
        if (Services.objects.filter(title=ser_title)):
            service = Services.objects.filter(title=ser_title).first()
            context = {'service': service}
        else:
            messages.error(request, "cette service est non introuvable")
            return redirect('collectionsviews')
    else:
        messages.error(request, "cette category est non introuvable")
        return redirect('index')
    return render(request, 'societe/service/view.html', context)









# Create your views here.
def home(request):
    return render(request, 'chat/home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'chat/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']


    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    html = render_to_string('contact/contactform.html', {
        'user':request.user,
        'room_id': room_id,
        'username': username,
        'message': message,

    })


    send_mail(room_id, message, settings.EMAIL_HOST_USER, [username], fail_silently=False,
               html_message=html)

    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details)
    return JsonResponse({"messages":list(messages.values())})













