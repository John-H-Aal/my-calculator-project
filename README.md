# My Calculator - CI/CD Demo Project

![CI/CD Status](https://github.com/John-H-Aal/my-calculator-project/workflows/CI%2FCD%20Pipeline/badge.svg)

Et simpelt Python package der demonstrerer GitHub CI/CD pipeline med automatisk testing.

## 📋 Indholdsfortegnelse

- [Features](#features)
- [Krav](#krav)
- [Installation](#installation)
- [Brug](#brug)
- [CI/CD Pipeline](#cicd-pipeline)
- [Udvikling](#udvikling)
- [Test](#test)
- [Fejlfinding](#fejlfinding)

## ✨ Features

- ✅ Komplet Calculator klasse med grundlæggende operationer
- ✅ 100% test coverage
- ✅ Automatisk CI/CD pipeline via GitHub Actions
- ✅ Kode kvalitets check med flake8
- ✅ Virtual environment support

## 📦 Krav

- Python 3.8 eller nyere
- pip (Python package manager)
- Git

## 🚀 Installation

### 1. Klon repository
```bash
git clone https://github.com/John-H-Aal/my-calculator-project.git
cd my-calculator-project
```

### 2. Opret og aktiver virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer dependencies
```bash
pip install -r requirements.txt
```

### 4. Installer projektet i editable mode
```bash
pip install -e .
```

Dette er **vigtigt** for at Python kan finde `my_calculator` modulet.

## 💻 Brug

### Som Python modul

```python
from my_calculator import Calculator

calc = Calculator()

# Basale operationer
print(calc.add(5, 3))        # 8
print(calc.subtract(10, 4))  # 6
print(calc.multiply(3, 7))   # 21
print(calc.divide(15, 3))    # 5.0

# Division by zero håndtering
try:
    calc.divide(10, 0)
except ValueError as e:
    print(e)  # "Kan ikke dividere med nul!"
```

## 🔄 CI/CD Pipeline

Projektet bruger GitHub Actions til automatisk CI/CD. Ved hver push til `main` branch:

1. ✅ **Setup** - Forbereder miljø
2. ✅ **Checkout** - Henter koden
3. ✅ **Python Setup** - Installerer Python 3.11
4. ✅ **Dependencies** - Installerer packages og projektet
5. ✅ **Tests** - Kører alle tests med coverage rapport
6. ✅ **Kvalitet** - Checker kode med flake8

**Total tid:** ~30 sekunder

Se pipeline status: [GitHub Actions](https://github.com/John-H-Aal/my-calculator-project/actions)

## 🛠️ Udvikling

### Projekt struktur
```
my-calculator-project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD konfiguration
├── my_calculator/
│   ├── __init__.py            # Package initialisering
│   └── calculator.py          # Hovedkoden
├── tests/
│   └── test_calculator.py     # Test suite
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── .gitignore                 # Git ignore filer
└── README.md                  # Denne fil
```

### Tilføj ny funktionalitet

**1. Skriv funktionen** i `my_calculator/calculator.py`:
```python
def power(self, a, b):
    """Opløft a til b'te potens"""
    return a ** b
```

**2. Skriv tests** i `tests/test_calculator.py`:
```python
def test_power():
    """Test potens funktion"""
    calc = Calculator()
    assert calc.power(2, 3) == 8
    assert calc.power(5, 2) == 25
    assert calc.power(10, 0) == 1
```

**3. Test lokalt:**
```bash
pytest tests/ -v
```

**4. Commit og push:**
```bash
git add .
git commit -m "Added power function"
git push origin main
```

**5. Se CI/CD køre** på GitHub Actions tab

## 🧪 Test

### Kør alle tests
```bash
pytest tests/ -v
```

### Med coverage rapport
```bash
pytest tests/ --cov=my_calculator --cov-report=term-missing
```

### Generer HTML coverage rapport
```bash
pytest tests/ --cov=my_calculator --cov-report=html
# Åbn htmlcov/index.html i browser
```

### Kør specifik test
```bash
pytest tests/test_calculator.py::test_add -v
```

### Watch mode (kører tests ved ændringer)
```bash
pip install pytest-watch
ptw
```

## 🔍 Kode kvalitet

### Check med flake8
```bash
flake8 my_calculator/ tests/
```

### Se coverage status
```bash
pytest tests/ --cov=my_calculator
```

**Mål:** Minimum 80% coverage (aktuelt: 100%)

## 🆘 Fejlfinding

### Problem: `ModuleNotFoundError: No module named 'my_calculator'`

**Løsning:**
```bash
# Aktiver venv først
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Installer projektet
pip install -e .
```

### Problem: `pytest: command not found`

**Løsning:**
```bash
# Aktiver venv
source venv/bin/activate  # Mac/Linux

# Installer dependencies
pip install -r requirements.txt
```

### Problem: Tests fejler lokalt men virker i CI/CD

**Løsning:**
```bash
# Geninstaller alt fra scratch
deactivate
rm -rf venv/
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v
```

### Problem: CI/CD pipeline fejler

1. Gå til **Actions** tab på GitHub
2. Klik på den fejlede workflow run
3. Udvid det fejlede step
4. Læs fejlbeskeden
5. Ret fejlen lokalt
6. Test lokalt: `pytest tests/ -v`
7. Push igen

## 📊 Status badges

Tilføj til dit projekt README:

```markdown
![CI/CD Status](https://github.com/John-H-Aal/my-calculator-project/workflows/CI%2FCD%20Pipeline/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
```

## 🤝 Bidrag

1. Fork projektet
2. Opret feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit ændringer (`git commit -m 'Add some AmazingFeature'`)
4. Push til branch (`git push origin feature/AmazingFeature`)
5. Åbn Pull Request

## 📚 Yderligere dokumentation

- [HURTIG_START.md](HURTIG_START.md) - Step-by-step begynder guide
- [PIPELINE_FORKLARING.md](PIPELINE_FORKLARING.md) - Detaljeret CI/CD forklaring
- [FIL_STRUKTUR.md](FIL_STRUKTUR.md) - Projekt struktur oversigt
- [KUNDE_PITCH.md](KUNDE_PITCH.md) - Business værdi og ROI argumenter

## 📝 License

Dette er et demo projekt til læring og demonstration.

## 👤 Forfatter

**John-H-Aal**
- GitHub: [@John-H-Aal](https://github.com/John-H-Aal)

## 🙏 Anerkendelser

- [pytest](https://pytest.org/) - Testing framework
- [GitHub Actions](https://github.com/features/actions) - CI/CD platform
- [flake8](https://flake8.pycqa.org/) - Code quality tool

---

**God fornøjelse med CI/CD! 🚀**

*For spørgsmål eller problemer, åbn et issue på GitHub.*
