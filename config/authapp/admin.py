from django.contrib import admin
from django.db import models


# Register your models here.
from .models import User
from .forms import UserAdminCreationForm,UserAdminChangeForm

class UserAdmin(admin.ModelAdmin):
    search_fields = ["email"]
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    # class Meta:
    #     model = User


admin.site.register(User, UserAdmin)

