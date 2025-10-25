"""
Flask Web App - Calculator Demo
Simpel web interface til vores calculator
"""
from flask import Flask, render_template, request, jsonify
from my_calculator import Calculator

app = Flask(__name__)
calc = Calculator()


@app.route('/')
def home():
    """Hovedside med calculator interface"""
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    """API endpoint til at udføre beregninger"""
    try:
        data = request.get_json()
        operation = data.get('operation')
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        
        # Udfør beregning baseret på operation
        if operation == 'add':
            result = calc.add(a, b)
        elif operation == 'subtract':
            result = calc.subtract(a, b)
        elif operation == 'multiply':
            result = calc.multiply(a, b)
        elif operation == 'divide':
            result = calc.divide(a, b)
        else:
            return jsonify({'error': 'Ukendt operation'}), 400
        
        return jsonify({
            'result': result,
            'operation': operation,
            'a': a,
            'b': b
        })
    
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'Der skete en fejl'}), 500


@app.route('/health')
def health():
    """Health check endpoint til Railway"""
    return jsonify({'status': 'healthy', 'service': 'calculator-api'}), 200


if __name__ == '__main__':
    # Railway sætter PORT environment variable
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
