from django.contrib import admin
from .models import GroupMember, Group

class GroupMemberInline(admin.TabularInline):
    model = GroupMember

admin.site.register(Group)
# admin.site.register(GroupMember)