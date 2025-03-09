from datacenter.models import Schoolkid, Mark

def fix_marks(schoolkid):

    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    count = bad_marks.count()

    if count == 0:
        print("Нет плохих оценок для исправления!")
        return

    bad_marks.update(points=5)
    print(f"Исправлено {count} оценок!")
