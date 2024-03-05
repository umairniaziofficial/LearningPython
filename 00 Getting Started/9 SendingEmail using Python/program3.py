import imaplib
import email
import getpass
from email.header import decode_header

# IMAP server and port
mail_server = "imap.gmail.com"
port = 993

# Connect to the IMAP server
mail = imaplib.IMAP4_SSL(mail_server, port)

# Get user credentials
user_email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")

# Login to the email account
mail.login(user_email, password)

# Select the mailbox (inbox in this case)
mail.select("inbox")

# Search for all emails
result, data = mail.search(None, "ALL")

# Fetch the email IDs
email_ids = data[0].split()


# Function to decode email header
def decode_email_header(header):
    value, encoding = decode_header(header)[0]
    if encoding:
        return value.decode(encoding)
    else:
        return value


# Print details of each email
for email_id in email_ids:
    result, msg_data = mail.fetch(email_id, "(RFC822)")
    raw_email = msg_data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Extract email details
    sender = decode_email_header(msg["From"])
    subject = decode_email_header(msg["Subject"])
    date = msg["Date"]

    # Print email details
    print(f"Email ID: {email_id.decode()}")
    print(f"Sender: {sender}")
    print(f"Subject: {subject}")
    print(f"Date: {date}")

    # Print email body if available
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                print(f"Body:\n{body.decode()}")
    else:
        body = msg.get_payload(decode=True)
        print(f"Body:\n{body.decode()}")

    print("\n" + "-" * 30 + "\n")

# Logout from the email account
mail.logout()
