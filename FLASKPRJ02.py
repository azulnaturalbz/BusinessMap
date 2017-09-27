from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
DB = DBHelper()


@app.route('/')
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as e:
        print(e)
        data = None
    return render_template("home.html", data=data)


@app.route('/add', methods=['POST'])
def add():
    try:
        data = request.form.get('userinput')
        DB.add_input(data)
    except Exception as e:
        print(e)
    return home()


@app.route('/submitbusiness', methods=['POST'])
def submitbusiness():
    try:
        bizname = request.form.get('bizname')
        bizaddr = request.form.get('bizaddr')
        usrtel = request.form.get('usrtel')
        email = request.form.get('email')
        homepage = request.form.get('homepage')
        category = request.form.get('category')
        date = request.form.get('date')
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
        description = request.form.get('description')
        DB.add_business(bizname, bizaddr, usrtel, email, homepage, category, date, latitude, longitude, description)
        return home()
    except Exception as e:
        print(e)
    return home()


@app.route('/clear')
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print(e)
    return home()


if __name__ == '__main__':
    app.run()



