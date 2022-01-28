#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def mkdir(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def create_env_dir():
    from django.conf import settings
    mkdir(path=os.path.join(settings.BASE_DIR, settings.APP_NAME, settings.STATIC_URL[1:], settings.IMAGE_DIR))
    

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    create_env_dir()
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
