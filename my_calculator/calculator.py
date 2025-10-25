"""
En simpel calculator klasse til at demonstrere CI/CD
"""

class Calculator:
    """En simpel lommeregner"""
    
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
