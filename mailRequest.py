import mysql.connector
from datetime import datetime, timedelta
import smtplib


# Function sendMail
def sendMail(mailReceiver):
    sender = "concierge.expert.tedanvi@gmail.com"

    message = """From: Concierge Expert <concierge.expert.tedanvi@gmail.com>
To: <""" + str(mailReceiver) + """>
Subject: Fin d'abonnement

Bonjour,
    
Votre abonnement va bientot se terminer.
Si vous souhaitez vous reinscrire, il vous suffit de suivre ce lien : http://localhost/Concierge_Expert/website/html/subscription.php
    
Cordialement,
Concierge Expert

"""

    password = "kLKLxEe8M1EfOdvG"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")

    return


mydb = mysql.connector.connect(
    host='localhost',
    user="root",
    passwd="",
    database="concierge_expert"
)

myCursor = mydb.cursor()

myCursor.execute("SELECT idUser, dateStart FROM subscription")

results = myCursor.fetchall()

d = datetime.now().date()

for i in range(len(results)):
    d2 = results[i][1]
    oneYear = timedelta(days=365)
    d2 += oneYear
    d3 = d2 - d

    days = timedelta(days=14)

    if d3 <= days:
        print("Moins de 2 semaines")
        req = "SELECT mail FROM client WHERE id = " + str(results[i][0])
        myCursor.execute(req)
        receiver = myCursor.fetchone()
        sendMail(receiver[0])
    else:
        print("Personne n'a besoin de se réabonner")
