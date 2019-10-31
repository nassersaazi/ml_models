from django.db import models

# Create your models here.
class approvals(models.Model):
    GENDER_CHOICES = (
        ('Male','Male')
        ('Female','Female')
    )

    MARRIED_CHOICES = (
        ('Yes','Yes')
        ('No','No')
    )

    GRADUATED_CHOICES = (
        ('Graduate','Graduate')
        ('Not_Graduate','Not_Graduate')
    )

    SELFEMLOYED_CHOICES = (
        ('Yes','Yes')
        ('No','No')
    )

    PROPERTY_CHOICES = (
        ('Rural','Rural')
        ('Semiurban','Semiurban')
        ('Urban','Urban')
    )


    firstname=models.CharField(max_length=15)
    lastname=models.CharField(max_length=15)
    dependants=models.IntegerField()
    applicantincome=models.IntegerField()
    coapplicant=models.IntegerField()
    loanamt=models.IntegerField()
    loanterm=models.IntegerField()
    credithistory=models.IntegerField()
    gender=models.CharField(max_length=15)
    married=models.CharField(max_length=15)
    graduatededucation=models.CharField(max_length=15)
    selfemployed=models.CharField(max_length=15)
    area=models.CharField(max_length=15)

    def __str__(self):
        return self.firstname,self.lastname
