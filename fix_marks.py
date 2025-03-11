from datacenter.models import Mark
from commendations import get_schoolkid

def fix_marks(schoolkid_name):
    try:
        schoolkid = get_schoolkid(schoolkid_name)
        bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        updated_count = bad_marks.update(points=5)

        if updated_count:
            print(f"Исправлено {updated_count} оценок!")
        else:
            print("Нет плохих оценок для исправления!")

    except Exception as e:
        print(f"Ошибка: {e}")
