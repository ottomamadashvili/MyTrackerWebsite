import smtplib
import DTBS
#senderpython123@gmail.com Password
#recipientpython123@gmail.com Password

# just to use email and password without encryption
# you can search google: Less secure app access, and turn ON "Allow less secure apps" to use

def send_mail(body_one):
    server =  smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('senderpython123@gmail.com', 'sasatokakashi')
    subject = 'New listing has been added'
    body1 = DTBS.collections.find_one({"_id": body_one})





    msg = f"Subject: {subject}\n\n{body1}"

    server.sendmail(
        'senderpython123@gmail.com',
        'recipientpython123@gmail.com',
        msg.encode('utf8')
    )
    server.quit()


