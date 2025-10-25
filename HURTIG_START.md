# 🚀 HURTIG START GUIDE - CI/CD Demo

## Trin 1: Download projektet
Du har nu alle filerne. Lav en ny folder på din computer, f.eks. `my-calculator-project`

## Trin 2: Opret GitHub Repository
1. Gå til https://github.com/John-H-Aal
2. Klik på "+" og vælg "New repository"
3. Navn: `my-calculator-project`
4. Vælg "Public" eller "Private"
5. VIGTIGT: Lad "Add README" være UMARKERET (vi har allerede en)
6. Klik "Create repository"

## Trin 3: Upload koden (vælg EN af metoderne)

### Metode A: Via VSCode (anbefalet)
1. Åbn VSCode
2. Åbn din projekt folder
3. Kopier alle downloadede filer til folderen
4. Åbn Terminal i VSCode (Ctrl+Shift+Ø eller View > Terminal)
5. Kør følgende kommandoer:

```bash
git init
git add .
git commit -m "Initial commit - CI/CD setup"
git branch -M main
git remote add origin https://github.com/John-H-Aal/my-calculator-project.git
git push -u origin main
```

### Metode B: Via GitHub Desktop
1. Åbn GitHub Desktop
2. Klik "Add" > "Create new repository"
3. Vælg din projekt folder
4. Klik "Publish repository"

## Trin 4: Opsæt lokalt udviklings miljø (venv)

**VIGTIGT: Brug altid virtual environment når du udvikler!**

### Hvad er venv?
Virtual environment er en isoleret Python installation kun til dit projekt. Det betyder:
- ✅ Ingen konflikter med andre projekter
- ✅ Nem at dele (via requirements.txt)
- ✅ Professionel best practice

### Opsæt venv:

**Windows:**
```bash
# Opret virtual environment
python -m venv venv

# Aktiver det
venv\Scripts\activate

# Du vil se (venv) i din terminal nu!
```

**Mac/Linux:**
```bash
# Opret virtual environment
python3 -m venv venv

# Aktiver det
source venv/bin/activate

# Du vil se (venv) i din terminal nu!
```

### Installer dependencies:
```bash
# Sørg for venv er aktiveret først!
pip install -r requirements.txt
```

### Test lokalt:
```bash
# Kør alle tests
pytest tests/ -v

# Kør tests med coverage
pytest tests/ -v --cov=my_calculator
```

### Deaktiver venv når du er færdig:
```bash
deactivate
```

## Trin 5: Se CI/CD i aktion! 🎉
1. Gå til https://github.com/John-H-Aal/my-calculator-project
2. Klik på "Actions" tab
3. Du vil se din første pipeline køre!

## Trin 6: Test det virker
1. I VSCode, åbn `my_calculator/calculator.py`
2. Tilføj en ny metode:

```python
def square(self, a):
    """Opløft tal i anden potens"""
    return a * a
```

3. Tilføj en test i `tests/test_calculator.py`:

```python
def test_square():
    calc = Calculator()
    assert calc.square(5) == 25
    assert calc.square(0) == 0
```

4. Gem filerne
5. I Terminal:
```bash
git add .
git commit -m "Added square function"
git push
```

6. Gå til GitHub Actions og se pipeline'en køre igen! ✅

## Hvad skal du se efter?
- Grøn check mark = SUCCESS! 🎉
- Rød X = Noget gik galt (klik for at se hvad)

## Daglig workflow med venv

**Hver gang du starter arbejde på projektet:**

```bash
# 1. Åbn projektet i VSCode
# 2. Åbn Terminal (Ctrl+Shift+Ø)

# 3. Aktiver venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# 4. Nu er du klar til at kode!
# Du vil se (venv) i din terminal prompt

# 5. Test ændringer lokalt
pytest tests/ -v

# 6. Push til GitHub
git add .
git commit -m "Din besked"
git push

# 7. Deaktiver når du er færdig
deactivate
```

## Tips til venv

✅ **Aktiver altid venv før du koder**
✅ **Installer nye packages i venv:** `pip install package-navn`
✅ **Opdater requirements.txt:** `pip freeze > requirements.txt`
✅ **venv/ folder skal IKKE committes** (allerede i .gitignore)

## Fejlfinding

**Problem:** `pytest: command not found`
**Løsning:** Husk at aktivere venv først!

**Problem:** `ModuleNotFoundError`
**Løsning:** Kør `pip install -r requirements.txt` i aktiveret venv

## Næste skridt
- Læs README.md for flere detaljer
- Prøv at lave en fejl og se hvad der sker
- Eksperimenter med koden!

## Hurtige kommandoer

**Kør tests lokalt:**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
pytest tests/ -v
```

**Push ændringer:**
```bash
git add .
git commit -m "Din besked her"
git push
```

God fornøjelse! 🚀
