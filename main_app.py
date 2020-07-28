# main app
from flask import Flask, jsonify, request, url_for, redirect, session

app = Flask(__name__)

app.config.update(
    TESTING=True,
    DEBUG=True,
    SECRET_KEY=b'_5#y234dasfgsd324535ghjgk32hrjhqgwf4123fgd4123t2374dsfgsdf2L"F4Q8z\n\xec]/'
)

@app.route('/')
def start():
    tekst = '''
    <h1> Aplikacja quizy szkolne </h1> <hr>
    Tu będzie Bootstrap zapewne ;-)
    '''
    return tekst

@app.route('/login')
def login():
    # tutaj trzeba logowanie jakieś sensowne dorobić...
    tekst = '''
    <h1> Aplikacja quizy szkolne </h1> <hr>
    Tu będzie logowanie zapewne ;-)
    '''
    return tekst



if __name__ == "__main__":
    app.run()
