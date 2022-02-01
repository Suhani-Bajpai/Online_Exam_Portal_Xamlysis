from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class role_id(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name= models.CharField(max_length=100)


class course_id(models.Model):
    course_id = models.CharField(primary_key=True , max_length=100)
    course_name= models.TextField(max_length=100)

class sign_up(models.Model):
    role_id=models.ForeignKey("role_id" , on_delete=models.CASCADE)
    id=models.CharField( max_length=50)
    name=models.TextField()
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email_id=models.EmailField(primary_key=True , blank=False)
    mobile_no=models.IntegerField()
    institute_name=models.TextField()

class class_stu_tech(models.Model):
    role_id=models.ForeignKey("role_id" , on_delete=models.CASCADE)
    email_id=models.ForeignKey("sign_up" , on_delete=models.CASCADE)
    class_stu_tech=models.IntegerField()
    serial_no=models.AutoField(primary_key=True)


class courses_availed(models.Model):
    course_id=models.ForeignKey("course_id" , on_delete=models.CASCADE)
    role_id=models.ForeignKey("role_id" , on_delete=models.CASCADE)
    email_id=models.ForeignKey("sign_up" , on_delete=models.CASCADE)
    serial_no=models.AutoField(primary_key=True)

class exam_details(models.Model):
    exam_code=models.CharField(max_length=50 , primary_key=True)
    exam_title=models.TextField()
    date=models.DateField()
    start_time=models.TimeField()
    duration=models.DurationField()
    no_of_ques=models.IntegerField()
    max_marks=models.IntegerField()
    course_id=models.ForeignKey("course_id" , on_delete=models.CASCADE)
    email_id=models.ForeignKey("sign_up" , on_delete=models.CASCADE)





