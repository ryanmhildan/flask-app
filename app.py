from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Halo, ini aplikasi Flask kamu di Render!"
