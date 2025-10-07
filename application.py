from flask import Flask

application = Flask(__name__)

@app.route('/')
def hello():
    return 'Hi!'

if __name__ == '__main__':
    application.run(debug=True)
