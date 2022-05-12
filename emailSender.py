def mailsender(reciever, subject, message):
    import smtplib
    from email.message import EmailMessage

    msg = EmailMessage()
    msg.set_content(message)
    # msg.set_content('This is my message')

    msg['Subject'] = subject
    # msg['Subject'] = 'Hired as technician in Royal Tech Support'
    msg['From'] = "complaintoptimizationwindow@gmail.com"
    msg['To'] = reciever
    # msg['To'] = "mukulkumar2652@gmail.com"

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("complaintoptimizationwindow@gmail.com", "Manubhav@123")
    server.send_message(msg)

    print("message sent successfully")
    server.quit()