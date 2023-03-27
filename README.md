# MoveFiles App

Версия Python: 3.10.10

*Windows утилита для переноса файлов, Access time которых превышает указанное количество дней. Изначально создана для копирования старых файлов на другой жесткий диск.*

## Описание проекта
Для сбора exe файла проекта используется вспомогательный файл *generate_exe.py*, который запускается из консоли.
Формат запуска: *python generate_exe.py -sn **{исходный файл}** -fn **{название конечного файла}***

Исходный файл в данном случае: *ui.py*
Название конечного файла должно быть передано без расширения, например, *MoveFiles*, а не *MoveFiles.exe*

## Технологии:
- tkinter (для оконного интерфейса утилиты)
- pyinstaller (для сбора exe файла)

## Алгоритм:
- Утилита получает начальный и конечный путь, а также условие по количеству дней
- Дублирует полный путь до директории в конечном пути | *таким образом, например, при копировании из **C:\\Users\\User\\Downloads** в **D:\\** конечная директория **D:\\** получает путь **D:\\Users\\User\\Downloads** в который и будут перенесены все подходящие файлы*
- Проходит по начальному пути рекурсивной функцией прохода папок, если находит папку - заходит в неё и продолжает путь в ней. Если находит - файл, проверяет условие и при удовлетворении условия - переносит файл
- В процессе такого сбора могут образовываться пустые папки как в начальном, так и в конечном пути (например, когда условие не соблюдено ни для одного файла из папки или все файлы перенесены или папка пустая), для этого в конце переноса делается дополнительный проход по директории и пустые папки удаляются
- В главную функцию возвращается количество перенесенных файлов и отображается в интерфейсе

## Описание структуры
1. В качестве названия для виртуального окружения используется *move_env*, данное название зафиксировано в *.gitignore*
2. Сборка интерфейса полностью заложена в файле *ui.py*, в файле *utils.py* для изменения содержания используются только отдельные элементы интерфейса (прогрессбар, строка состояния)
3. Все необходимые библиотеки описаны в файле *requirements.txt*
