from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()



class CustomUser(AbstractUser):
    HOD = '1'
    STAFF = '2'
    STUDENT = '3'

    EMAIL_TO_USER_TYPE_MAP = {
        'hod': HOD,
        'staff' : STAFF, 
        'student': STUDENT
    }


    user_type_data = ((HOD, "HOD"), (STAFF, "Staff"), (STUDENT, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)



class AdminHOD(models.Model):
    id =  models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()





class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager



class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)

    # default course 
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    staff_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()



class Student(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    address = models.TextField()
    course_id = models.ForeignKey(Course, on_delete = models.DO_NOTHING, default=1)
    session_year_id = models.ForeignKey(SessionYearModel, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()



class Attendance(models.Model):
    # subject attendance
    id = models.AutoField(primary_key=True)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING) 
    attendance_date = models.DateField() 
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager() 



class AttendanceReport(models.Model): 
    # Individual Student Attendance 
    id = models.AutoField(primary_key=True) 
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING) 
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE) 
    status = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager() 


class LeaveReportStudent(models.Model): 
    id = models.AutoField(primary_key=True) 
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE) 
    leave_date = models.CharField(max_length=255) 
    leave_message = models.TextField() 
    leave_status = models.IntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager() 




class LeaveReportStaff(models.Model): 
    id = models.AutoField(primary_key=True) 
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE) 
    leave_date = models.CharField(max_length=255) 
    leave_message = models.TextField() 
    leave_status = models.IntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager() 



class FeedBackStudent(models.Model): 
    id = models.AutoField(primary_key=True) 
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE) 
    feedback = models.TextField() 
    feedback_reply = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager() 
  
  
class FeedBackStaff(models.Model): 
    id = models.AutoField(primary_key=True) 
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE) 
    feedback = models.TextField() 
    feedback_reply = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager() 
  



class NotificationStudent(models.Model): 
    id = models.AutoField(primary_key=True) 
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE) 
    message = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager() 


class NotificationStaff(models.Model): 
    id = models.AutoField(primary_key=True) 
    stafff_id = models.ForeignKey(Staff, on_delete=models.CASCADE) 
    message = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager() 
  


class StudentResult(models.Model): 
    id = models.AutoField(primary_key=True) 
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE) 
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1) 
    subject_exam_marks = models.FloatField(default=0) 
    subject_assignment_marks = models.FloatField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    objects = models.Manager()



receiver(post_save, sender=CustomUser) 
  
# Now Creating a Function which will 
# automatically insert data in HOD, Staff or Student 
def create_user_profile(sender, instance, created, **kwargs): 
    # if Created is true (Means Data Inserted) 
    if created: 
        
        # Check the user_type and insert the data in respective tables 
        if instance.user_type == 1: 
            AdminHOD.objects.create(admin=instance) 
        if instance.user_type == 2: 
            Staff.objects.create(admin=instance) 
        if instance.user_type == 3: 
            Student.objects.create(admin=instance, 
                                    course_id=Course.objects.get(id=1), 
                                    session_year_id=SessionYearModel.objects.get(id=1), 
                                    address="", 
                                    profile_pic="", 
                                    gender="") 
      
  
@receiver(post_save, sender=CustomUser) 
def save_user_profile(sender, instance, **kwargs): 
    if instance.user_type == 1: 
        instance.adminhod.save() 
    if instance.user_type == 2: 
        instance.staff.save() 
    if instance.user_type == 3: 
        instance.students.save()


