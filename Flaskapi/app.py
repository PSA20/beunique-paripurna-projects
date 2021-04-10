from flask import Flask,request,render_template,redirect,url_for
from mailjet_rest import Client
import os
api_key = 'ab7bf40ef737993df803847be1b37660'
api_secret = '19bed21a2c04bb0e3bb1d27878a04e84'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

@app.route('/submit',methods=['post'])
def submit():
    xt=[str(x) for x in request.form.values()]
    print(xt)
    data = {
        'Messages': [
        {
            "From": {
            "Email": "parthasai88@gmail.com",
            "Name": "Paripurna"
            },
            "To": [
            {
            "Email": xt[0],
            "Name": xt[1]
            }
            ],
            "Subject": "Greetings from Connections",
            "TextPart": "Your Result",
            "HTMLPart": '<h1 style=text-align:center;> <span style="background:#ff00ff;"">Your unique 390-degree Persona with your current vibes and your ultimate life purpose!</span> </h1><p style=text-align:center;>Your Ultimate Purpose Persona Epitome is </p> <p style=text-align:center;><mark>'+xt[2]+'</mark> </p> <p style=text-align:center;> And your Current Vibes are</p><p style=text-align:center;><mark>The Modification Expert/ The Accomplisher / The Intuitive</mark></p><p style=text-align:center;>Your Current Emotions and intellect quotient is</p><p style=text-align:center;><mark>ABC</mark></p><br><p style=text-align:center;>YOU ARE HERE TO </p> <p style=text-align:center;><mark>'+ xt[3] +'</mark></p><h2 style=text-align:center;>You are one of the unique combination and has excellent persona, but you need some alignment work done for that.Learn more on how to achieve your ultimate life purpose in detail and create your Magical Persona.</h2><p style=text-align:center;>&#10070; What is your Epitome </p><p style=text-align:center;> &#10070; How to walk on your purpose Epitome </p><p style=text-align:center;>&#10070; How you can overcome the major emotional and intellectual obstacles those you are reflecting strongly</p><p style=text-align:center;>&#10070; The ultimate way to head towards Purpose </p><p style=text-align:center;>&#10070; How you can discover your Ultimate Purpose by 7 step-by-step formula</p><p style=text-align:center;>&#10070; How you can make work your chakra and Kosha for your Purpose</p><p style=text-align:center;>&#10070; How to overcome- over-whelming</p><p style=text-align:center;>&#10070; How you can select or fix your purpose </p><br><br><br><div style=text-align:center;>I am ready to discover my Ultimate Life Purpose with you</div><h1 style=text-align:center;><span style="background:#ff00ff;">Book your session now by sending email on fulfil@paripurnalife.com</span></h1><h2 style=text-align:center;>What session will Have</h2><p style=text-align:center;>1.Free your limitations technique </p><p style=text-align:center;> 2.Verbalization</p><p style=text-align:center;> 3.Visualization </p><p style=text-align:center;>4.Body Energizations </p><p style=text-align:center;> 5.Find your Purpose Epitome</p><p style=text-align:center;> 6.Blueprint of Your Ultimate Purpose </p><p style=text-align:center;> 7.Balance your Emotional and Intelligent quotient </p>',
            "CustomID": "AppGettingStartedTest"
        }
        ]
    }
    result = mailjet.send.create(data=data)
    return 'Thank you for taking quiz... Please check your mail'

if __name__ == '__main__':
    app.run()