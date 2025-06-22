# GOIT-PYCORE-HW-04

Домашнє завдання №4 з курсу Python Core.

## Структура

```
GOIT-PYCORE-HW-04/
├── data/ ← вхідні файли для завдань
├── scripts/ ← всі виконувані скрипти-завдання
│ ├── get_cats_info.py
│ ├── get_cats_info.py
│ ├── total_salary.py
│ └── get_dir_structure.py
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
python get_cats_info.py
python total_salary.py
python get_dir_structure.py
python bot_assistant.py
```

## Примітки

- Папки `.venv/`, `__pycache__/`, `.vscode/` додані у `.gitignore` і не завантажуються до репозиторію.
- Усі завдання використовують спільне віртуальне середовище.
- Якщо з’являться нові залежності — онови файл `requirements.txt` за допомогою:

```bash
pip freeze > requirements.txt
```
