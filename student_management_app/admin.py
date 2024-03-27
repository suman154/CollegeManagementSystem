from django.contrib import admin
from .models import SessionYearModel, CustomUser, AdminHOD, Staff, Course, Subject, Student, Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff, FeedBackStudent, FeedBackStaff, NotificationStudent, NotificationStaff, StudentResult

# Register your models here.
admin.site.register(SessionYearModel)
admin.site.register(CustomUser)
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
admin.site.register(StudentResult)
