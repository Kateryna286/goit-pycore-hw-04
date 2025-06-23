# GOIT-PYCORE-HW-04

Домашнє завдання 4 з курсу Python.

## Структура

```
GOIT-PYCORE-HW-04/
├── data/ ---> вхідні файли для завдань
├── scripts/ ---> всі виконувані скрипти-завдання
│ ├── bot_assistant.py ---> консольний бот для роботи з контактами
│ ├── get_cats_info.py ---> читає файл з інформацією про котів і виводить список словників
│ ├── total_salary.py ---> обчислює загальну та середню зарплати з файлу
│ └── get_dir_structure.py ---> виводить структуру директорії з кольоровим форматуванням
├── .gitignore
├── README.md
├── requirements.txt
└── .venv/ ← віртуальне середовище (сховане у VS Code)
```

## Як працювати з проєктом

### 1. Клонувати репозиторій

```bash
git clone https://github.com/your-username/GOIT-PYCORE-HW-04.git
cd GOIT-PYCORE-HW-04
```

### 2. Створити та активувати віртуальне середовище

```bash
python -m venv .venv
source .venv/bin/activate  # для macOS/Linux
# або .venv\Scripts\activate.bat для Windows
```

### 3. Встановити залежності

```bash
pip install -r requirements.txt
```

### 4. Запустити завдання

```bash
python3 scripts/get_cats_info.py
python3 scripts/total_salary.py
python3 scripts/get_dir_structure.py
python3 scripts/bot_assistant.py
```

## Примітки

- Папки `.venv/`, `__pycache__/`, `.vscode/` додані у `.gitignore` і не завантажуються до репозиторію.
- Усі завдання використовують спільне віртуальне середовище.
- Якщо з’являться нові залежності — онови файл `requirements.txt` за допомогою:

```bash
pip freeze > requirements.txt
```
