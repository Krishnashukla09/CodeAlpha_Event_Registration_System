from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})



def register(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    success = False
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Registration.objects.create(event=event, name=name, email=email)
        success = True
    return render(request, 'register.html', {'event': event, 'success': success})
