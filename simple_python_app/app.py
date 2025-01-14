from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'We are still winning in these tests'

if __name__ == '__main__':
    app.run()

# The above is a simple python app that uses the Flask framework to create a web server that listens on port 5000 and returns a simple message when you visit the root URL.