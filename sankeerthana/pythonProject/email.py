import smtplib
from email.message import EmailMessage

def sendmail(to, subject='brainless idiot', body='ni thalakai'):
    print("Starting email send process...")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    print("Connected to the SMTP server.")

    server.login('sankeerthanachikati540@gmail.com', 'wvwx pknn sqyg wkkl')
    print("Logged in to the SMTP server.")

    msg = EmailMessage()
    msg['From'] = 'sankeerthanachikati540gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)

    server.send_message(msg)
    print("Email sent successfully.")
    server.quit()
    print("Connection closed.")

# Example usage
sendmail('avkarthikeya2002@gmail.com')