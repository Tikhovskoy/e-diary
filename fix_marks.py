from datacenter.models import Mark
from commendations import get_schoolkid, StudentNotFoundError, MultipleStudentsError, LessonNotFoundError
from django.db.utils import DatabaseError

def fix_marks(schoolkid_name):
    try:
        schoolkid = get_schoolkid(schoolkid_name)
        bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        updated_count = bad_marks.update(points=5)

        if updated_count:
            print(f"Исправлено {updated_count} оценок!")
        else:
            print("Нет плохих оценок для исправления!")

    except (StudentNotFoundError, MultipleStudentsError, LessonNotFoundError) as e:
        print(e)
    except DatabaseError as e:
        print(f"Ошибка базы данных: {e}")
