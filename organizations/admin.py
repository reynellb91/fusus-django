from django.contrib import admin

from .models import Organization, User

# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
