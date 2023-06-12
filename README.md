<img align="right" src="https://github.com/preraksemwal/Paciente/blob/main/paciente.png" width=400>

Paciente is a highly secure **Django**-based web application developed specifically for the **IIITD network**. It offers a seamless online experience for appointments, prescriptions, and transactions while prioritizing robust security measures against cyber adversaries.<br/><br/>

<h3> Tech Stack </h3>

- Front-End Development: **_HTML, CSS, JavaScript_** <br/>
- Back-End Framework   : **_Django (Python)_** <br/>
- Database             : **_SQLite_** <br/>
- Server               : **_Nginx_** <br/>
- Payment Gateway      : **_RazorPay_** <br/><br/>

<h4> Security Counter-Measures Offered </h4> 

* **HTTPS** used for hosting the website (within IIITD's network at https://192.168.3.114) <br/>
* Secure against **_SQL Injection_** attacks <br/>
* Protected from **_XSS_** and **_CSRF_** attacks <br/>
* OTP verification required during Sign-Up and Transactions <br/>
* Server capable of restarting against **_DOS_** attacks using **_Slowloris_** <br/>


[YouTube Video Link](https://youtu.be/JNq6Itf5ro0) <br/>
[User Guide](https://drive.google.com/file/d/1Lc8HBtGRO4rg8CY4wmITUvYwkNMEJncB/view?usp=share_link) <br/>
[Demo Transaction Receipt recieved over Email](https://drive.google.com/file/d/1-XOXT0Pif_a26axTZCCtbZv1GAOD6s74/view?usp=share_link) <br/><br/>

**Useful Commands for Installing Libraries**: <br/>
```
_sudo apt install python-django_ <br/>
_pip install python-decouple_ <br/>
_pip install django-admin-honeypot_ <br/><br/>
```

**Other Commands useful while testing the Application**: <br/>
```
_python manage.py runserver_ <br/>
_python manage.py showmigrations_ <br/>
_python manage.py makemigrations_ <br/>
_python manage.py migrate_ <br/>
```
