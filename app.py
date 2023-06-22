from flask import Flask,render_template,request
from email.message import EmailMessage
import ssl
import smtplib

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    result=''
    if(request.method=="POST"):
        try:
            user_email=request.form.get('email')
            amt=int(request.form.get('amt'))
            sub=request.form.get('subject')
            bdy=request.form.get('message')
            for i in range(amt):
                print("Sending",i+1)
                send_email(user_email,sub,bdy)
            result='Your mail have been sent sucessfully !!'
            request.method="";
            return render_template('index.html',result=result)
            
        except:
            result='Error Occured !!'
            return render_template('index.html',result=result)
        
        
    return render_template('index.html',result=result)

def send_email(receiver_email,subject,body):
    
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "prathamkolar2511@gmail.com"
    password ='asjrjsbenvfsesdl'

    em=EmailMessage()
    em['From']=sender_email
    em['To']=receiver_email
    em['subject']=subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email,password)
        server.sendmail(sender_email, receiver_email,em.as_string())
        server.quit()



if __name__ == '__main__':
   app.run()