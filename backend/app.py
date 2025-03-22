from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from service import search_word

app = Flask(__name__, template_folder='../templates', static_folder='../static')


USERNAME = 'admin'
PASSWORD = 'password123'

dictionary_data = {}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('main'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            return redirect(url_for('main'))
        else:
            return render_template('login.html', error="Invalid username or password.")
    return render_template('login.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        word = request.form.get('word', '').strip().lower()
        result = search_word(word)

        if result['type'] == 'exact':
            return render_template('main.html', result=result['result'], username=session['username'])
        elif result['type'] == 'suggestion':
            suggestions = ", ".join(result['suggestions'])
            return render_template('main.html', suggestions=suggestions, username=session['username'])
        else:
            return render_template('main.html', result=result['result'], username=session['username'])
    
    return render_template('main.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
