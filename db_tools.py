import random
from datacenter.models import Schoolkid, Lesson, Commendation, Mark, Chastisement
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, DatabaseError

COMMENDATION_TEXTS = [
    "Молодец!",
    "Отлично!",
    "Хорошая работа!",
    "Так держать!",
    "Прекрасно!"
]

class StudentNotFoundError(Exception):
    """Вызывается, если ученик не найден в базе данных."""
    pass

class MultipleStudentsError(Exception):
    """Вызывается, если найдено несколько учеников с одним именем."""
    pass

class LessonNotFoundError(Exception):
    """Вызывается, если не найден урок по заданному предмету."""
    pass

def get_schoolkid(schoolkid_name):
    """
    Ищет ученика в базе данных по имени.

    :param schoolkid_name: Имя ученика (или его часть).
    :return: Объект Schoolkid, если найден.
    :raises StudentNotFoundError: Если ученик не найден.
    :raises MultipleStudentsError: Если найдено несколько учеников с одинаковым именем.
    """
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except ObjectDoesNotExist:
        raise StudentNotFoundError(f"Ошибка: Ученик {schoolkid_name} не найден!")
    except MultipleObjectsReturned:
        raise MultipleStudentsError(f"Ошибка: Найдено несколько учеников с именем {schoolkid_name}. Уточните запрос!")

def fix_marks(schoolkid_name):
    """
    Исправляет все двойки и тройки ученика на пятёрки.

    :param schoolkid_name: Имя ученика (или его часть).
    """
    try:
        schoolkid = get_schoolkid(schoolkid_name)
        bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
        updated_count = bad_marks.update(points=5)

        if updated_count:
            print(f"Исправлено {updated_count} оценок!")
        else:
            print("Нет плохих оценок для исправления!")

    except (StudentNotFoundError, MultipleStudentsError) as e:
        print(e)
    except DatabaseError as e:
        print(f"Ошибка базы данных: {e}")

def remove_chastisements(schoolkid_name):
    """
    Удаляет все замечания ученика.

    :param schoolkid_name: Имя ученика (или его часть).
    """
    try:
        schoolkid = get_schoolkid(schoolkid_name)
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        deleted_count, _ = chastisements.delete()

        if deleted_count:
            print(f"Удалено {deleted_count} замечаний у {schoolkid.full_name}!")
        else:
            print(f"У {schoolkid.full_name} нет замечаний!")

    except (StudentNotFoundError, MultipleStudentsError) as e:
        print(e)
    except DatabaseError as e:
        print(f"Ошибка базы данных: {e}")

def create_commendation(schoolkid_name, subject_title):
    """
    Добавляет похвалу ученику за последний урок по указанному предмету.

    :param schoolkid_name: Имя ученика (или его часть).
    :param subject_title: Название предмета (например, "Математика").
    """
    try:
        kid = get_schoolkid(schoolkid_name)

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
