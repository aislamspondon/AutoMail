from django.db import models


# Create your models here.
class MailInfo(models.Model):
    _id = models.AutoField(primary_key=True)
    sender_mail = models.CharField(max_length=40)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject}"