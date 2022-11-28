from django.db import models
import os

# Create your models here.
class patient(models.Model):
    firstName = models.CharField(max_length = 122)
    lastName = models.CharField(max_length = 122)
    email = models.EmailField(max_length = 122, unique=True)
    loginPassword = models.CharField(max_length = 122)
    uniqueID = models.CharField(max_length=122, unique=True)
    phoneNumber = models.CharField(max_length=122, unique=True)
    # document = models.FileField(upload_to = 'None', null = True)
    # document = models.FileField(upload_to = 'static/upload/' + str(email), null = True)

    parent_dir = 'static/uploads/'
    path = os.path.join(parent_dir, str(email))
    try: 
        os.mkdir(path)
    except OSError as error:
        pass
    finally:
        # document = models.FileField(upload_to = path, null = True)
        uploaded_image1 = models.FileField(upload_to = path, null = True)
        uploaded_image2 = models.FileField(upload_to = path, null = True)

    def __str__(self):
        return self.email

class healthcare_professional(models.Model):
    firstName = models.CharField(max_length = 122)
    lastName = models.CharField(max_length = 122)
    email = models.EmailField(max_length = 122, unique=True)
    loginPassword = models.CharField(max_length = 122)
    uniqueID = models.CharField(max_length=122, unique=True)
    phoneNumber = models.CharField(max_length=122, unique=True)

    parent_dir = 'static/uploads/'
    path = os.path.join(parent_dir, str(email))
    try: 
        os.mkdir(path)
    except OSError as error:
        pass
    finally:
        # document = models.FileField(upload_to = path, null = True)
        uploaded_image1 = models.FileField(upload_to = path, null = True)
        uploaded_image2 = models.FileField(upload_to = path, null = True)

    def __str__(self):
        return self.email

class organization(models.Model):
    firstName = models.CharField(max_length = 122)
    lastName = models.CharField(max_length = 122)
    email = models.EmailField(max_length = 122, unique=True)
    loginPassword = models.CharField(max_length = 122)
    uniqueID = models.CharField(max_length=122, default=None, unique=True)
    phoneNumber = models.CharField(max_length=122, default=None, unique=True)

    parent_dir = 'static/uploads/'
    path = os.path.join(parent_dir, str(email))
    try: 
        os.mkdir(path)
    except OSError as error:
        pass
    finally:
        # document = models.FileField(upload_to = path, null = True)
        uploaded_image1 = models.FileField(upload_to = path, null = True)
        uploaded_image2 = models.FileField(upload_to = path, null = True)

    def __str__(self):
        return self.email

class booked_appointment(models.Model):
    patient_name = models.CharField(max_length=122)
    patient_email = models.EmailField(max_length=122)
    doctor_email = models.EmailField(max_length=122)
    description = models.CharField(max_length=122)
    date = models.DateField(max_length=122)
    time = models.TimeField(max_length=122)