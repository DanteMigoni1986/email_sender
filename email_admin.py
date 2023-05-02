import datetime
import smtplib
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM
from email.message import EmailMessage
from fpdf import FPDF


class EmailSender():
    def __init__(self):
        self.sender_email = "dantemigoni@gmail.com"
        self.rec_email = "dantemigoni@hotmail.com"
        self.passwd = "terekcqlwknqdahv"
        self.plainTextMessage = "Hola mundo desde python"
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(self.sender_email, self.passwd)
        
    def sendHappyBirthdayEmail(self, subject, birthday_receiver, name):
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
        self.server.sendmail(self.sender_email, birthday_receiver, msg.as_string())
        
        
    def sendEmailWithPDF(self, subject, messageReceiver, name):
        msg = EmailMessage()
        msg['Subject'] = subject +' '+str(name)+'!'
        msg['From'] = 'Dante Migoni'
        msg['To'] = messageReceiver
        
        with open('test.pdf', "rb") as f:
            file_data = f.read()
            file_name = f.name
            msg.add_attachment(file_data, maintype = "application", subtype="pdf", filename= file_name)
            self.server.send_message(msg)
            
    def sendEmails(self, mode):
        myFile = open('Emails.csv')
        text = myFile.readline()
        
        while text != "":
            text = myFile.readline()
            text = text.rstrip()
            infoFields = text.split(',')
            if ( len(infoFields) == 4):
                email = infoFields[3]
                name = infoFields[0]
                print(email)
                if mode == "birthday":
                    self.sendHappyBirthdayEmail("Tu cumple", email, name)
                elif mode == "plainText":
                    self.server.sendmail(self.sender_email, email, self.plainTextMessage)
                elif mode == "pdf":
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size = 15)
                    pdf.cell(200, 10, txt = name, ln = 1, align = 'C')
                    pdf.cell(200, 10, txt = "Bienvenido al curso", ln = 2, align = 'C')
                    pdf.output("test.pdf")
                    self.sendEmailWithPDF("Tu archivo",email, name)
                    
                print("Email has been sent to: ", email)
        myFile.close()
        
       
if __name__ == '__main__':  
    emailSender = EmailSender()
    emailSender.sendEmails(mode="plainText")
    emailSender.sendEmails(mode="birthday")
    emailSender.sendEmails(mode="pdf")