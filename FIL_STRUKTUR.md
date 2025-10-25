# 📁 PROJEKT STRUKTUR OVERSIGT

## Komplet fil hierarki

```
my-calculator-project/
│
├── 📄 README.md                    # Hovedvejledning (start her!)
├── 📄 HURTIG_START.md              # Trin-for-trin guide
├── 📄 PIPELINE_FORKLARING.md       # CI/CD forklaring
├── 📄 requirements.txt             # Python dependencies
├── 📄 setup.py                     # Package installation setup
├── 📄 .gitignore                   # Filer Git skal ignorere
│
├── 📂 .github/                     # ⭐ GitHub konfiguration
│   └── 📂 workflows/
│       └── 📄 ci-cd.yml           # 🚀 CI/CD PIPELINE - VIGTIG!
│
├── 📂 my_calculator/               # ⭐ Hovedkoden
│   ├── 📄 __init__.py             # Markerer det som Python package
│   └── 📄 calculator.py           # Calculator klasse (DETTE EDITERER DU)
│
└── 📂 tests/                       # ⭐ Test filer
    └── 📄 test_calculator.py      # Tests for calculator (DETTE EDITERER DU)
```

## 🔥 De vigtigste filer at kende

### 1️⃣ `.github/workflows/ci-cd.yml`
**DETTE ER HJERTET I CI/CD!**
- Definerer hvad der skal ske automatisk
- Køres hver gang du pusher kode
- Du behøver SJÆLDENT at ændre denne fil

**Hvad den gør:**
```yaml
1. Hent kode fra GitHub
2. Opsæt Python miljø
3. Installer dependencies
4. Kør alle tests
5. Check kode kvalitet
6. Rapporter resultat (✅ eller ❌)
```

### 2️⃣ `my_calculator/calculator.py`
**DIN HOVEDKODE**
- Her skriver du din funktionalitet
- Dette er det du primært arbejder i
- Prøv at tilføje nye metoder her!

### 3️⃣ `tests/test_calculator.py`
**DINE TESTS**
- Hver funktion skal have mindst én test
- Tests sikrer din kode virker
- Pipeline'en kører disse automatisk

### 4️⃣ `requirements.txt`
**DEPENDENCIES**
- Liste over Python packages der skal installeres
- pytest = test framework
- pytest-cov = test coverage rapport

### 5️⃣ `README.md`
**DOKUMENTATION**
- Forklarer hvad projektet er
- Setup instruktioner
- Øvelser at prøve

## 🎯 Typisk workflow

### Du redigerer primært:
1. ✏️ `my_calculator/calculator.py` (ny funktionalitet)
2. ✏️ `tests/test_calculator.py` (tests for ny funktionalitet)

### Sjældent redigeret:
- ⚙️ `.github/workflows/ci-cd.yml` (kun hvis du vil ændre pipeline)
- 📦 `requirements.txt` (kun hvis du tilføjer nye dependencies)
- ⚙️ `setup.py` (kun hvis du vil publicere package)

### Aldrig redigeret:
- 🚫 `__init__.py` filer (medmindre du ved hvad du gør)
- 🚫 `.gitignore` (medmindre du har specielle behov)

## 📝 Quick reference

| Fil | Hvad er det? | Redigerer du det? |
|-----|--------------|-------------------|
| `calculator.py` | Din kode | ✅ Ja, ofte |
| `test_calculator.py` | Dine tests | ✅ Ja, ofte |
| `ci-cd.yml` | Pipeline setup | ⚠️ Sjældent |
| `requirements.txt` | Dependencies | ⚠️ Sjældent |
| `README.md` | Dokumentation | ⚠️ Efter behov |
| `__init__.py` | Package marker | 🚫 Sjældent |

## 💡 Tips til organisering

### Når du tilføjer ny funktionalitet:
1. Skriv funktionen i `calculator.py`
2. Skriv tests i `test_calculator.py`
3. Test lokalt: `pytest tests/ -v`
4. Push til GitHub
5. Se CI/CD køre!

### God praksis:
```
1. Én funktion → Mindst én test
2. Test lokalt før push
3. Små, hyppige commits
4. Beskrivende commit beskeder
```

## 🔍 Hvad skal du se i VSCode?

Når du åbner projektet i VSCode:
```
EXPLORER PANEL (venstre side):
├── .github/         ← Åbn og se ci-cd.yml
├── my_calculator/   ← DIN KODE HER
├── tests/           ← TESTS HER
├── README.md        ← Start dokumentation
└── requirements.txt ← Dependencies
```

## 🚀 Kommanndoer at huske

```bash
# Se fil struktur
ls -la

# Se test coverage
pytest tests/ -v --cov=my_calculator

# Se hvad der skal committes
git status

# Se historik
git log --oneline
```

---

**Næste skridt:** Læs HURTIG_START.md for at komme i gang! 🎉
