from flask import Flask, render_template, request
from db_connection import addCustomer
app = Flask(__name__)

#registration page
@app.route("/registration", methods=['GET','POST'])
def registration():
    return render_template('registration.html')

#contact page
@app.route("/contact")
def contact():
    return render_template('contact.html')

#about page
@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/header")
def header():
    return render_template('footer.html')

#index page
@app.route("/")
def index():
    return render_template('index.html')

#home page
@app.route("/home")
def home():
    return render_template('index.html')

#thank you
@app.route("/ThankYouPage")
def thankYou():
    return render_template('ThankYouPage.html')

#
@app.route("/add", methods = ['GET','POST'])
def add():
    if request.method == 'POST':
        fname = str(request.form['fname'])
        lname = str(request.form['lname'])
        email = str(request.form['email'])
        mo = str(request.form['mo'])
        number_plate = str(request.form['Vehicle_Number'])
        city = str(request.form['City'])
        land_mark = str(request.form['land_mark'])
        ty = str(request.form['Vehicle_Type'])

        added = addCustomer(fname,lname,email,mo,number_plate,city,land_mark,ty)
        print(fname,lname)
        if added == True:
            return render_template('ThankYouPage.html')
        else:
            return render_template('registration.html')
if __name__ == "__main__":
    app.run()
