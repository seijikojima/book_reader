from flask import *
from flask import render_template

# app = Flask(__name__)
app = Flask(__name__, static_folder='./')

@app.route("/")
def main_page():    
    return current_app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
