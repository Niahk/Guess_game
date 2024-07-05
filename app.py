from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xxxxxxxxxxxxxxx'

@app.route('/')
def index():
     session['number_to_guess'] = random.randint(1, 100)  # Generate a random number
     session['guesses'] = 0  
     return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
     guess = int(request.form['guess'])
     session['guesses'] += 1

     if guess == session['number_to_guess']:
        message = f"Congratulations! You guessed it right in {session['guesses']} guesses."
        return render_template('result.html', message=message)
     elif guess < session['number_to_guess']:
        message = "Too low. Try again!"
       
     else:
        message = "Too high. Try again!"
       

     return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)