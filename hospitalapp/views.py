from django.shortcuts import render,redirect, get_object_or_404
from hospitalapp.models import *
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'index.html')


def starter(request):
    return render(request, 'starter-page.html')    


def about(request):
    return render(request, 'about.html')  

def services(request):
    return render(request, 'services.html') 
 

def departments(request):
    return render(request, 'departments.html')  


def doctors(request):
    return render(request, 'doctors.html')  



def contact(request):
    return render(request, 'contact.html')  




def appointment(request):

    if request.method == 'POST':
        all = MyAppointment(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            datetime = request.POST['date'],
            department = request.POST['department'],
            doctor = request.POST['doctor'],
            message = request.POST['message'],

        )  
        all.save()
        messages.success(request, 'Appointment booked successfully!')

        return render(request,'appointment.html')

    else: 
         return render(request,'appointment.html')       
             
            
def show(request):
    allappointments = MyAppointment.objects.all()  
    return render(request, 'show.html', {'allappointments': allappointments})          



def delete(request, id):
    myappoint = MyAppointment.objects.get(id=id)
    myappoint.delete()
    messages.success(request, 'Appointment deleted successfully!')
    return redirect('/show')



def edit(request, id):
    editappointment = get_object_or_404(MyAppointment, id=id)  

    if request.method == 'POST':
        editappointment.name = request.POST.get('name')
        editappointment.email = request.POST.get('email')
        editappointment.phone = request.POST.get('phone')
        editappointment.datetime= request.POST.get('date')
        editappointment.department = request.POST.get('department')
        editappointment.doctor = request.POST.get('doctor')
        editappointment.message = request.POST.get('message')
        editappointment.save()
        messages.success(request, 'Appointment updated successfully!')
        return redirect('/show')

    return render(request, 'edit.html', {'editappointment': editappointment})    
