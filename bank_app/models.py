from django.db import models

# Create your models here.


class Bank(models.Model):
    """Database model for the bank in the system"""
    name = models.CharField(max_length=49, blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    def __str__(self):
        """Returns string representation of bank"""
        return self.name

    class Meta:
        managed = False
        db_table = 'banks'


class Branche(models.Model):
    """Database model for bank branches in the system"""
    ifsc = models.CharField(primary_key=True, max_length=11)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, blank=True, null=True)
    branch = models.CharField(max_length=300, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=300, blank=True, null=True)
    district = models.CharField(max_length=300, blank=True, null=True)
    state = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        """Returns string representation of the branch"""
        return self.ifsc

    class Meta:
        managed = False
        db_table = 'branches'
