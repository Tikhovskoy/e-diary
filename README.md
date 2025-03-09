# db-hack

Скрипты для редактирования базы данных электронного дневника.  
Позволяют исправлять оценки, удалять замечания и добавлять похвалу.

## Установка и запуск

1. **Склонируйте репозиторий:**
   ```sh
   git clone https://github.com/ТВОЙ_GITHUB/e-diary-scripts.git
   cd e-diary-scripts
   ```

2. **Перейдите в папку с сайтом (если скрипты рядом с `manage.py`):**
   ```sh
   cd ~/e-diary
   ```

3. **Активируйте виртуальное окружение:**
   ```sh
   source venv/bin/activate
   ```

4. **Запустите Django Shell:**
   ```sh
   python manage.py shell
   ```

5. **Подключите скрипт (например, для похвалы):**
   ```python
   exec(open("commendations.py").read())
   ```

6. **Вызовите нужную функцию, например, для похвалы:**
   ```python
   create_commendation("Фролов Иван", "Музыка")
   ```

---

## 🔹 Доступные скрипты и функции

### `fix_marks.py` – Исправление оценок
- `fix_marks(schoolkid)`: Исправляет все двойки и тройки на пятёрки.

### `fix_chastisements.py` – Удаление замечаний
- `remove_chastisements(schoolkid)`: Удаляет все замечания ученика.

### `commendations.py` – Добавление похвалы
- `create_commendation(schoolkid_name, subject_title)`:  
  Добавляет похвалу на **последний урок** по указанному предмету.

---

## **Пример использования**
```python
# Исправляем оценки Вани
exec(open("fix_marks.py").read())
kid = Schoolkid.objects.get(full_name__contains="Фролов Иван")
fix_marks(kid)

# Удаляем замечания Вани
exec(open("fix_chastisements.py").read())
remove_chastisements(kid)

# Добавляем похвалу по математике
exec(open("commendations.py").read())
create_commendation("Фролов Иван", "Математика")
```

