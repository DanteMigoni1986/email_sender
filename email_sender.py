import smtplib

sender_email = "dantemigoni@gmail.com"
rec_email = "dantemigoni@hotmail.com"
passwd = "terekcqlwknqdahv"
message = "Hola mundo desde python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, passwd)
print("Login success")

myFile = open('Emails.csv')
print("The content of CSV file is:")
text = myFile.readline()
while text != "":
    text = myFile.readline()
    text = text.rstrip()
    infoFields = text.split(',')
    if ( len(infoFields) == 4):
        email = infoFields[3]
        print(email)
        server.sendmail(sender_email, email, message)
        print("Email has been sent to: ", email)
myFile.close()