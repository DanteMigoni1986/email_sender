import datetime
import smtplib
import ssl
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM


def email_func (subject, birthday_receiver, name):
    receiver = birthday_receiver
    sender = "dantemigoni@gmail.com"
    sender_passwd = "terekcqlwknqdahv"
    
    msg = MM()
    msg['Subject'] = subject +' '+str(name)+'!'
    
    HTML= """
    <html>
        <body>
            <h1>Feliz cumple campeon!</h1>
            <img src="https://live.staticflickr.com/7007/6658419953_35db7eedf1_b.jpg" alt ="Image" width="640" height="360"></img>
            <p>Photo by: Sugar Daze</p>
            <h2>
                <p>Hola,<br>
                Espero que tengas un grandioso dia! <br><br>
                De:<br>
                Dante Migoni
                </p>
            </h2>
        </body>
    </html>
    """
    
    MTObj = MT(HTML, "html")
    msg.attach(MTObj)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, sender_passwd)
    server.sendmail(sender, receiver, msg.as_string())

myFile = open('Emails.csv')
print("The content of CSV file is:")
text = myFile.readline()
while text != "":
    text = myFile.readline()
    text = text.rstrip()
    infoFields = text.split(',')
    if ( len(infoFields) == 4):
        email = infoFields[3]
        name = infoFields[0]
        email_func("Tu cumple", email, name)
        print("Email has been sent to: ", email)
myFile.close()