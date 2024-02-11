import smtplib
import getpass

smtp_object = smtplib.SMTP("smtp.gmail.com", 587)
smtp_object.starttls()

email = getpass.getpass("Enter Your Email: ")
password = getpass.getpass("Enter your Password")

print(smtp_object.login(email, password))

from_Email = ""
to_Email = ""

subject = input("Enter Your Email Subject: ")
message = """Hello,
Is everthing working fine? As this is my first mail by python.

Regards,
"""

msg = "Subject: " + subject + "\n" + message
print(smtp_object.sendmail(from_Email, to_Email, msg))

smtp_object.quit()
