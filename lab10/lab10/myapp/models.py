from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Student(Person):
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} (Student)'

class Teacher(Person):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} (Teacher)'