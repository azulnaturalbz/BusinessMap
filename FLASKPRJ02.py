from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request
import html
import datetime
import dateparser
import json
import string
app = Flask(__name__)
DB = DBHelper()
categories = ['retail','restuarants','bars','fashion-beauty','hardware','autoparts','banks','technology',
              'telecom', 'pharmacy']


@app.route('/')
def home(error_message=None):
    #global businesses
    try:
        data = DB.get_all_inputs()
        businesses = DB.get_all_business()
        businesses = json.dumps(businesses)
    except Exception as e:
        print(e)
        data = None
    return render_template("home.html", data=data, businesses=businesses, categories=categories,
                           error_message=error_message)


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
        if category not in categories:
            return home()
        date=format_date(request.form.get('date'))
        if not date:
            return home("Invalid date please use correct format")
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
        description = html.escape(request.form.get('description'))
        #description = sanitized_string(request.form.get('description'))
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


def format_date(userdate):
    date = dateparser.parse(userdate)
    try:
        return datetime.datetime.strftime(date,"%Y-%m-%d")
    except TypeError:
        return None


def sanitized_string(userinput):
    whitelist = string.ascii_letters + " !?$.,;:-'()&"
    return filter(lambda x: x in whitelist, userinput)


if __name__ == '__main__':
    app.run()



