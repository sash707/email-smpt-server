import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from emaillist import emails
from subject import sub
from tamplate import tamp
from runmultiple import times
from em_pass import servermail
from em_pass import serverpass

alredy= (0)
multiple= (times)
for _ in range(multiple):


    subj = (sub)
    temp= (tamp)
    emailsj= emails[alredy]

    email_lists= (emails)

    # Your email credentials
    sender_email = (servermail)
    sender_password = (serverpass)

    # List of recipient emails

    
    recipient_emails = (emailsj)
    
    


    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ",".join(recipient_emails)
    message["Subject"] = (subj)

    # Your HTML email content
    html_content = (temp)

    # Attach HTML content to the email
    message.attach(MIMEText(html_content, "html"))

    # Connect to Gmail's SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() # Enable encryption
        server.login(sender_email, sender_password)

         # Send email to multiple recipients
        server.sendmail(sender_email, recipient_emails, message.as_string())


    alredy= (alredy+1)
    print("Total email sent: {}".format(alredy))
