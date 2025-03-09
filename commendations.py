import random
from datacenter.models import Schoolkid, Lesson, Commendation

def create_commendation(schoolkid_name, subject_title):

    try:
        kids = Schoolkid.objects.filter(full_name__contains=schoolkid_name)

        if kids.count() > 1:
            print(f"Найдено несколько учеников с именем {schoolkid_name}. Уточните запрос!")
            return
        elif kids.count() == 0:
            print(f"Ученик с именем {schoolkid_name} не найден!")
            return

        kid = kids.first()

        lesson = Lesson.objects.filter(
            year_of_study=kid.year_of_study,
            group_letter=kid.group_letter,
            subject__title=subject_title
        ).order_by("-date").first()

        if not lesson:
            print(f"Не найдено занятий по предмету {subject_title} для {kid.full_name}.")
            return

        commendation_texts = [
            "Молодец!",
            "Отлично!",
            "Хорошая работа!",
            "Так держать!",
            "Прекрасно!"
        ]

        Commendation.objects.create(
            text=random.choice(commendation_texts),
            schoolkid=kid,
            subject=lesson.subject,
            teacher=lesson.teacher,
            created=lesson.date
        )

        print(f"Похвала добавлена для {kid.full_name} на уроке {subject_title}!")

    except Exception as e:
        print(f"Ошибка: {e}")
