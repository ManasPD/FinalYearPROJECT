from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/profile/<usn>")
def profile(usn):
    return render_template('profile.html', name=usn)

if __name__ == "__main__":
    app.run()