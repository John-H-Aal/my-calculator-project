# 🌿 Git Branch Workflow Guide

Komplet guide til at arbejde med branches, merge, push og pull i dit CI/CD projekt.

## 📋 Indholdsfortegnelse

1. [Git Basics](#git-basics)
2. [Branch Workflow](#branch-workflow)
3. [Daglig Workflow](#daglig-workflow)
4. [Pull Requests](#pull-requests)
5. [Merge Strategier](#merge-strategier)
6. [Fejlfinding](#fejlfinding)
7. [Best Practices](#best-practices)
8. [Cheat Sheet](#cheat-sheet)

---

## 🎯 Git Basics

### Hvad er hvad?

**Branch:**
- En parallel version af din kode
- Lader dig arbejde på nye features uden at påvirke main
- Tænk: Separate arbejdsrum

**Commit:**
- Et snapshot af dine ændringer
- Permanent historie af hvad der blev ændret
- Tænk: Save point i et spil

**Push:**
- Send dine lokale commits til GitHub
- Gør dine ændringer synlige for andre
- Tænk: Upload til skyen

**Pull:**
- Hent ændringer fra GitHub til din lokale computer
- Hold din kode opdateret
- Tænk: Download fra skyen

**Merge:**
- Kombiner to branches
- Integrer din feature i main
- Tænk: Flet to dokumenter sammen

---

## 🌿 Branch Workflow

### Branch navngivning

**Brug beskrivende navne:**

```bash
# ✅ GODT:
feature/add-square-function
fix/division-by-zero-error
refactor/clean-calculator-code
docs/update-readme
test/improve-coverage

# ❌ DÅRLIGT:
new-stuff
fix
test123
johns-branch
```

**Konventioner:**
- `feature/` - Ny funktionalitet
- `fix/` - Bug fixes
- `refactor/` - Code forbedringer
- `docs/` - Dokumentation
- `test/` - Test forbedringer
- `chore/` - Vedligehold (dependencies osv.)

### Se dine branches

```bash
# Se lokale branches
git branch

# Se alle branches (inkl. remote)
git branch -a

# Se hvilken branch du er på
git status
```

---

## 📅 Daglig Workflow

### Scenario 1: Start ny feature

```bash
# 1. Sørg for du er på main og har seneste ændringer
git checkout main
git pull origin main

# 2. Lav ny feature branch
git checkout -b feature/add-square-function

# 3. Verificer du er på den nye branch
git branch
# * feature/add-square-function  (← stjerne = aktiv branch)
#   main
```

### Scenario 2: Arbejd på din feature

```bash
# 1. Lav dine ændringer i VSCode
# - Rediger filer
# - Tilføj ny funktionalitet
# - Skriv tests

# 2. Se hvad der er ændret
git status

# 3. Test lokalt
pytest tests/ -v

# 4. Tilføj dine ændringer til staging
git add .
# Eller specifik fil:
git add my_calculator/calculator.py tests/test_calculator.py

# 5. Commit med beskrivende besked
git commit -m "Added square function with comprehensive tests"

# 6. Push til GitHub
git push origin feature/add-square-function
```

### Scenario 3: Se GitHub Actions teste din branch

```bash
# Efter push:
# 1. Gå til GitHub.com
# 2. Dit repository → Actions tab
# 3. Se din branch blive testet ✅
# Men den deployer IKKE til Railway endnu!
```

### Scenario 4: Merge til main

**Option A: Via GitHub Pull Request (Anbefalet)**

```bash
# 1. Din branch er pushed
git push origin feature/add-square-function

# 2. På GitHub.com:
# - Gå til repository
# - Klik "Pull requests"
# - Klik "New pull request"
# - Base: main, Compare: feature/add-square-function
# - Klik "Create pull request"
# - Skriv beskrivelse
# - Vent på at tests er grønne ✅
# - Klik "Merge pull request"
# - Klik "Confirm merge"

# 3. Opdater din lokale main
git checkout main
git pull origin main

# 4. Slet feature branch (valgfrit)
git branch -d feature/add-square-function
git push origin --delete feature/add-square-function
```

**Option B: Direkte merge lokalt**

```bash
# 1. Skift til main
git checkout main

# 2. Hent seneste fra GitHub
git pull origin main

# 3. Merge din feature
git merge feature/add-square-function

# 4. Push til GitHub
git push origin main

# 5. Nu deployer Railway! 🚀

# 6. Slet feature branch (valgfrit)
git branch -d feature/add-square-function
```

---

## 🔄 Pull Requests (PRs)

### Hvad er en Pull Request?

En formel anmodning om at merge din branch til main:
- ✅ Code review mulighed
- ✅ Diskussion af ændringer
- ✅ Automatiske tests
- ✅ Historik og dokumentation

### Lav en god PR

**1. Beskrivende titel:**
```
✅ GODT: "Add square function with comprehensive tests"
❌ DÅRLIGT: "Update"
```

**2. God beskrivelse:**
```markdown
## Hvad
Tilføjet square() funktion til Calculator klasse

## Hvorfor
Kunder har bedt om mulighed for at kvadrere tal

## Ændringer
- Tilføjet square() metode i calculator.py
- Tilføjet test_square() med 5 test cases
- Opdateret README med dokumentation

## Test
- ✅ Alle tests bestået lokalt
- ✅ Coverage stadig 100%
- ✅ GitHub Actions grøn

## Screenshots
[hvis relevant]
```

**3. Link til issue (hvis relevant):**
```markdown
Fixes #42
Closes #38
```

### Review din egen PR

```bash
# Før du laver PR:
1. Kør tests lokalt
   pytest tests/ -v

2. Check code quality
   flake8 .

3. Læs dine ændringer igennem
   git diff main

4. Test i browser (hvis web app)
   python app.py
```

---

## 🔀 Merge Strategier

### Strategy 1: Merge Commit (Standard)

```bash
git checkout main
git merge feature/add-square-function
```

**Resultat:**
```
main:     A---B---C-------E
                   \     /
feature:            D---/
```

**Fordele:**
- ✅ Bevarer fuld historie
- ✅ Kan se hvornår feature blev merged

**Ulemper:**
- ⚠️ Mange merge commits kan rode historikken

### Strategy 2: Squash Merge

```bash
git checkout main
git merge --squash feature/add-square-function
git commit -m "Add square function"
```

**Resultat:**
```
main:     A---B---C---D (alle feature commits squashed)
```

**Fordele:**
- ✅ Ren historie (én commit per feature)
- ✅ Lettere at revert

**Ulemper:**
- ⚠️ Mister detaljeret commit historie

### Strategy 3: Rebase

```bash
git checkout feature/add-square-function
git rebase main
git checkout main
git merge feature/add-square-function
```

**Resultat:**
```
main:     A---B---C---D (lineær historie)
```

**Fordele:**
- ✅ Helt lineær historie
- ✅ Ingen merge commits

**Ulemper:**
- ⚠️ Mere kompleks
- ⚠️ Kan være farligt hvis allerede pushed

**Anbefaling for begyndere: Brug standard merge!**

---

## 🐛 Fejlfinding

### Problem 1: Merge conflicts

**Symptom:**
```bash
git merge feature/my-feature
# CONFLICT (content): Merge conflict in calculator.py
# Automatic merge failed
```

**Løsning:**
```bash
# 1. Se hvilke filer har conflicts
git status

# 2. Åbn filen i VSCode
# Du vil se:
<<<<<<< HEAD
def add(self, a, b):
    return a + b
=======
def add(self, x, y):
    return x + y
>>>>>>> feature/my-feature

# 3. Redigér filen - vælg hvad du vil beholde
def add(self, a, b):
    return a + b

# 4. Gem filen

# 5. Mark som resolved
git add calculator.py

# 6. Færdiggør merge
git commit -m "Resolved merge conflict in calculator.py"
```

### Problem 2: Pushed til forkert branch

```bash
# Hvis du har pushed til main ved en fejl:

# 1. Se log
git log

# 2. Revert sidste commit
git revert HEAD

# 3. Push
git push origin main
```

### Problem 3: Vil fortryde lokale ændringer

```bash
# Kassér alle ændringer i working directory
git checkout .

# Eller specifik fil
git checkout -- calculator.py

# Kassér også staged ændringer
git reset --hard HEAD
```

### Problem 4: Branch er bagud

```bash
# Din feature branch er bagud i forhold til main

# 1. Skift til din branch
git checkout feature/my-feature

# 2. Hent seneste fra main
git pull origin main

# 3. Løs eventuelle conflicts

# 4. Push
git push origin feature/my-feature
```

### Problem 5: "Your branch is behind"

```bash
# Besked: Your branch is behind 'origin/main' by 3 commits

# Løsning:
git pull origin main
```

---

## ⭐ Best Practices

### 1. Små, fokuserede branches

**✅ GODT:**
```bash
feature/add-square-function      # Én funktion
fix/division-by-zero            # Ét problem
```

**❌ DÅRLIGT:**
```bash
feature/add-all-math-functions   # For meget på én gang
fix/everything                   # Ikke fokuseret
```

### 2. Commit ofte

```bash
# Flere små commits er bedre end én stor

git commit -m "Add square function"
git commit -m "Add tests for square function"
git commit -m "Update documentation"

# Ikke:
git commit -m "Did a lot of stuff"
```

### 3. Beskrivende commit beskeder

**✅ GODT:**
```bash
git commit -m "Fix division by zero error in divide method"
git commit -m "Add comprehensive tests for square function"
git commit -m "Refactor calculator class for better readability"
```

**❌ DÅRLIGT:**
```bash
git commit -m "fix"
git commit -m "update"
git commit -m "more changes"
git commit -m "asdf"
```

### 4. Pull før push

```bash
# Før du pusher, hent seneste ændringer:
git pull origin main
# Løs eventuelle conflicts
git push origin main
```

### 5. Beskyt main branch

**GitHub Settings → Branches → Branch protection rules:**
- ✅ Require pull request reviews
- ✅ Require status checks (tests må bestå)
- ✅ Ingen force push til main

### 6. Slet branches efter merge

```bash
# Lokalt
git branch -d feature/completed-feature

# Remote
git push origin --delete feature/completed-feature
```

---

## 📝 Cheat Sheet

### Daglig brug

```bash
# Se status
git status

# Se branches
git branch

# Lav ny branch
git checkout -b feature/new-thing

# Skift branch
git checkout main

# Tilføj ændringer
git add .

# Commit
git commit -m "Beskrivelse"

# Push
git push origin branch-navn

# Pull
git pull origin main

# Merge
git checkout main
git merge feature/my-feature

# Slet branch
git branch -d feature/old-feature
```

### Nyttige kommandoer

```bash
# Se log
git log --oneline

# Se ændringer
git diff

# Se hvem der ændrede hvad
git blame calculator.py

# Søg i commits
git log --grep="square"

# Se remote URLs
git remote -v

# Ryd op i branches
git fetch --prune
```

### Undo kommandoer

```bash
# Undo sidste commit (keep changes)
git reset --soft HEAD~1

# Undo sidste commit (discard changes)
git reset --hard HEAD~1

# Undo ændringer i fil
git checkout -- filename.py

# Undo staged changes
git reset HEAD filename.py

# Revert pushed commit
git revert HEAD
```

---

## 🎯 Komplet Workflow Eksempel

### Scenario: Tilføj modulo funktion

```bash
# DAG 1: Start feature
git checkout main
git pull origin main
git checkout -b feature/add-modulo
# [Lav ændringer i VSCode]
pytest tests/ -v
git add .
git commit -m "Add modulo function skeleton"
git push origin feature/add-modulo

# DAG 2: Tilføj tests
# [Lav tests]
pytest tests/ -v
git add tests/test_calculator.py
git commit -m "Add comprehensive tests for modulo"
git push origin feature/add-modulo

# DAG 3: Dokumentation
# [Opdater README]
git add README.md
git commit -m "Document modulo function usage"
git push origin feature/add-modulo

# DAG 4: Review og merge
# På GitHub: Lav Pull Request
# Review kode
# Se at tests er grønne ✅
# Merge PR

# Lokalt: Opdater main
git checkout main
git pull origin main
# Railway deployer automatisk! 🚀

# Cleanup
git branch -d feature/add-modulo
git push origin --delete feature/add-modulo
```

---

## 📚 Yderligere Ressourcer

**Visualisering:**
- https://git-school.github.io/visualizing-git/
- https://learngitbranching.js.org/

**Guides:**
- https://guides.github.com/
- https://www.atlassian.com/git/tutorials

**Interaktiv læring:**
- https://try.github.io/

---

## 🎓 Quiz: Test din forståelse

1. **Hvad gør `git checkout -b feature/new`?**
   - Laver og skifter til ny branch

2. **Hvornår deployer Railway?**
   - Når ændringer merges til main branch

3. **Hvad er forskellen på `git pull` og `git push`?**
   - pull = download fra GitHub
   - push = upload til GitHub

4. **Hvorfor bruge feature branches?**
   - Test nye features uden at påvirke main
   - Code review før merge
   - Hold main stable

5. **Hvad gør `git status`?**
   - Viser hvilke filer er ændret
   - Viser hvilken branch du er på
   - Viser hvad der skal committes

---

## ✅ Tjekliste for hver feature

```
[ ] Lav feature branch fra opdateret main
[ ] Lav ændringer
[ ] Test lokalt (pytest)
[ ] Commit med god besked
[ ] Push til GitHub
[ ] Se at GitHub Actions er grøn
[ ] Lav Pull Request
[ ] Review kode
[ ] Merge til main
[ ] Verificer deployment på Railway
[ ] Slet feature branch
[ ] Opdater lokal main
```

---

**God arbejdslyst med Git! 🚀**

*Husk: Commit tidligt, commit ofte, og lav små fokuserede ændringer!*
