#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from crud_ops import *
# os.remove('db.sqlite3')


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookr.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    # call your functions here ########
    # crud_ops()
    # many_to_one_example()
    # many_to_many_example()
    # get_examples()
    # filter_example()
    # order_by_example()
    # query_many_to_many()
    # update_example()
    # delete_example()


if __name__ == '__main__':
    main()
