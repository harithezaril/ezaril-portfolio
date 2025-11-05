#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

### **3. Save the file** (Ctrl + S)

---

## Your project structure should look like:
```
myportfolio/
├── myportfolio/
├── home/
├── contact/
├── venv/
├── manage.py
├── requirements.txt  ✅ (you just created this)
├── build.sh          ✅ (create this now)
└── db.sqlite3