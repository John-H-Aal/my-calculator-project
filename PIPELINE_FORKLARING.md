# 📊 CI/CD PIPELINE FORKLARING

## Hvad sker der når du pusher kode?

```
DU SKRIVER KODE I VSCODE
         ↓
    git push
         ↓
┌────────────────────────────────────────┐
│      GITHUB MODTAGER DIN KODE          │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│   PIPELINE STARTER AUTOMATISK! 🚀      │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│ STEP 1: Checkout kode                  │
│ → Henter din kode fra repository       │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│ STEP 2: Opsæt Python                   │
│ → Installerer Python 3.11              │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│ STEP 3: Installer dependencies         │
│ → pip install pytest osv.              │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│ STEP 4: KØR TESTS ✓                    │
│ → test_add()         ✅                │
│ → test_subtract()    ✅                │
│ → test_multiply()    ✅                │
│ → test_divide()      ✅                │
│ → test_divide_by_zero() ✅             │
└────────────────────────────────────────┘
         ↓
┌────────────────────────────────────────┐
│ STEP 5: Check kode kvalitet            │
│ → Leder efter fejl og problemer        │
└────────────────────────────────────────┘
         ↓
    ┌─────────┴─────────┐
    │                   │
    ↓                   ↓
┌─────────┐     ┌─────────────┐
│ SUCCESS │     │   FAILURE   │
│    ✅   │     │      ❌     │
└─────────┘     └─────────────┘
    │                   │
    ↓                   ↓
Grøn check        Rød X - se
på GitHub         fejllog!
```

## Hvad betyder det i praksis?

### ✅ Når alt går godt:
- Du ser en grøn check mark på GitHub
- Din kode er testet og valideret
- Trygt at merge til main branch
- Andre kan bruge din kode

### ❌ Når noget går galt:
- Du ser en rød X
- GitHub viser præcist hvilken test der fejlede
- Du kan klikke og se fejlloggen
- Ret fejlen og push igen

## Eksempel på fejllog

```
FAILED tests/test_calculator.py::test_add - AssertionError
Expected: 5
Got: 6

Din add() funktion returnerer forkert resultat!
```

## Tidsplan

```
0:00 - Du pusher kode
0:05 - Pipeline starter
0:30 - Dependencies installeret
1:00 - Tests køres
1:30 - Kvalitet check
2:00 - DONE! ✅ eller ❌
```

**Typisk total tid: 1-2 minutter**

## Real-world analogi

Forestil dig du baker en kage:

1. **Du baker kagen** (skriver kode)
2. **Leverer til kontrollen** (git push)
3. **Automatisk kvalitetskontrol:**
   - Vejer kagen ✓
   - Tjekker temperatur ✓
   - Smager den ✓
   - Tjekker konsistens ✓
4. **Resultat:**
   - ✅ Godkendt til salg (kan deployes)
   - ❌ Sendes tilbage (fix fejl)

Dette sker hver eneste gang, automatisk!

## Fordele

✅ **Fanger fejl tidligt** - Inden de når produktion
✅ **Konsistent kvalitet** - Samme tests hver gang
✅ **Tid sparet** - Automatisk, ikke manuelt
✅ **Tillid** - Ved at koden virker
✅ **Dokumentation** - Historie af alle tests

## Tips

💡 Tjek altid GitHub Actions efter push
💡 Test lokalt først (pytest)
💡 Læs fejlloggen omhyggeligt
💡 En fejl = mulighed for at lære!
