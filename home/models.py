from django.db import models

# Create your models here.
class userInfo(models.Model):
    firstName = models.CharField(max_length = 122)
    lastName = models.CharField(max_length = 122)
    email = models.EmailField(max_length = 122)
    loginPassword = models.CharField(max_length = 122)
    document = models.FileField(upload_to = None, null = True)

    def __str__(self):
        return self.email
