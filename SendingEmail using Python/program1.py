import smtplib
from email.mime.text import MIMEText

HOST = "smtp.outlook.com"
PORT = 587

FROM_MAIL = "umairniaziofficial@gmail.com"
TOEMAIL = "muhammadumairniazi01@gmail.com"
PASSWORD = input("Enter Password: ")

MESSAGE = """Subject: Mail Sent Using Python
Hi Umair,

This is sent using a Test account.

Thanks,
Umair Niazi"""

# Create a secure connection
smtp = smtplib.SMTP(HOST, PORT)
smtp.starttls()

# Login using the secure connection
try:
    status_code, response = smtp.login(FROM_MAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")
except smtplib.SMTPAuthenticationError as e:
    print(f"[!] Authentication error: {e}")
    smtp.quit()
    exit()

# Create a MIMEText object and send the email
msg = MIMEText(MESSAGE)
msg["Subject"] = "Mail Sent Using Python"
msg["From"] = FROM_MAIL
msg["To"] = TOEMAIL

# Send the email
try:
    smtp.sendmail(FROM_MAIL, TOEMAIL, msg.as_string())
    print("[*] Email sent successfully!")
except smtplib.SMTPException as e:
    print(f"[!] Failed to send email: {e}")

# Quit the SMTP session
smtp.quit()
