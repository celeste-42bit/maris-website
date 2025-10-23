from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This will look for templates/index.html
    return render_template('index.html')

if __name__ == '__main__':
    # Run on all interfaces, port 80, with debug mode on
    app.run(host='0.0.0.0', port=8080, debug=True)