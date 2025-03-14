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
После этого можно **импортировать скрипты**.

### **Импортируйте `db_tools.py`**
```python
import db_tools
```

### **Используйте нужные функции**  
Примеры:

- **Находим ученика**
  ```python
  kid = db_tools.get_schoolkid("Фролов Иван")
  ```

- **Исправляем оценки**
  ```python
  db_tools.fix_marks("Фролов Иван")
  ```

- **Удаляем замечания**
  ```python
  db_tools.remove_chastisements("Фролов Иван")
  ```

- **Добавляем похвалу по математике**
  ```python
  db_tools.create_commendation("Фролов Иван", "Математика")
  ```

---

## Доступные функции в `db_tools.py`

### **Исправление оценок**
- `fix_marks(schoolkid_name)`: Исправляет все **двойки** и **тройки** ученика, заменяя их на **пятёрки**.

### **Удаление замечаний**
- `remove_chastisements(schoolkid_name)`: Удаляет **все замечания** у ученика.

### **Добавление похвалы**
- `create_commendation(schoolkid_name, subject_title)`:  
  Добавляет **похвалу** на последний урок по указанному предмету.

### **Поиск ученика**
- `get_schoolkid(schoolkid_name)`:  
  Возвращает **объект ученика**, если найден.

