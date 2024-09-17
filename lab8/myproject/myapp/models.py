from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_citizenid(value):
    if value[0] == '0':
        raise ValidationError('รหัสประชาชนต้องไม่เริ่มต้นด้วยเลข 0')
    if len(value) != 13:
        raise ValidationError('รหัสประชาชนต้องมีความยาว 13 หลัก')

def validate_names_different(value1, value2):
    if value1 == value2:
        raise ValidationError('ชื่อและนามสกุลต้องไม่เหมือนกัน')

def validate_expire_date(value):
    if value < timezone.now().date():
        raise ValidationError('วันหมดอายุต้องไม่อยู่ก่อนวันปัจจุบัน')

class UserProfile(models.Model):
    citizenid = models.CharField(max_length=13, validators=[validate_citizenid])
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    expire_date = models.DateField(validators=[validate_expire_date])
    BLOOD_TYPES = [
        ('A', 'A'),
        ('B', 'B'),
        ('AB', 'AB'),
        ('O', 'O'),
    ]
    blood_type = models.CharField(max_length=2, choices=BLOOD_TYPES)

    
    def clean(self):
        validate_names_different(self.firstname, self.lastname)