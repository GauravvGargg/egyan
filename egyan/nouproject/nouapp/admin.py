from django.contrib import admin
from . models import Enquiry
from . models import StudentInfo
from . models import LoginInfo

# Register your models here.
admin.site.register(Enquiry)
admin.site.register(StudentInfo)
admin.site.register(LoginInfo)