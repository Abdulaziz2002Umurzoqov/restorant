from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=150, blank=False)
    lastName = models.CharField(max_length=150, blank=False)
    phone = models.CharField(max_length=100)
    mail = models.EmailField(blank=True, null=True)
    order_number = models.IntegerField(blank=True, default=1)


    def __str__(self):
        return f"{self.lastName} {self.firstName}"

    class Meta:
        db_table = 'Users'





