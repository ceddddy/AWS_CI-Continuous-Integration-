from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world!, This is a milestone numer one to be specific. One, two, one, two - this is a test for the CI/CD pipeline, focusing on the CI part.'

if __name__ == '__main__':
    app.run()

# The above is a simple python app that uses the Flask framework to create a web server that listens on port 5000 and returns a simple message when you visit the root URL.