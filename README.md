<img align="right" src="https://github.com/preraksemwal/Paciente/blob/main/paciente.png" width=400>

Paciente is a highly secure **Django**-based web application developed specifically for the **IIITD network**. It offers a seamless online experience for appointments, prescriptions, and transactions while prioritizing robust security measures against cyber adversaries.<br/><br/>

<h4> Cyber Threat Counter-Measures </h4> 

* **HTTPS** used for hosting the website (within IIITD's network at https://192.168.3.114) <br/>
* Secure against **_SQL Injection_** attacks <br/>
* Protected from **_XSS_** and **_CSRF_** attacks <br/>
* OTP verification required during Sign-Up and Transactions <br/>
* Server capable of restarting against **_DOS_** attacks using **_Slowloris_** <br/><br/>

<h2> Tech Stack </h2>

- Front-End Development: **_HTML, CSS, JavaScript_** <br/>
- Back-End Framework   : **_Django (Python)_** <br/>
- Database             : **_SQLite_** <br/>
- Server               : **_Nginx_** <br/>
- Payment Gateway      : **_RazorPay_** <br/><br/>


[YouTube Video Link](https://youtu.be/JNq6Itf5ro0) <br/>
[User Guide](https://drive.google.com/file/d/1Lc8HBtGRO4rg8CY4wmITUvYwkNMEJncB/view?usp=share_link) <br/>
[Demo Transaction Receipt recieved over Email](https://drive.google.com/file/d/1-XOXT0Pif_a26axTZCCtbZv1GAOD6s74/view?usp=share_link) <br/><br/>



![first](https://github.com/preraksemwal/Paciente/assets/77500750/4edb4364-4827-4af7-ab65-3fa5c6a2e6b4)
![second](https://github.com/preraksemwal/Paciente/assets/77500750/dd7afdb5-e675-4912-900d-4faf6c615eb6)
![third](https://github.com/preraksemwal/Paciente/assets/77500750/2e9a2d21-e7a5-4c6e-b44f-216f4828ee59)
![fourth](https://github.com/preraksemwal/Paciente/assets/77500750/48a9edd5-284d-4265-9c96-b55f5e38cfec)
![fifth](https://github.com/preraksemwal/Paciente/assets/77500750/50883a21-b5af-4e1f-b0ad-4b970d16b7c4)
![sixth](https://github.com/preraksemwal/Paciente/assets/77500750/80576a61-0f81-470a-81eb-74eca3f9f0f6)



**Useful Commands for Installing Libraries**: <br/>
```
sudo apt install python-django
pip install python-decouple
pip install django-admin-honeypot
```

**Other Commands useful while testing the Application**: <br/>
```
python manage.py runserver
python manage.py showmigrations
python manage.py makemigrations
python manage.py migrate
```
