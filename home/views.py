from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from home.models import patient, healthcare_professional, organization, booked_appointment
from django.core.mail import send_mail
import hashlib
import random
import os
import string

sign_up_info1 = []
req = None
logged_in = False
payment_otp = None

def upload_document(file, email, secondary = False):
    parent_dir = 'static/uploads/'
    if secondary == True:
        email += '(1)'
        path = os.path.join(parent_dir, email)
    else:    
        path = os.path.join(parent_dir, email)
    try: 
        os.mkdir(path)
    except OSError as error:
        pass
    finally:
        with open(path + '/' + file.name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

# Create your views here.
def index(request):
    global logged_in
    context = {
        'variable_name' : 'value'
    }
    # both GET/POST
    logged_in = False
    return render(request, 'index.html', context)

def signup1(request):
    return render(request, 'signup1.html')

def signup2(request):
    global sign_up_info1
    if request.method == "POST":
        email = request.POST.get('loginUser')
        password = request.POST.get('loginPassword')
        rePassword = request.POST.get('rePassword')
        if password != rePassword:
            return HttpResponse("<h3>Passwords don't match.</h3>")
        
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        otp = str(random.randint(1000, 9999))
        sign_up_info1 = [email, hashed_password, otp]
        
        # check password strength
        has_lower, has_upper, has_special, has_digits, is_long = False, False, False, False, len(password) >= 8
        for ch in password:
            if ch.islower():
                has_lower = True
            if ch.isupper():
                has_upper = True
            if ch in string.digits:
                has_digits = True
            if ch in string.punctuation:
                has_special = True

        if has_digits == False or has_lower == False or has_special == False or has_upper == False or is_long == False:
            return HttpResponse("<h3>Weak Password.</h3>")

        if patient.objects.filter(email = request.POST.get('loginUser')).count() != 0 or healthcare_professional.objects.filter(email = request.POST.get('loginUser')).count() != 0:
            return HttpResponse("<h3>User Already Exists. Try Login.</h3>")


        send_mail(
        'Paciente: Email Verification',
        "Your One Time Password (OTP): " + otp,
        'paciente.inc@gmail.com',
        [email],
        fail_silently = False,
        )
    return render(request, 'signup2.html')

def login(request):
    global sign_up_info1
    if request.method == "POST":
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        enteredOTP = request.POST.get('otp')
        user_type = request.POST.get('userType')
        unique_id = request.POST.get('uniqueID')
        phone_no = request.POST.get('phoneNumber')
        image1 = request.POST.get('image1')
        image2 = request.POST.get('image2')
        print(image1)
        print(image2)
        if sign_up_info1[-1] != enteredOTP:
            return HttpResponse("<h3>Invalid OTP.</h3>")
        if sign_up_info1[0] != email:
            return HttpResponse("<h3>Please enter the same email address.</h3>")
        if user_type.lower() not in ['patient', 'doctor', 'organization']:
            return HttpResponse("<h3>Invalid User Type.</h3>")
        if user_type.lower() == "patient":
            try:
                upload_document(request.FILES['image1'], email)
                upload_document(request.FILES['image2'], email, True)
            except:
                pass
            patient(firstName = firstname, lastName = lastname, email = email, loginPassword = sign_up_info1[1], uniqueID = unique_id, phoneNumber = phone_no, uploaded_image1 = image1, uploaded_image2 = image2).save()
        elif user_type.lower() == "doctor":
            try:
                upload_document(request.FILES['image1'], email)
                upload_document(request.FILES['image2'], email, True)
            except:
                pass
            healthcare_professional(firstName = firstname, lastName = lastname, email = email, loginPassword = sign_up_info1[1], uniqueID = unique_id, phoneNumber = phone_no, uploaded_image1 = image1, uploaded_image2 = image2).save()
        else:
            try:
                upload_document(request.FILES['image1'], email)
                upload_document(request.FILES['image2'], email, True)
            except:
                return HttpResponseRedirect('/')
            organization(firstName = firstname, lastName = lastname, email = email, loginPassword = sign_up_info1[1], uniqueID = unique_id, phoneNumber = phone_no, uploaded_image1 = image1, uploaded_image2 = image2).save()

        '''
        # request.POST
        <QueryDict: {
            'csrfmiddlewaretoken': ['Z5o4HJUpIxV0IochtG1c2dLbKH7k8KkxZCX6vVSfWkR1RIzC7RUfWt0KE0LErYuT'],
            'firstName': ['1'], 
            'lastName': ['a'], 
            'email': ['prerak20105@iiitd.ac.in'], 
            'otp': ['8361'], 
            'document': ['hello - Copy (3).txt']}> 
        <class 'django.http.request.QueryDict'>

         # print(document, type(document)) # is a str
        '''
        sign_up_info1 = None
    return HttpResponseRedirect('/')

# def redirectToHome(request):
#     global req
#     req = request
#     print("hi")
#     return HttpResponseRedirect('/home/')

def home(request):
    global req
    global logged_in
    if request.method == 'GET':
        if logged_in:
            return render(request, 'home.html')         
        return HttpResponseRedirect('/')
    if req != None:
        request = req
        req = None
    if (patient.objects.filter(email = request.POST.get('email'), loginPassword = hashlib.sha256(request.POST.get('password').encode('utf-8')).hexdigest()).count() == 0) and (healthcare_professional.objects.filter(email = request.POST.get('email'), loginPassword = hashlib.sha256(request.POST.get('password').encode('utf-8')).hexdigest()).count() == 0):
        return HttpResponse("<h3>Invalid Credentials.</h3>")
    logged_in = True
    return render(request, 'home.html')

def doctor(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect('/')
    doctor_list = healthcare_professional.objects.all()
    return render(request, 'doctor.html', {'doctor_list': doctor_list})

def about(request):
    return render(request, 'about.html')

def services(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect('/')
    return render(request, 'services.html')

def pharmacyPage(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect('/')
    pharmacy_list = organization.objects.all()
    return render(request, 'pharmacy.html', {'pharmacy_list': pharmacy_list})

def prescriptionPage(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect('/')
    pharmacy_list = organization.objects.all()
    return render(request, 'prescription.html', {'pharmacy_list': pharmacy_list})

def payment(request):
    global logged_in
    global payment_otp
    if logged_in == False:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        patient_name = request.POST.get('name')
        patient_email = request.POST.get('email')
        print(request.POST)
        pharmacy_email = organization.objects.all()[int(request.POST.get('dropdown')) - 3]
        payment_otp = str(random.randint(1000, 9999))
        send_mail(
        'Paciente: Email Verification',
        "Your One Time Password (OTP) for Payment Gateway: " + payment_otp,
        'paciente.inc@gmail.com',
        [patient_email],
        fail_silently = False,
        )
        print(patient_name, patient_email, pharmacy_email)
    return render(request, 'payment.html')

def razorpay(request):
    global payment_otp
    if request.method == 'GET':
        if logged_in:
            return render(request, 'home.html')         
        return HttpResponseRedirect('/')
    enteredPaymentOTP = request.POST.get('otp')
    if payment_otp == enteredPaymentOTP:
        payment_otp = None
        return render(request, 'pop.html')
    payment_otp = None
    return render(request, 'home.html')

def hospitalPage(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect('/')
    return render(request, 'hospital.html')

def appointment(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect('/')
    if request.method == "POST":
        search_word = request.POST['data']
        print(search_word)
    doctor_list = healthcare_professional.objects.all()
    return render(request, 'appointment.html', {'doctor_list': doctor_list})

def booking_complete(request):
    if request.method == 'POST':
        patient_name = request.POST.get('name')
        patient_email = request.POST.get('email')
        doctor_email = healthcare_professional.objects.all()[int(request.POST.get('dropdown')) - 5]
        description = request.POST.get('subject')
        date = request.POST.get('date')
        time = request.POST.get('time')

        booked_appointment(patient_name=patient_name, patient_email=patient_email, doctor_email=doctor_email, description=description, date=date, time=time).save()

    return HttpResponseRedirect('/home/')

def settings(request):
    return render(request, 'settings.html')