from django.db import models

category =[
    ("Fulltime","Fulltime"),
    ("Parttime","Parttime"),
]

class Author(models.Model):
    id = models.CharField(primary_key=True, max_length=13)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=10, blank=True)
    joined_date = models.DateField()
    type_author = models.CharField(max_length=10, choices=category, default='Fulltime')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    def name_with_initial(self):
        return f'{self.firstname[0]}. {self.lastname}'

    def get_type(self):
        return f'Type: {self.type_author}'
    

class Video(models.Model):
    title = models.CharField(max_length=50)
    published_date = models.DateField(null=True)
    short_detail = models.CharField(max_length=300)
    demo = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} {self.id}'