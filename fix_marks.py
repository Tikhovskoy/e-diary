from datacenter.models import Schoolkid, Mark

def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    updated_count = bad_marks.update(points=5)

    if updated_count:
        print(f"Исправлено {updated_count} оценок!")
    else:
        print("Нет плохих оценок для исправления!")