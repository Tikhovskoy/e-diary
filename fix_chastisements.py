from datacenter.models import Schoolkid, Chastisement

def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    deleted_count, _ = chastisements.delete()

    if deleted_count:
        print(f"Удалено {deleted_count} замечаний у {schoolkid.full_name}!")
    else:
        print(f"У {schoolkid.full_name} нет замечаний!")