# db-hack

Скрипты для редактирования базы данных электронного дневника.  
Позволяют исправлять оценки, удалять замечания и добавлять похвалу.

## Установка и запуск

### **Склонируйте репозиторий**
Скачайте код с GitHub и перейдите в папку со скриптами:
```sh
git clone https://github.com/Tikhovskoy/e-diary.git
cd e-diary
```

### **Активируйте виртуальное окружение**
Перед запуском скриптов нужно активировать Python-окружение проекта:
```sh
source venv/bin/activate
```

### **Запустите Django без `manage.py`**
Теперь можно загружать Django через `run_shell.py`:
```sh
python run_shell.py
```
Должно появиться сообщение:
```
Django загружен, можно использовать скрипты.
```

### **Импортируйте скрипты**
```python
import fix_marks
import fix_chastisements
import commendations
```

### **Используйте нужные функции**  
Примеры:

- **Находим ученика**
  ```python
  from datacenter.models import Schoolkid
  kid = Schoolkid.objects.get(full_name__contains="Фролов Иван")
  ```

- **Исправляем оценки**
  ```python
  fix_marks.fix_marks(kid)
  ```

- **Удаляем замечания**
  ```python
  fix_chastisements.remove_chastisements(kid)
  ```

- **Добавляем похвалу по математике**
  ```python
  commendations.create_commendation("Фролов Иван", "Математика")
  ```

---

## Доступные скрипты и функции

### ** Исправление оценок – `fix_marks.py`**
- `fix_marks(schoolkid)`: Исправляет все **двойки** и **тройки** ученика, заменяя их на **пятёрки**.

### ** Удаление замечаний – `fix_chastisements.py`**
- `remove_chastisements(schoolkid)`: Удаляет **все замечания** у ученика.

### ** Добавление похвалы – `commendations.py`**
- `create_commendation(schoolkid_name, subject_title)`:  
  Добавляет **похвалу** на последний урок по указанному предмету.

