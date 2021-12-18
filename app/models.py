from django.db import models 
from multiselectfield import MultiSelectField
from django import forms

CHOICES_EMPRESA = (
        ('COMPANY XYZ', 'COMPANY XYZ'),
        ('COMPANY ABC', 'COMPANY ABC'),
    )

CHOICES=[('Y','YES'),('N','NO')]

TEST=(('Fever', 'Fever'),
        ('Cough', 'Cough'),
        ('Pain of Throat', 'Pain of Throat'),
        ('Difficulty breathing', 'Difficulty breathing'),
        ('Headache (Headache)', 'Headache (Headache)'),
        ('Coryza', 'Coryza'),
        ('I DONT HAVE SYMPTOMS', 'I DONT HAVE SYMPTOMS'),
)

class cadastro(models.Model):
    user_name = models.CharField(max_length=150)
    user_lastname = models.CharField(max_length=150)
    user_company = models.CharField(max_length=15, choices=CHOICES_EMPRESA, blank=False, null=False) 
    user_choices = models.CharField(max_length=15, choices=CHOICES) 
    user_text1=models.TextField(max_length=100,  blank=True )  
    #MultiSelectField
    user_test = MultiSelectField(choices=TEST) 