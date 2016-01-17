#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kanvas.settings")

    from django.core.management import execute_from_command_line

    import logging
    from sorl.thumbnail.log import ThumbnailLogHandler
    logging.basicConfig(filename='django.log',level=logging.DEBUG)
    handler = ThumbnailLogHandler()
    handler.setLevel(logging.ERROR)
    logging.getLogger('sorl.thumbnail').addHandler(handler)

    execute_from_command_line(sys.argv)
