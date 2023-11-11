from flask import Flask, render_template, request
from HillCipher import EncryptHC
import numpy as np 

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Choose your cipher'
    return render_template('index.html', title=title)

@app.route('/hillcipher')
def hillcipher():
    return render_template('hillcipher.html')

@app.route('/playfaircipher')
def playfaircipher():
    return render_template('playfaircipher.html')

@app.route('/process_hillcipherEN', methods=['POST'])
def process_hillcipherEN():
    user_message = request.form['message']
    user_key = request.form['key']
    rows = user_key.strip('{}').split('},{')
    user_key = [[int(e) for e in row.split(',')] for row in rows]
    user_mod = int(request.form['mod'])
    # Create an instance of EncryptHC
    cipher = EncryptHC(user_message, user_key, user_mod)
    # Encrypt the message
    ciphertext = cipher.encrypt(user_message)
    return render_template('hillcipher.html', ciphertext=ciphertext)

@app.route('/process_hillcipherDC', methods=['POST'])
def process_hillcipherDC():
    user_message = request.form['message']
    user_key = request.form['key']
    rows = user_key.strip('{}').split('},{')
    user_key = [[int(e) for e in row.split(',')] for row in rows]
    user_mod = int(request.form['mod'])
    # Create an instance of EncryptHC
    cipher = EncryptHC(user_message, user_key, user_mod)
    # Encrypt the message
    plaintext = cipher.decrypt(user_message)
    return render_template('hillcipher.html', plaintext=plaintext)

if __name__ == '__main__':
    app.run()
