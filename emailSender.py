import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mailer(receiver_email, subject, emailMessage):

    sender_email = "complaintoptimizationwindow@gmail.com"
    # receiver_email = "manubhav2002rastogi@gmail.com"
    password = "zrqf agap ojup fpmf"

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    html = """\
    <html>
    <body>
        {message}
    </body>
    </html>
    """.format(message = emailMessage)

    # .format(imageLink = imageLink)

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
        print("email sent successfully")


# mailer("mukulkumar2652@gmail.com", "testing", "message")


