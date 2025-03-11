from datacenter.models import Chastisement
from commendations import get_schoolkid

def remove_chastisements(schoolkid_name):
    try:
        schoolkid = get_schoolkid(schoolkid_name)
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        deleted_count, _ = chastisements.delete()

        if deleted_count:
            print(f"Удалено {deleted_count} замечаний у {schoolkid.full_name}!")
        else:
            print(f"У {schoolkid.full_name} нет замечаний!")

    except Exception as e:
        print(f"Ошибка: {e}")
