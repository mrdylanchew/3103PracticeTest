from flask import Flask, render_template, request
import bleach

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    entered_password = request.form.get('password', '')
    
    # Pass the password to the template
    return render_template('welcome.html', password=entered_password)

@app.route('/result', methods=['POST'])
def result():
    search_term = request.form['search_term']

    if validate_input(search_term):
        sanitized_search_term = bleach.clean(search_term)
        return render_template('result.html', search_term=sanitized_search_term)
    else:
        # If XSS or SQL injection attempt is detected, clear the input and remain on the home page
        return render_template('home.html')

def validate_input(input_text):
    # Check for XSS and SQL injection patterns
    
    # Check for common XSS patterns
    xss_patterns = ['<script>', 'onmouseover', 'onerror', 'javascript:']
    
    for pattern in xss_patterns:
        if pattern.lower() in input_text.lower():
            return False

    # Check for common SQL injection patterns
    sql_injection_patterns = ['SELECT', 'UNION', 'FROM', 'WHERE', 'INSERT', 'DELETE', 'UPDATE']
    
    for pattern in sql_injection_patterns:
        if pattern.lower() in input_text.lower():
            return False
    
    return True

if __name__ == '__main__':
    app.run(debug=True)
