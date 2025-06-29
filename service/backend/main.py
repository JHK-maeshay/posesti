from flask import Flask, send_from_directory, render_template
from routes import bp

app = Flask(__name__)
app.config.from_object('config.Config')
app.register_blueprint(bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)