# 🌐 Flask Client-Server Arkitektur Forklaring

Komplet guide til hvordan din Calculator app fungerer som en rigtig web applikation med frontend, backend og API.

## 📋 Indholdsfortegnelse

1. [Hvad er Client-Server?](#hvad-er-client-server)
2. [Arkitektur Oversigt](#arkitektur-oversigt)
3. [Dataflow](#dataflow)
4. [Kode Gennemgang](#kode-gennemgang)
5. [API Endpoints](#api-endpoints)
6. [Request/Response Cyklus](#requestresponse-cyklus)
7. [Hvorfor denne arkitektur?](#hvorfor-denne-arkitektur)
8. [Alternativer](#alternativer)
9. [Udvid arkitekturen](#udvid-arkitekturen)

---

## 🎯 Hvad er Client-Server?

### Simpel forklaring:

**Client (Klient):**
- Din browser (Chrome, Firefox, Safari)
- Det du ser og interagerer med
- Sender requests og viser resultater

**Server:**
- Computer der kører din Python kode
- Modtager requests fra clients
- Udfører beregninger og sender resultater tilbage

**API (Application Programming Interface):**
- Måden client og server taler sammen
- Definerer hvilke requests server accepterer
- I vores projekt: HTTP endpoints som `/calculate`

### Analogi:

```
Restaurant analogi:

Client (Browser)     = Gæst der bestiller
API (/calculate)     = Menu med muligheder
Server (Flask)       = Tjener der tager imod
Backend Logic        = Køkken der laver mad
Response             = Mad der serveres
```

---

## 🏗️ Arkitektur Oversigt

### 3-Tier Arkitektur

```
┌─────────────────────────────────────────────────────┐
│                 TIER 1: FRONTEND                    │
│                  (Presentation)                     │
├─────────────────────────────────────────────────────┤
│  📱 Browser / Client                                │
│  ├── HTML (templates/index.html)                    │
│  │   └── Layout og struktur                         │
│  ├── CSS (i <style> tags)                          │
│  │   └── Design og farver                           │
│  └── JavaScript (i <script> tags)                  │
│      └── Bruger interaktion                         │
│      └── Sender API requests                        │
│      └── Viser resultater                           │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ HTTP Request
                   │ POST /calculate
                   │ Content-Type: application/json
                   │ Body: {"operation": "add", "a": 10, "b": 5}
                   │
                   ↓
┌─────────────────────────────────────────────────────┐
│                 TIER 2: BACKEND                     │
│              (Application Logic)                    │
├─────────────────────────────────────────────────────┤
│  🐍 Flask Server (app.py)                           │
│  ├── Modtager HTTP requests                         │
│  ├── Parser JSON data                               │
│  ├── Validerer input                                │
│  ├── Router til korrekt handler                     │
│  └── Sender JSON response tilbage                   │
└──────────────────┬──────────────────────────────────┘
                   │
                   │ Function Call
                   │ calc.add(10, 5)
                   │
                   ↓
┌─────────────────────────────────────────────────────┐
│                TIER 3: BUSINESS LOGIC               │
│                  (Domain Logic)                     │
├─────────────────────────────────────────────────────┤
│  🧮 Calculator Class (my_calculator/calculator.py)  │
│  ├── add(a, b) → a + b                             │
│  ├── subtract(a, b) → a - b                        │
│  ├── multiply(a, b) → a * b                        │
│  └── divide(a, b) → a / b                          │
│                                                     │
│  ✅ DETTE TESTES AF PYTEST                          │
└─────────────────────────────────────────────────────┘
```

---

## 🔄 Dataflow: Fra klik til resultat

### Komplet Request/Response Cyklus

```
1. BRUGER HANDLING
   └─ Bruger taster: A=10, B=5
   └─ Klikker på "Plus" knap

2. JAVASCRIPT AKTIVERES
   └─ Event listener fanger klik
   └─ Læser værdier fra input felter
   └─ Opretter JSON objekt

3. HTTP REQUEST SENDES
   └─ Method: POST
   └─ URL: https://your-app.railway.app/calculate
   └─ Headers: Content-Type: application/json
   └─ Body: {"operation": "add", "a": 10, "b": 5}

4. FLASK MODTAGER
   └─ Route: @app.route('/calculate', methods=['POST'])
   └─ Parser JSON: request.get_json()
   └─ Validerer data typer

5. PYTHON BEREGNER
   └─ Kalder: calc.add(10, 5)
   └─ Calculator.add() kører: return 10 + 5
   └─ Resultat: 15

6. FLASK SVARER
   └─ Opretter JSON: {"result": 15, "operation": "add", ...}
   └─ Status: 200 OK
   └─ Sender response

7. JAVASCRIPT MODTAGER
   └─ Parser JSON response
   └─ Opdaterer DOM
   └─ Viser: "10 + 5 = 15"

8. BRUGER SER RESULTAT
   └─ Resultat vises på skærmen
   └─ Total tid: ~50-200ms
```

---

## 💻 Kode Gennemgang

### Frontend: `templates/index.html`

#### HTML Struktur

```html
<!-- Input felter hvor bruger taster tal -->
<input type="number" id="numA" value="10">
<input type="number" id="numB" value="5">

<!-- Knapper til operationer -->
<button class="op-btn" onclick="calculate('add')">➕ Plus</button>
<button class="op-btn" onclick="calculate('subtract')">➖ Minus</button>
<button class="op-btn" onclick="calculate('multiply')">✖️ Gange</button>
<button class="op-btn" onclick="calculate('divide')">➗ Divider</button>

<!-- Område hvor resultat vises -->
<div id="result">
    <div class="result-value"><!-- Resultat kommer her --></div>
</div>
```

#### JavaScript - API Kald

```javascript
async function calculate(operation) {
    // 1. Læs værdier fra input felter
    const a = parseFloat(document.getElementById('numA').value);
    const b = parseFloat(document.getElementById('numB').value);
    
    // 2. Send HTTP POST request til Flask server
    const response = await fetch('/calculate', {
        method: 'POST',                           // HTTP method
        headers: {
            'Content-Type': 'application/json',   // Vi sender JSON
        },
        body: JSON.stringify({                    // Convert til JSON string
            operation: operation,                 // "add", "subtract", etc.
            a: a,                                // Første tal
            b: b                                 // Andet tal
        })
    });
    
    // 3. Parser JSON response fra server
    const data = await response.json();
    
    // 4. Vis resultat på skærmen
    if (response.ok) {
        document.getElementById('result').innerHTML = `
            <div class="result-value">${data.result}</div>
        `;
    } else {
        // Vis fejl hvis noget gik galt
        document.getElementById('result').innerHTML = `
            <div class="error">${data.error}</div>
        `;
    }
}
```

### Backend: `app.py`

#### Flask App Setup

```python
from flask import Flask, render_template, request, jsonify
from my_calculator import Calculator

# Opret Flask applikation
app = Flask(__name__)

# Opret Calculator instans (bruges til alle requests)
calc = Calculator()
```

#### Route: Serve Frontend

```python
@app.route('/')
def home():
    """
    Hovedside - sender HTML til browser
    Når bruger går til https://your-app.railway.app/
    """
    return render_template('index.html')
```

#### Route: API Endpoint

```python
@app.route('/calculate', methods=['POST'])
def calculate():
    """
    API endpoint - modtager beregnings requests
    URL: /calculate
    Method: POST
    Content-Type: application/json
    Body: {"operation": "add", "a": 10, "b": 5}
    """
    try:
        # 1. Hent JSON data fra request
        data = request.get_json()
        
        # 2. Extract værdier
        operation = data.get('operation')  # "add", "subtract", etc.
        a = float(data.get('a', 0))       # Første tal (default 0)
        b = float(data.get('b', 0))       # Andet tal (default 0)
        
        # 3. Udfør beregning baseret på operation
        if operation == 'add':
            result = calc.add(a, b)        # Kalder Calculator.add()
        elif operation == 'subtract':
            result = calc.subtract(a, b)
        elif operation == 'multiply':
            result = calc.multiply(a, b)
        elif operation == 'divide':
            result = calc.divide(a, b)
        else:
            # Ukendt operation
            return jsonify({'error': 'Ukendt operation'}), 400
        
        # 4. Send resultat tilbage som JSON
        return jsonify({
            'result': result,
            'operation': operation,
            'a': a,
            'b': b
        })
    
    except ValueError as e:
        # Håndter fejl (f.eks. division by zero)
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Generisk fejl
        return jsonify({'error': 'Der skete en fejl'}), 500
```

#### Health Check Endpoint

```python
@app.route('/health')
def health():
    """
    Health check - Railway bruger dette til at tjekke om app'en kører
    """
    return jsonify({'status': 'healthy', 'service': 'calculator-api'}), 200
```

#### Start Server

```python
if __name__ == '__main__':
    import os
    # Railway sætter PORT environment variable
    port = int(os.environ.get('PORT', 5000))
    # Start Flask server
    app.run(host='0.0.0.0', port=port, debug=False)
```

### Business Logic: `my_calculator/calculator.py`

```python
class Calculator:
    """
    Calculator klasse - indeholder al beregnings logik
    Denne kode testes af pytest!
    """
    
    def add(self, a, b):
        """Læg to tal sammen"""
        return a + b
    
    def subtract(self, a, b):
        """Træk b fra a"""
        return a - b
    
    def multiply(self, a, b):
        """Gang to tal sammen"""
        return a * b
    
    def divide(self, a, b):
        """Divider a med b"""
        if b == 0:
            raise ValueError("Kan ikke dividere med nul!")
        return a / b
```

**Hvorfor separat klasse?**
- ✅ Kan testes uafhængigt
- ✅ Genbrugelig (kunne bruges af andre apps)
- ✅ Nem at udvide med ny funktionalitet
- ✅ Separation of concerns

---

## 📡 API Endpoints

### Oversigt

| Endpoint | Method | Formål | Input | Output |
|----------|--------|--------|-------|--------|
| `/` | GET | Serve HTML | - | HTML side |
| `/calculate` | POST | Beregn | JSON | JSON resultat |
| `/health` | GET | Health check | - | Status |

### Endpoint: `/calculate` Detaljer

**Request:**
```http
POST /calculate HTTP/1.1
Host: your-app.railway.app
Content-Type: application/json

{
    "operation": "add",
    "a": 10,
    "b": 5
}
```

**Response (Success):**
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "result": 15,
    "operation": "add",
    "a": 10,
    "b": 5
}
```

**Response (Error):**
```http
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
    "error": "Kan ikke dividere med nul!"
}
```

### Test API med curl

```bash
# Test add operation
curl -X POST https://your-app.railway.app/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "add", "a": 10, "b": 5}'

# Response: {"result": 15, "operation": "add", "a": 10, "b": 5}

# Test division by zero
curl -X POST https://your-app.railway.app/calculate \
  -H "Content-Type: application/json" \
  -d '{"operation": "divide", "a": 10, "b": 0}'

# Response: {"error": "Kan ikke dividere med nul!"}

# Test health check
curl https://your-app.railway.app/health

# Response: {"status": "healthy", "service": "calculator-api"}
```

---

## 🔄 Request/Response Cyklus Detaljeret

### 1. Browser sender request

```javascript
// Browser JavaScript
fetch('/calculate', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({operation: 'add', a: 10, b: 5})
})
```

↓ **Konverteres til HTTP request:**

```http
POST /calculate HTTP/1.1
Host: my-calculator-production.up.railway.app
Content-Type: application/json
Content-Length: 45

{"operation":"add","a":10,"b":5}
```

### 2. Railway router modtager

```
Internet → Railway Load Balancer → Din Flask App
```

### 3. Flask modtager og parser

```python
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()  # {"operation": "add", "a": 10, "b": 5}
    # ... processing ...
```

### 4. Calculator udfører

```python
calc.add(10, 5)  # Returns: 15
```

### 5. Flask sender response

```python
return jsonify({'result': 15, 'operation': 'add', 'a': 10, 'b': 5})
```

↓ **Konverteres til HTTP response:**

```http
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 52

{"result":15,"operation":"add","a":10,"b":5}
```

### 6. Browser modtager og viser

```javascript
const data = await response.json();  // {result: 15, ...}
document.getElementById('result').textContent = data.result;  // Viser "15"
```

**Total tid: ~50-200ms** ⚡

---

## 🤔 Hvorfor denne arkitektur?

### ✅ Fordele

**1. Separation of Concerns**
```
HTML/CSS/JS  →  Kun præsentation
Flask        →  Kun routing og validering
Calculator   →  Kun beregninger
```

**2. Testbar kode**
```python
# Du kan teste Calculator klassen direkte
def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5  # ✅
```

**3. Skalerbarhed**
```
En server kan håndtere tusindvis af clients
Load balancing mulig
Kan deploye flere instanser
```

**4. Sikkerhed**
```python
# Backend validerer ALT input
if not isinstance(a, (int, float)):
    return error("Invalid input")

# Client kan ikke manipulere beregninger
# Kun backend har kontrol
```

**5. Flere klienter**
```
Browser Web App    ──┐
Mobile App (iOS)   ──┼──→  Flask API  →  Calculator
Mobile App (Android)─┤
Desktop App        ──┘
```

**6. Vedligehold**
```
Ændre UI:        Kun HTML/CSS/JS
Ændre logik:     Kun Calculator.py
Tilføj endpoint: Kun app.py
```

### ⚠️ Ulemper (trade-offs)

**1. Mere kompleks**
- Flere moving parts
- Skal forstå HTTP
- Async JavaScript nødvendig

**2. Netværks latency**
- 50-200ms delay per request
- Vs. 0ms for local JavaScript

**3. Server omkostninger**
- Skal hoste backend
- Koster penge (dog billigt)

**4. Single Point of Failure**
- Hvis server går ned, virker intet
- Mere kompleks deployment

---

## 🔄 Alternativer

### Alternative 1: Alt i JavaScript (Client-side only)

```html
<script>
function calculate(operation) {
    const a = parseFloat(document.getElementById('numA').value);
    const b = parseFloat(document.getElementById('numB').value);
    
    let result;
    if (operation === 'add') {
        result = a + b;  // ← Beregning direkte i browser
    }
    
    document.getElementById('result').textContent = result;
}
</script>
```

**Fordele:**
- ✅ Meget simpelt
- ✅ Ingen server omkostninger
- ✅ Instant respons (ingen netværk)

**Ulemper:**
- ❌ Ingen backend logik
- ❌ Kan ikke gemme data
- ❌ Ingen sikkerhed
- ❌ Python tests er irrelevante
- ❌ Ikke skalerbart til kompleks logik

**Hvornår bruge:** Simple calculators, static sites

### Alternative 2: Server-Side Rendering (SSR)

```python
@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form.get('a'))
    b = float(request.form.get('b'))
    result = calc.add(a, b)
    
    # Render helt ny HTML side
    return render_template('result.html', result=result)
```

**Fordele:**
- ✅ Simpel (ingen JavaScript nødvendig)
- ✅ SEO venlig

**Ulemper:**
- ❌ Fuld page reload
- ❌ Langsommere user experience
- ❌ Ikke moderne

**Hvornår bruge:** Traditionelle web apps, blogs

### Alternative 3: GraphQL API

```python
type Query {
    calculate(operation: String!, a: Float!, b: Float!): Float!
}
```

**Fordele:**
- ✅ Meget fleksibel
- ✅ Kun hent præcis det du behøver

**Ulemper:**
- ❌ Mere kompleks
- ❌ Overkill for simple apps

**Hvornår bruge:** Store apps med mange data typer

### Alternative 4: WebSockets (Real-time)

```python
@socketio.on('calculate')
def handle_calculate(data):
    result = calc.add(data['a'], data['b'])
    emit('result', {'result': result})
```

**Fordele:**
- ✅ Real-time bidirectional
- ✅ Perfekt til chat, live data

**Ulemper:**
- ❌ Mere kompleks
- ❌ Overkill for simple requests

**Hvornår bruge:** Chat apps, live dashboards, multiplayer games

---

## 🚀 Udvid arkitekturen

### 1. Tilføj Database

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String(20))
    a = db.Column(db.Float)
    b = db.Column(db.Float)
    result = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

@app.route('/calculate', methods=['POST'])
def calculate():
    # ... beregn result ...
    
    # Gem i database
    calc_record = Calculation(
        operation=operation,
        a=a, b=b, result=result,
        timestamp=datetime.now()
    )
    db.session.add(calc_record)
    db.session.commit()
    
    return jsonify({'result': result})

@app.route('/history')
def history():
    """Vis de sidste 10 beregninger"""
    calcs = Calculation.query.order_by(
        Calculation.timestamp.desc()
    ).limit(10).all()
    
    return jsonify([{
        'operation': c.operation,
        'a': c.a, 'b': c.b,
        'result': c.result,
        'time': c.timestamp
    } for c in calcs])
```

### 2. Tilføj Authentication

```python
from flask_login import login_required, current_user

@app.route('/calculate', methods=['POST'])
@login_required  # Kun logged in users
def calculate():
    # ... beregn result ...
    
    # Log hvem der beregnede
    log_calculation(current_user.id, operation, result)
    
    return jsonify({'result': result})
```

### 3. Tilføj Rate Limiting

```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/calculate', methods=['POST'])
@limiter.limit("100 per hour")  # Max 100 requests per time
def calculate():
    # ...
```

### 4. Tilføj Caching

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/calculate', methods=['POST'])
@cache.memoize(timeout=300)  # Cache i 5 minutter
def calculate():
    # ... expensive calculation ...
```

### 5. Tilføj Validation

```python
from marshmallow import Schema, fields, ValidationError

class CalculateSchema(Schema):
    operation = fields.Str(required=True)
    a = fields.Float(required=True)
    b = fields.Float(required=True)

schema = CalculateSchema()

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = schema.load(request.get_json())
    except ValidationError as e:
        return jsonify({'errors': e.messages}), 400
    
    # Nu ved vi data er valid!
```

### 6. Tilføj Logging

```python
import logging

logger = logging.getLogger(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    logger.info(f"Calculation request: {operation} {a} {b}")
    
    result = calc.add(a, b)
    
    logger.info(f"Result: {result}")
    
    return jsonify({'result': result})
```

### 7. Tilføj Multiple Operations Endpoint

```python
@app.route('/batch-calculate', methods=['POST'])
def batch_calculate():
    """
    Udfør flere beregninger på én gang
    Input: {"operations": [
        {"op": "add", "a": 1, "b": 2},
        {"op": "multiply", "a": 3, "b": 4}
    ]}
    """
    operations = request.get_json()['operations']
    results = []
    
    for op in operations:
        if op['op'] == 'add':
            result = calc.add(op['a'], op['b'])
        # ... andre operations ...
        
        results.append(result)
    
    return jsonify({'results': results})
```

---

## 🎓 Læringsmål

Efter at have læst denne guide, skulle du forstå:

✅ **Hvad er client-server arkitektur**
- Browser (client) sender requests
- Flask (server) modtager og beregner
- Response sendes tilbage

✅ **Hvordan HTTP requests fungerer**
- POST /calculate med JSON body
- Server parser og processerer
- JSON response sendes tilbage

✅ **Hvorfor separere frontend og backend**
- Testbar kode
- Skalerbar arkitektur
- Sikkerhed

✅ **Hvordan Flask routes fungerer**
- @app.route() decorator
- HTTP methods (GET, POST)
- Request/response handling

✅ **Hvordan dit projekt hænger sammen**
- HTML → JavaScript → Flask → Calculator → Flask → JavaScript → HTML
- Hver del har sin rolle
- Tests tester faktisk koden der bruges

---

## 📝 Opsummering

### Din Calculator App er:

**🎨 Frontend (Client):**
- HTML for struktur
- CSS for design
- JavaScript for interaktion
- Sender API requests

**🐍 Backend (Server):**
- Flask for routing
- API endpoints
- Validering
- Error handling

**🧮 Business Logic:**
- Calculator klasse
- Ren Python
- Testbar med pytest
- Genbrugelig

### Dataflow:

```
Bruger → JavaScript → HTTP Request → Flask → Calculator → Flask → HTTP Response → JavaScript → Bruger
```

### Hvorfor det er smart:

- ✅ Professionel arkitektur
- ✅ Testbar kode
- ✅ Skalerbar
- ✅ Sikker
- ✅ Vedligeholdbar
- ✅ Kan udvides

---

**Nu forstår du hvordan moderne web applikationer fungerer! 🎉**

*Dette er den samme arkitektur som bruges af Facebook, Twitter, Netflix og alle andre moderne web apps - bare i miniature!*
