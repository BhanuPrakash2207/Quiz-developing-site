from django.db import models
class Ques(models.Model):
    ques=models.CharField(max_length=250,null=True)
    op1=models.CharField(max_length=250,null=True)
    op2=models.CharField(max_length=250,null=True)
    op3=models.CharField(max_length=250,null=True)
    op4=models.CharField(max_length=250,null=True)
    ans=models.CharField(max_length=250,null=True)
    start_time=models.DateTimeField(null=True)
    end_time=models.DateTimeField(null=True)

    def __str__(self):
        return self.ques
# Create your models here.
