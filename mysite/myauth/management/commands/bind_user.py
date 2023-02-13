from django.contrib.auth.models import User, Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(pk=21)
        group, created = Group.objects.get_or_create(name='profile_manager')
        permission_profiled = Permission.objects.get(codename='view_profiled')
        permission_logentry = Permission.objects.get(codename='view_logentry')

        # добавление разрешения в группу
        group.permissions.add(permission_profiled)

        # присоединение пользователя к группе
        user.groups.add(group)

        # связать пользователя напрямую с разрешением
        user.user_permissions.add(permission_logentry)

        group.save()
        user.save()
