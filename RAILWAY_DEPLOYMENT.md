# 🚀 Railway Deployment Guide

Komplet guide til at deploye din Calculator app til Railway med automatisk CI/CD.

## 📋 Indholdsfortegnelse

1. [Hvad er Railway?](#hvad-er-railway)
2. [Omkostninger](#omkostninger)
3. [Forberedelse](#forberedelse)
4. [Railway Setup](#railway-setup)
5. [GitHub Secrets](#github-secrets)
6. [Test Deployment](#test-deployment)
7. [Se din app live](#se-din-app-live)
8. [Fejlfinding](#fejlfinding)

---

## 🎯 Hvad er Railway?

Railway er en moderne hosting platform hvor du kan deploye apps gratis:

✅ **$5 gratis kredit/måned** (nok til små apps)
✅ **Automatisk deployment** fra GitHub
✅ **Gratis HTTPS** (sikker forbindelse)
✅ **Ingen kreditkort krævet** til at starte
✅ **Let at bruge** (ingen kompleks setup)

### Hvad kan vi deploye?
Vores Calculator bliver en **live web app** som:
- Kører 24/7 på internettet
- Har sin egen URL (f.eks. `my-calculator.up.railway.app`)
- Opdateres automatisk når du pusher kode til GitHub
- Kunden kan bruge direkte i browseren

---

## 💰 Omkostninger

### Gratis tier (hvad du får):
```
✅ $5 kredit per måned
✅ 512MB RAM
✅ 1GB disk plads  
✅ Shared CPU
✅ HTTPS inkluderet
✅ Automatisk deployments

Vores calculator bruger: ~$1-2/måned
Din pris: $0 (under gratis kredit)
```

### Hvis du overskrider $5:
```
Du betaler kun forskellen:
- Bruger $7 → betaler $2
- Bruger $4 → betaler $0

Du kan sætte spending limit på $5 så det stopper automatisk
```

### Sammenligning:
| Platform | Pris | Features |
|----------|------|----------|
| Railway | $0-5/måned | Fuld kontrol, ingen sleep |
| Render | $0 (med sleep) eller $7 | Går i sleep efter 15min |
| Heroku | $5+/måned | Ingen gratis tier længere |
| Fly.io | $0 | Gratis men mere kompleks |

**Railway vinder for begyndere! 🏆**

---

## 📦 Forberedelse

### Tjek at du har disse filer i dit projekt:

```
my-calculator-project/
├── app.py                     ✅ Flask web app (ny!)
├── templates/
│   └── index.html            ✅ Web interface (ny!)
├── my_calculator/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── .github/workflows/
│   └── ci-cd.yml             ✅ Opdateret med deploy
├── Procfile                   ✅ Railway config (ny!)
├── runtime.txt                ✅ Python version (ny!)
├── requirements.txt           ✅ Opdateret med Flask
└── setup.py
```

### Alle nye filer er inkluderet i zip'en! ✅

---

## 🚂 Railway Setup (Step-by-step)

### Step 1: Opret Railway konto (2 minutter)

1. Gå til **https://railway.app**
2. Klik **"Start a New Project"** eller **"Login"**
3. Vælg **"Login with GitHub"**
4. Godkend Railway adgang til din GitHub konto
5. ✅ Du er nu logget ind!

**Vigtigt:** Ingen kreditkort nødvendigt! 💳

### Step 2: Opret nyt projekt (1 minut)

1. På Railway dashboard, klik **"New Project"**
2. Vælg **"Deploy from GitHub repo"**
3. Vælg dit repository: **"my-calculator-project"**
4. Railway scanner dit projekt automatisk
5. Den finder `Procfile` og ved hvad den skal gøre
6. Klik **"Deploy"**

**Første deployment starter automatisk!** ⏳

### Step 3: Vent på første deployment (2-3 minutter)

Du vil se:
```
📦 Building...
   ├─ Installing Python 3.11
   ├─ Installing dependencies (requirements.txt)
   ├─ Building app
   └─ ✅ Build successful!

🚀 Deploying...
   ├─ Starting gunicorn
   ├─ App running on port 5000
   └─ ✅ Deployment successful!
```

### Step 4: Få din app URL

1. Klik på dit deployment
2. Gå til **"Settings"** tab
3. Under **"Domains"** klik **"Generate Domain"**
4. Railway giver dig en URL: `my-calculator-xxxxx.up.railway.app`
5. ✅ **Klik på linket - din app er live!** 🎉

---

## 🔐 GitHub Secrets Setup (Automatisk deployment)

Nu skal vi forbinde GitHub Actions med Railway så hver push deployer automatisk.

### Step 1: Få Railway API Token (1 minut)

1. I Railway, klik på din **profil** (top højre)
2. Klik **"Account Settings"**
3. Gå til **"Tokens"** tab
4. Klik **"Create Token"**
5. Giv den et navn: `GitHub Actions Deploy`
6. **KOPIER TOKEN NU!** (du ser den kun én gang) 📋
   ```
   Eksempel: railway_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

### Step 2: Tilføj token til GitHub (2 minutter)

1. Gå til din GitHub repository
2. Klik **"Settings"** (repository settings, ikke din profil)
3. I venstre menu, klik **"Secrets and variables"** → **"Actions"**
4. Klik **"New repository secret"**
5. Udfyld:
   - **Name:** `RAILWAY_TOKEN`
   - **Secret:** [indsæt din kopierede token]
6. Klik **"Add secret"**
7. ✅ Token er nu gemt sikkert!

**Vigtigt:** Secrets er:
- ✅ Krypteret i GitHub
- ✅ Kun synlig i workflow runs
- ✅ Aldrig synlig i logs eller kode
- ✅ Kan kun bruges af dine workflows

### Step 3: Verificer setup

Tjek at `.github/workflows/ci-cd.yml` har denne sektion:

```yaml
deploy:
  name: Deploy til Railway
  needs: test
  runs-on: ubuntu-latest
  if: github.ref == 'refs/heads/main' && github.event_name == 'push'
  
  steps:
  - name: Checkout kode
    uses: actions/checkout@v3
  
  - name: Deploy til Railway
    uses: bervProject/railway-deploy@main
    with:
      railway_token: ${{ secrets.RAILWAY_TOKEN }}
      service: my-calculator-app
```

**✅ Dette er allerede i din opdaterede workflow fil!**

---

## 🧪 Test Deployment

Nu skal vi teste at alt virker automatisk!

### Test 1: Lav en lille ændring

1. Åbn `templates/index.html` i VSCode
2. Find linjen med "🧮 Calculator"
3. Ændr til "🧮 Min Calculator" (eller noget andet)
4. Gem filen

### Test 2: Push til GitHub

```bash
git add .
git commit -m "Test: Opdateret titel"
git push origin main
```

### Test 3: Se CI/CD køre

1. Gå til GitHub repository
2. Klik **"Actions"** tab
3. Du vil se 2 jobs køre:
   ```
   ✅ Test og Build (30 sek)
   🚀 Deploy til Railway (1-2 min)
   ```

### Test 4: Verificer deployment

1. Gå til Railway dashboard
2. Under **"Deployments"** ser du ny deployment
3. Vent til den viser ✅
4. Refresh din app URL i browseren
5. **Du ser din ændring live!** 🎉

---

## 🌐 Se din app live

### Hvad kunden ser:

Din app URL (f.eks. `https://my-calculator-xxxxx.up.railway.app`) viser:

```
🧮 Calculator
Demonstrerer automatisk CI/CD deployment

[Input felt: Tal A]
[Input felt: Tal B]

[+ Plus]  [- Minus]
[× Gange] [÷ Divider]

🚀 Automatisk deployed via GitHub Actions
Hver push til main → Tests → Deploy til Railway
```

### Features:
✅ Fungerende calculator interface
✅ Realtime beregninger
✅ Flot design
✅ Mobil-venlig
✅ Automatisk HTTPS
✅ 24/7 tilgængelighed

### Del med andre:

```
Send linket til kolleger/kunder:
https://my-calculator-xxxxx.up.railway.app

De kan bruge den direkte i browseren!
Ingen installation nødvendig.
```

---

## 🎯 Fuld CI/CD workflow nu:

```
1. Du retter kode i VSCode
   ↓
2. git push origin main
   ↓
3. GitHub Actions starter automatisk
   ↓
4. Test Job (30 sek)
   ├─ Checkout kode
   ├─ Setup Python
   ├─ Install dependencies
   ├─ Run pytest
   └─ ✅ Tests bestået
   ↓
5. Deploy Job (1-2 min) - KUN hvis tests OK
   ├─ Checkout kode
   ├─ Railway deployment
   └─ ✅ Deployed
   ↓
6. Din app på Railway opdateres automatisk
   ↓
7. Kunden ser ændringen live!
```

**Total tid: Fra kode til live på 2-3 minutter! ⚡**

---

## 🔍 Overvågning og Logs

### Railway Dashboard:

**Deployments:**
- Se alle deployments
- Hvornår blev de deployed?
- Hvem deployed dem? (git commit info)

**Logs:**
```bash
# Realtime logs fra din app
2024-10-25 14:23:11 | Starting gunicorn
2024-10-25 14:23:12 | Listening on 0.0.0.0:5000
2024-10-25 14:23:45 | GET / - 200 OK
```

**Metrics:**
- CPU brug
- RAM brug
- Request count
- Response times

**Billing:**
- Hvor meget kredit har du brugt?
- Trend over måneden
- Estimeret måneds-kostnad

---

## 🐛 Fejlfinding

### Problem 1: Deployment fejler

**Symptom:** Railway viser "Build Failed" eller "Deploy Failed"

**Løsning:**
1. Klik på deployment for at se logs
2. Find fejlbeskeden
3. Almindelige problemer:
   ```
   ModuleNotFoundError: No module named 'flask'
   → Tjek requirements.txt har flask
   
   No Procfile found
   → Sørg for Procfile er i root directory
   
   Port binding error
   → Sørg app.py bruger os.environ.get('PORT')
   ```

### Problem 2: App starter men viser 502 fejl

**Løsning:**
```bash
# Tjek at Procfile er korrekt:
web: gunicorn app:app

# Tjek at app.py har:
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```

### Problem 3: GitHub Actions kan ikke deploye

**Symptom:** Deploy job fejler med authentication error

**Løsning:**
1. Tjek at `RAILWAY_TOKEN` secret eksisterer i GitHub
2. Gå til GitHub → Settings → Secrets → Actions
3. Tjek at navnet er præcis: `RAILWAY_TOKEN` (ikke railway_token)
4. Generer ny token på Railway hvis nødvendigt

### Problem 4: Tests bestod, men deploy job kørte ikke

**Løsning:**
```yaml
# Tjek workflow fil har:
deploy:
  needs: test  # Denne linje er vigtig!
  if: github.ref == 'refs/heads/main'
```

### Problem 5: App bruger for meget kredit

**Løsning:**
1. Railway dashboard → Project Settings
2. Set "Usage Limits"
3. Max budget: $5
4. Railway stopper automatisk hvis du når $5

---

## 💡 Pro Tips

### 1. Custom Domain
```
Du kan bruge dit eget domæne:
1. Railway → Settings → Domains
2. Add Custom Domain
3. Point din DNS til Railway
4. ✅ Gratis HTTPS automatisk!
```

### 2. Environment Variables
```
Tilføj hemmeligheder uden at committe dem:
1. Railway → Variables
2. Add Variable: DATABASE_URL, API_KEY, osv.
3. Tilgængelige i din app via os.environ
```

### 3. Multiple Environments
```
Lav separate Railway projekter:
- Production (main branch)
- Staging (develop branch)
- Testing (feature branches)
```

### 4. Database
```
Railway har gratis PostgreSQL:
1. New → Database → PostgreSQL
2. Railway giver dig connection string
3. Brug i din app
```

### 5. Monitoring
```
Setup notifikationer:
1. Railway → Integrations
2. Connect Slack/Discord
3. Få besked ved deployment/fejl
```

---

## 📊 Success Metrics

Efter setup kan du måle:

**Deployment Hastighed:**
```
Før: 30-60 min (manuel)
Nu:  2-3 min (automatisk)
Forbedring: 95% hurtigere
```

**Deployment Frekvens:**
```
Før: 1-2 gange om måneden
Nu:  10-20 gange om måneden
Forbedring: 10x flere releases
```

**Fejl i Produktion:**
```
Før: 8-12 bugs/måned
Nu:  1-2 bugs/måned
Forbedring: 85% færre bugs
```

**Kunde Tilfredshed:**
```
Hurtigere fixes
Hyppigere opdateringer
Mere stabil app
```

---

## 🎁 Bonus: Vis det til kunder

### Live Demo Script:

> "Lad mig vise jer hvordan CI/CD virker i praksis.
> 
> [Åbn app URL i browser]
> Her er vores calculator app - den kører live på Railway.
> 
> [Åbn VSCode]
> Nu ændrer jeg noget i koden... [lav en lille ændring]
> 
> [Terminal]
> Jeg pusher til GitHub... [git push]
> 
> [GitHub Actions]
> Se her - systemet tester automatisk og deployer...
> 
> [30 sekunder senere]
> Tests bestået! Nu deployer den...
> 
> [2 minutter senere]
> [Refresh browser]
> Og voila! Ændringen er live. Fra kode til produktion på 2 minutter.
> 
> Hele processen er automatisk - jeg skal ikke gøre noget manuelt."

**Kunden vil være imponeret! 🤩**

---

## 📝 Checkliste

Før du går live med kunder:

- [ ] Railway konto oprettet
- [ ] Første deployment successful
- [ ] App URL virker
- [ ] GitHub Secret konfigureret
- [ ] Automatisk deployment testet
- [ ] Logs tjekket for fejl
- [ ] Spending limit sat til $5
- [ ] Custom domain (optional)
- [ ] Monitoring setup (optional)
- [ ] Dokumentation opdateret

---

## 🚀 Næste Skridt

Nu hvor du har Railway setup:

1. **Test det grundigt** - lav flere pushes og se det virke
2. **Vis det til en kollega** - få feedback
3. **Optag en demo video** - brug til kunder
4. **Tilføj til din portfolio** - vis din CI/CD skills
5. **Brug det i rigtige projekter** - skalér til kunde apps

---

## 📚 Yderligere Ressourcer

**Railway Dokumentation:**
- https://docs.railway.app

**GitHub Actions:**
- https://docs.github.com/en/actions

**Flask Dokumentation:**
- https://flask.palletsprojects.com

**Gunicorn:**
- https://gunicorn.org

---

**Tillykke! Du har nu fuld CI/CD med automatisk deployment! 🎉**

*Fra kode til live produktion på 2 minutter - det er moderne software udvikling!*