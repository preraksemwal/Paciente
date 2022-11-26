from django.db import models
import os

# Create your models here.
class userInfo(models.Model):
    firstName = models.CharField(max_length = 122)
    lastName = models.CharField(max_length = 122)
    email = models.EmailField(max_length = 122)
    loginPassword = models.CharField(max_length = 122)
    # document = models.FileField(upload_to = 'None', null = True)
    # document = models.FileField(upload_to = 'static/upload/' + str(email), null = True)

    parent_dir = 'static/uploads/'
    path = os.path.join(parent_dir, str(email))
    try: 
        os.mkdir(path)
    except OSError as error:
        pass
    finally:
        document = models.FileField(upload_to = path, null = True)

    def __str__(self):
        return self.email
