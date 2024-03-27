from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, AdminHOD, Staff, Course, Subject, Student, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaff, NotificationStudent, NotificationStaff


# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel) 

admin.site.register(AdminHOD) 
admin.site.register(Staff) 
admin.site.register(Course) 
admin.site.register(Subject) 
admin.site.register(Student) 
admin.site.register(Attendance) 
admin.site.register(AttendanceReport) 
admin.site.register(LeaveReportStudent) 
admin.site.register(LeaveReportStaff) 
admin.site.register(FeedBackStudent) 
admin.site.register(FeedBackStaff) 
admin.site.register(NotificationStudent) 
admin.site.register(NotificationStaff)
