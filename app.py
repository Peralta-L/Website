"""Main python File where it will
 assign the proper routes and pages"""
import os
import re
from passlib.hash import sha256_crypt
from datetime import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/password', methods=['GET', 'POST'])
def password():
    """route 1"""
    b = None
    if request.method == "POST":
        if request.form['button'] == 'YES':
            return redirect('/login')
            pass
        elif request.form['button'] == 'NO':
            return redirect('/register')
            pass
    return render_template('question.html', b=b)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        users = []
        file = open("info.txt", 'r')
        lines = file.readlines()
        file.close()
        for line in lines:
            username, passcode = line.strip().split()
            users.append({'user': username, 'password': passcode})
        u = request.form['name']
        code = request.form['passcode']
        for user in users:
            info1 = user['user']
            info2 = user['password']
            user_check = sha256_crypt.verify(u, info1)
            pass_check = sha256_crypt.verify(code, info2)
            if user_check and pass_check:
                return render_template('lab6.html', user_name=u)
            else:
                pass
        return render_template('login.html', wrong=False)
    else:
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        p = request.form['passcode']
        n = request.form['name']
        if complexity(p):
            hash_user = sha256_crypt.hash(n)
            hash_pass = sha256_crypt.hash(p)
            if not checks(n):
                with open("info.txt", 'a') as f:
                    f.write(f"{hash_user} {hash_pass}\n")
                    return redirect('/login')
            else:
                return render_template('register.html', notification=False,
                                       rules=complexity(p))
        else:
            return render_template('register.html', notification=True, rules=complexity(p))
    else:
        return render_template('register.html', notification=True, rules=True)


def complexity(p):
    rules = True
    if not re.search(r'[A-Z]', p):
        rules = False
    if not re.search(r'[a-z]', p):
        rules = False
    if not re.search(r'\d', p):
        rules = False
    if not re.search(r'[@!"§$%&/()=?*+|><]', p):
        rules = False
    return rules


def checks(n):
    match = False
    with open("info.txt", 'r') as f:
        repeats = f.readlines()
        for r in repeats:
            user, passcode = r.strip().split()
            match = sha256_crypt.verify(n, user)
            if match:
                return match
            break
    return match


@app.route('/')
def menu():
    return render_template('lab6.html')


@app.route('/Time')
def time():
    """route 2, gets time"""
    t = datetime.now()
    current_time = t.strftime("%H:%M:%S")
    return render_template('time.html', Time=current_time)


@app.route('/Date')
def date():
    """route 3 gets date"""
    d = datetime.now()
    current_date = d.strftime("%m/%d/%Y")
    return render_template('date.html', Date=current_date)


@app.route('/Poems')
def poems():
    """route 5, displays poems"""
    return render_template('poems.html')


if __name__ == '__main__':
    app.run()
