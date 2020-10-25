from django.contrib import admin
from .models import User,QR_code,Blog,Admin
# Register your models here.

admin.site.register(User)
admin.site.register(QR_code)
admin.site.register(Blog)
admin.site.register(Admin)