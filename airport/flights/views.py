from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Passenger, Flight, Security, Staff
import datetime
import pdfkit
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def login_security(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.user_type == 2:
                    login(request, user)
                    return redirect('security_clearing') #, pk=user.security.id)
                else:
                    return render(request, 'security_login.html', {'error_message': 'Invalid security staff credentials'})
            else:
                return render(request, 'security_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'security_login.html', {'error_message': 'Invalid login'})
    return render(request, 'security_login.html')


def login_staff(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if user.user_type == 1:
                    login(request, user)
                    return redirect('staff_generating_report', pk=user.staff.id)
                else:
                    return render(request, 'staff_login.html', {'error_message': 'Invalid flight staff credentials'})
            else:
                return render(request, 'staff_login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'staff_login.html', {'error_message': 'Invalid login'})
    return render(request, 'staff_login.html')


def home(request):
    return render(request, 'home.html')


def airport_mgmt(request):
    return render(request, 'airport_mgmt.html')


def clear_security(request):
    data = Passenger.objects.all()
    return render(request, 'security_clearing.html', {'passengers': data})


def clear_for_security(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    passenger.cleared_security_status = request.user.security.id
    passenger.save()

    return redirect('security_clearing')


def generate_report_staff(request,pk):
    staffperson = get_object_or_404(Staff, pk=pk)
    data = Passenger.objects.filter(flight_no=staffperson.flight_no)
    return render(request, 'staff_generating_report.html', {'passengers': data})

    
def view_flights(request):
    data = Flight.objects.all()
    return render(request, 'view_flights.html', {'flights': data})


def self_check_in(request,pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    passenger.checked_in_status = True
    passenger.save()

    return redirect('passenger_home', pnr=passenger.pnr)


def search_by_source(request):
    if request.method == "POST":
        source = request.POST['source']
        if source:
            data = Flight.objects.filter(source=source)
            return render(request, 'view_flights.html', {'flights': data})
        else:
            return redirect('view_flights')       
    else:
        return redirect('view_flights')


def search_by_destination(request):
    if request.method == "POST":
        destination = request.POST['destination']
        if destination:
            data = Flight.objects.filter(destination=destination)
            return render(request, 'view_flights.html', {'flights': data})
        else:
            return redirect('view_flights')
    else:
        return redirect('view_flights')


def view_available_flights(request):
    if request.method == "POST":
        source = request.POST['source']
        destination = request.POST['destination']
        if source and destination:
            flights = Flight.objects.filter(source=source, destination=destination)
            if flights:
                return render(request, 'home.html', {'flights': flights})
            else:
                return render(request, 'home.html', {'error_message': "No flights found"})
        else:
            return redirect('home')
    else:
        return redirect('home')


def book_flight(request, pk):
    if request.method == "POST":
        flight = Flight.objects.get(flight_no=pk)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        nationality = request.POST['nationality']
        gender = request.POST['gender']
        dob = request.POST['dob']
        pnr = str(flight.flight_no) + str(flight.destination)
        passenger = Passenger(pnr=pnr, first_name=first_name, last_name=last_name, nationality=nationality,
                              flight_no=flight, gender=gender, dob=dob)
        passenger.save()
        passenger.pnr = str(flight.flight_no) + str(flight.destination_code) + str(passenger.pk)
        passenger.save()
        flight.no_of_seats -= 1
        return redirect('passenger_home', pnr=passenger.pk)
    else:
        return render(request, 'book_flight.html', {'flight_no': pk})


def passenger_home(request, pnr):
    if request.method == "POST":
        pnr=request.POST['pnr']
        passenger = get_object_or_404(Passenger, pnr=pnr)
        return render(request, 'passenger_home.html', {'passenger': passenger})
    else:    
        passenger = get_object_or_404(Passenger, pk=pnr)
        return render(request, 'passenger_home.html', {'passenger': passenger})

def create_pdf(request,pnr):
    passenger = get_object_or_404(Passenger, pnr=pnr)
    html = loader.render_to_string('passenger_home.html', {'passenger': passenger})
    output= pdfkit.from_string(html, output_path=False)
    response = HttpResponse(content_type="application/pdf")
    response.write(output)
    return response