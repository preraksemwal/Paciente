from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from home.models import patient, doctor, organization
from django.core.mail import send_mail
import hashlib
import random
import os
import string

sign_up_info1 = []
req = None
logged_in = False

def upload_document(file, email):
    parent_dir = 'static/uploads/'
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
    context = {
        'variable_name' : 'value'
    }
    # both GET/POST
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

        if patient.objects.filter(email = request.POST.get('email')).count() != 0 or doctor.objects.filter(email = request.POST.get('email')).count() != 0:
            return HttpResponse("<h3>User Already Exists. Try Login.</h3>")

        if has_digits == False or has_lower == False or has_special == False or has_upper == False or is_long == False:
            return HttpResponse("<h3>Weak Password.</h3>")

        send_mail(
        'Paciente: Email Verification',
        otp,
        'paciente.inc@yahoo.com',
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

        if sign_up_info1[-1] != enteredOTP:
            return HttpResponse("<h3>Invalid OTP.</h3>")
        if sign_up_info1[0] != email:
            return HttpResponse("<h3>Please enter the same email address.</h3>")
        if user_type.lower() not in ['patient', 'doctor', 'organization']:
            return HttpResponse("<h3>Invalid User Type.</h3>")
        if user_type.lower() == "patient":
            upload_document(request.FILES['image1'], email)
            # upload_document(request.FILES['image2'], email)
            patient(firstName = firstname, lastName = lastname, email = email, loginPassword = sign_up_info1[1], uniqueID = unique_id, phoneNumber = phone_no, uploaded_image1 = image1, uploaded_image2 = image2).save()
        elif user_type.lower() == "doctor":
            upload_document(request.FILES['image1'], email)
            # upload_document(request.FILES['image2'], email)
            doctor(firstName = firstname, lastName = lastname, email = email, loginPassword = sign_up_info1[1], uniqueID = unique_id, phoneNumber = phone_no, uploaded_image1 = image1, uploaded_image2 = image2).save()
        else:
            pass

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
    if (patient.objects.filter(email = request.POST.get('email'), loginPassword = hashlib.sha256(request.POST.get('password').encode('utf-8')).hexdigest()).count() == 0) and (doctor.objects.filter(email = request.POST.get('email'), loginPassword = hashlib.sha256(request.POST.get('password').encode('utf-8')).hexdigest()).count() == 0):
        return HttpResponse("<h3>Invalid Credentials.</h3>")
    logged_in = True
    return render(request, 'home.html')

def doctorPage(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect('/')
    doctor_list = doctor.objects.all()
    return render(request, 'doctor.html', {'doctor_list': doctor_list})

def about(request):
    return render(request, 'about.html')

def services(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect('/')
    return HttpResponse("services.html")

def appointment(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect('/')
    doctor_list = doctor.objects.all()
    return render(request, 'appointment.html', {'doctor_list': doctor_list})