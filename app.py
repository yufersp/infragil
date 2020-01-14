#/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home ():
        return 'Showzin!'

app.run(host='0.0.0.0', port=808, debug=True)
# Comentario
