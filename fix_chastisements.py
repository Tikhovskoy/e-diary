from datacenter.models import Schoolkid, Chastisement

def remove_chastisements(schoolkid):

    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    count = chastisements.count()

    if count == 0:
        print(f"У {schoolkid.full_name} нет замечаний!")
        return

    chastisements.delete()
    print(f"Удалено {count} замечаний у {schoolkid.full_name}!")

