import smtplib
from email.message import EmailMessage
from fpdf import FPDF


def email_func (subject, message_receiver, name):
    receiver = message_receiver
    sender = "dantemigoni@gmail.com"
    sender_passwd = "terekcqlwknqdahv"
    
    msg = EmailMessage()
    msg['Subject'] = subject +' '+str(name)+'!'
    msg['From'] = 'Dante Migoni'
    msg['To'] = receiver
    
    with open('test.pdf', "rb") as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data, maintype = "application", subtype="pdf", filename= file_name)
        
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, sender_passwd)
    server.send_message(msg)
    
    
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
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)
        pdf.cell(200, 10, txt = name, ln = 1, align = 'C')
        pdf.cell(200, 10, txt = "Bienvenido al curso", ln = 2, align = 'C')
        pdf.output("test.pdf")
        email_func("Tu archivo", email, name)
        print("Email has been sent to: ", email)
myFile.close()