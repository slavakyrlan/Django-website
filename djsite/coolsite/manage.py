#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coolsite.settings')
    try:
        from django.core.management import execute_from_command_line
        # импорт execute_from_command_line из модуля django.core.management, который используется для выполнения командной строки Django.
    except ImportError as exc:
        #Если возникает ошибка ImportError, значит Django не может быть импортирован. В этом случае, генерируется соответствующее исключение, которое сообщает о проблеме с импортом Django.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv) # выполняет команду, указанную в аргументах командной строки.


if __name__ == '__main__':
    main()
