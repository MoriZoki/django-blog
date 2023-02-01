from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# baraye ezafe kardane fild haye shakhsie user abstract dar akhare safheye etelate karbaran admin django 
# UserAdmin.fieldsets += (('فیلد های شخصی من', {'fields': ('is_author', 'special_user')}),
# )

# baraye neveshtane field haye skahsi user dar jaygahe delkhah az admin.py khode django elham gerefte shbode 

UserAdmin.fieldsets[2][1]['fields'] = ('is_active',
'is_staff',
'is_superuser',
'is_author',
'special_user',
'groups',
'user_permissions',)
UserAdmin.list_display += ('is_author', 'is_special_user')

admin.site.register(User, UserAdmin)