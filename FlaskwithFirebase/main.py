from firebase import firebase
from flask import Flask, render_template
from form import FirePut
#from flask_wtf.csrf import CSRFProtect, CSRFError

app = Flask(__name__)
#csrf = CSRFProtect(app)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

firebase = firebase.FirebaseApplication('https://manas-53f1a.firebaseio.com/', None)

@app.route('/')
def index():
    return "<h1>Hello, world!</h1>"

@app.route('/testing')
def testing():
    return "<h1>This is another testing page</h1>"

count = 0

@app.route('/api/put', methods=['GET', 'POST'])
def fireput():
    form = FirePut()
    if form.validate_on_submit():
        global count
        count += 1
        putData = {'Title':form.title.data, 'Year':form.year.data, 'Rating':form.rating.data}
        firebase.put('/films','film' + str(count),putData)
        return render_template('api-put-result.html', form=form, putData=putData)
    return render_template('My-Form.html', form=form)

if __name__ =="__main__":
    app.run(debug=True)