import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from datacenter.models import Schoolkid, Mark, Lesson, Commendation
from fix_marks import fix_marks
from fix_chastisements import remove_chastisements
from commendations import create_commendation

print("Django загружен, можно использовать скрипты.")
