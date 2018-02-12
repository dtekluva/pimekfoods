import smtplib

def send(name, text, phone, recipient):
    try:
        sender = 'notifywebmailer@gmail.com'
        receiver = recipient
        server  = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender, "mailerforweb")

        message = "Moremiutencils new message from \n"+"Name: "+ name+"\n\n "+"Phone: "+ phone+"\n\n "+text
        server.sendmail(sender, receiver, message)
        server.quit()

    except:
        print("Unable to send email due to network")