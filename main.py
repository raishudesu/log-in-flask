from app import app
from flask import render_template, request, redirect, url_for
from flask.views import MethodView

class SubmitView(MethodView):
    def get(self):
        return redirect(url_for('home'))

    def post(self):
        email = request.form['email']
        password = request.form['password']
        print(email)
        print(password)
        if email == "admin@gmail.com" and password == "admin":
            print("ACCESS GRANTED")
            return redirect(url_for('home'))
        else:
            return 'ERROR'
        
app.add_url_rule('/submit', view_func=SubmitView.as_view('submit'))

@app.route('/')
def login():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()