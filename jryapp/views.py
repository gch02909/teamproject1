from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from jryapp.forms.ReservationForm import ReservationForm
from jryapp.models import *
import logging

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def detail(request, pk):
    pcroom = PCRoom.objects.get(pk=pk)
    seats = Seat.objects.all()
    return render(request, 'detail.html', {'pcroom':pcroom, 'seatsUp':seats[0:5], 'seatsDown':seats[5:10]})
    
def calendar(request):
    return render(request, 'calendar.html')

def reservation(request):
    return render(request, 'reservation.html')
    
def event(request):
    return render(request, 'event.html')

def event_details(request):
    return render(request, 'event_details.html')

def createReservation(request):
    if request.method == 'POST':
        reservationForm = ReservationForm(request.POST)
        if reservationForm.is_valid():
            reservation = reservationForm.save(commit=False)
            # logging.error(reservation.startDate)
            reservation.user = User.objects.get(username='rose')
            reservation.pcroom = PCRoom.objects.get(pk=request.POST['pcroom'])
            reservation.startDate = request.POST['startDay'] + ' ' +request.POST['startTime']
            reservation.endDate = request.POST['endDay'] + ' ' +request.POST['endTime']
            reservation.save()
    return redirect('/event_details')
        



