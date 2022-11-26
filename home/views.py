from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from home.models import userInfo
from django.core.mail import send_mail
import hashlib
import random
import os

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
        send_mail(
        'Paciente: Email Verification',
        otp,
        'paciente.inc@yahoo.com',
        [email],
        fail_silently = False,
        )

        sign_up_info1 = [email, hashed_password, otp]
    return render(request, 'signup2.html')

def login(request):
    global sign_up_info1
    if request.method == "POST":
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        enteredOTP = request.POST.get('otp')
        document = request.POST.get('document')
        if sign_up_info1[-1] != enteredOTP:
            return HttpResponse("<h3>Invalid OTP.</h3>")
        if sign_up_info1[0] != email:
            return HttpResponse("<h3>Please enter the same email address.")

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
        
        upload_document(request.FILES['document'], email)

        userInfo(firstName = firstname, lastName = lastname, email = email, loginPassword = sign_up_info1[1], document = document).save()
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
    if userInfo.objects.filter(email = request.POST.get('email'), loginPassword = hashlib.sha256(request.POST.get('password').encode('utf-8')).hexdigest()).count() == 0:
        return HttpResponse("<h3>Invalid Credentials.</h3>")
    logged_in = True
    return render(request, 'home.html')

def doctor(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect('/')
    return render(request, 'doctor.html')

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
    return render(request, 'appointment.html')