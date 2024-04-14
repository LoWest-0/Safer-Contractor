from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("MAIL_USERNAME")  
mail = Mail(app)

@app.route("/contact-thanks", methods=["POST"])
def contact_thanks():
    fname = request.form.get("first-name")
    lname = request.form.get("last-name")
    email = request.form.get('email')
    message = request.form.get('message')

    msg_title = "İletişim Formu Dolduruldu!"
    sender = app.config.get('MAIL_DEFAULT_SENDER')
    recipients = [app.config.get('MAIL_USERNAME')]  
    msg = Message(msg_title, sender=sender, recipients=recipients)
    msg_body = f"{fname} {lname},{email} Adresinden gelen mesaj: {message}"
    msg.html = msg_body

    try:
        mail.send(msg)
        return render_template("contact_thanks.html",username=fname+" "+lname)
    except Exception as e:
        print(e)
        return render_template("contact.html")

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def redirect_to_home():
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/policy')
def policy():
    return render_template('ourpolicy.html')

@app.route('/term-of-use')
def term_of_use():
    return render_template('term of use.html')


if __name__ == '__main__':
    app.run(debug=True)
