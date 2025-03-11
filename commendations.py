import random
from datacenter.models import Schoolkid, Lesson, Commendation

COMMENDATION_TEXTS = [
    "Молодец!",
    "Отлично!",
    "Хорошая работа!",
    "Так держать!",
    "Прекрасно!"
]

class StudentNotFoundError(Exception):
    """Исключение, если ученик не найден"""
    pass

class MultipleStudentsError(Exception):
    """Исключение, если найдено несколько учеников"""
    pass

class LessonNotFoundError(Exception):
    """Исключение, если не найден урок по предмету"""
    pass

def create_commendation(schoolkid_name, subject_title):
    try:
        try:
            kid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        except Schoolkid.DoesNotExist:
            raise StudentNotFoundError(f"Ошибка: Ученик {schoolkid_name} не найден!")
        except Schoolkid.MultipleObjectsReturned:
            raise MultipleStudentsError(f"Ошибка: Найдено несколько учеников с именем {schoolkid_name}. Уточните запрос!")

        lesson = Lesson.objects.filter(
            year_of_study=kid.year_of_study,
            group_letter=kid.group_letter,
            subject__title=subject_title
        ).order_by("-date").first()

        if not lesson:
            raise LessonNotFoundError(f"Не найдено занятий по предмету {subject_title} для {kid.full_name}.")

        Commendation.objects.create(
            text=random.choice(COMMENDATION_TEXTS),
            schoolkid=kid,
            subject=lesson.subject,
            teacher=lesson.teacher,
            created=lesson.date
        )

        print(f"Похвала добавлена для {kid.full_name} на уроке {subject_title}!")

    except (StudentNotFoundError, MultipleStudentsError, LessonNotFoundError) as e:
        print(e)
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
