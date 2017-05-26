import subprocess

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = (
        "Run 'webpack' from django"
    )

    def handle(self, *args, **kwargs):
        cmd = (
            "NODE_ENV={0} yarn run webpack "
            "-- --config config/webpack/{0}.coffee"
            ).format(settings.DJANGO_ENV)

        try:
            res = subprocess.run(cmd, shell=True)
            res.check_returncode()
        except Exception as e:
            print()
            raise e
