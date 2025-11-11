from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Crea un usuario normal o administrador desde la terminal"

    def add_arguments(self, parser):
        parser.add_argument("username", type=str, help="Nombre de usuario")
        parser.add_argument("password", type=str, help="Contraseña del usuario")
        parser.add_argument("--admin", action="store_true", help="Crea un usuario administrador")

    def handle(self, *args, **kwargs):
        username = kwargs["username"]
        password = kwargs["password"]
        es_admin = kwargs["admin"]

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f"⚠️ El usuario '{username}' ya existe"))
            return

        if es_admin:
            User.objects.create_superuser(username=username, password=password, email=f"{username}@admin.com")
            self.stdout.write(self.style.SUCCESS(f"✅ Usuario administrador '{username}' creado correctamente"))
        else:
            User.objects.create_user(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f"✅ Usuario normal '{username}' creado correctamente"))
