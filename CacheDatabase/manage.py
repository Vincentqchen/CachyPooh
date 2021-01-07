#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#Scheduler
from apscheduler.schedulers.background import BackgroundScheduler

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CacheDatabase.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    #Schedule daily database updates
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(train_model, 'interval', hours=3)
    # scheduler.start()



if __name__ == '__main__':
    main()
