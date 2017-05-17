import os
from importlib import import_module

from django.conf import settings
from django.core.management.base import CommandError
from django.core.management.templates import TemplateCommand


class Command(TemplateCommand):
    help = (
        "Override [django] startapp "
        "default `target` is APPS_DIR/app_name"
    )
    missing_args_message = "You must provide an application name."

    def handle(self, *args, **options):
        app_name, target = options.pop('name'), options.pop('directory')
        self.validate_name(app_name, "app")

        try:
            import_module(app_name)
        except ImportError:
            pass
        else:
            raise CommandError(
                "%r conflicts with the name of an existing "
                "Python module and cannot be used as an app name. "
                "Please try another name." % app_name
            )

        if target is None:
            target = settings.APPS_DIR(app_name)

        if not os.path.exists(target):
            os.makedirs(target)

        super().handle('app', app_name, target, **options)
