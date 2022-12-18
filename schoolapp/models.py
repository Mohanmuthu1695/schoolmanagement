from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class customuser(AbstractUser):
    user_type_data=((1,'Hod'),(2,'staff'),(3,'student'))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=50)
    
    
class adminHod(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(customuser,on_delete=models.CASCADE)
   
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()
    
class course(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=50)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()

class staff(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(customuser,on_delete=models.CASCADE)
   
    address=models.CharField(max_length=50)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()


    
class subject(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=50)
    course_id=models.ForeignKey(course,on_delete=models.CASCADE)
    staff_id=models.ForeignKey(staff, on_delete=models.CASCADE)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()

   
    
class student(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(customuser,on_delete=models.CASCADE)
  
    gender=models.CharField( max_length=50)
    profile_pic=models.FileField()
    address=models.CharField(max_length=400)
    course_id=models.ForeignKey(course, on_delete=models.DO_NOTHING)
    session_start_year=models.DateField(auto_now=True)
    session_end_year=models.DateField(auto_now=True)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()


class attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(subject, on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()


class attendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(student, on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(attendance, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()

class leave_reportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    leave_date=models.DateField()
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()

class leave_reportStaff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    leave_date=models.DateField()
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()


class Feedback_staff(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()

class Feedback_student(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(student,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()
    
class Notification_staf(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField( auto_now_add=True)
    updated_at=models.DateTimeField( auto_now_add=True)
    object=models.Manager()

@receiver(post_save, sender=customuser)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        if instance.user_type==1:
            adminHod.object.create(admin=instance)
        if instance.user_type==2:
            staff.object.create(admin=instance)
        if instance.user_type==3:
            student.object.create(admin=instance)
@receiver(post_save, sender=customuser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staff.save()
    if instance.user_type==3:
        instance.student.save()
    
    
        
    
    

            
    


    
    
    