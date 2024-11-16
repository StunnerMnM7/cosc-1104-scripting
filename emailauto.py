import smtplib
from email.message import EmailMessage
from threading import Thread
from time import sleep, strptime, mktime
from datetime import datetime

# Send email function
def send_email(to_email, subject, body):
    try:
        # Server configuration and email (requires email and pass)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        from_email = "[*Put your email*]" 
        password = "[*Add your password here*]"  
        msg = EmailMessage()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)

        # Server connection 
        with smtplib.SMTP(smtp_server, smtp_port) as ef:
            ef.starttls() 
            ef.login(from_email, password)
            ef.send_message(msg)

        print("Email successfully sent!")
    except Exception as Er:
        print(f"Error sending email: {Er}")
        
def schedule_email(to_email, subject, body, send_time):
    # Convert send_time (HH:MM) to a datetime object for today
    now = datetime.now()
    send_time_format = strptime(send_time, "%H:%M")
    send_time_today = datetime(now.year, now.month, now.day, send_time_format.tm_hour, send_time_format.tm_min)

    # Calculate delay 
    delay = (send_time_today - now).total_seconds()
    if delay < 0:
        print("Scheduled time is in the past. Please enter a future time.")
        return

    print(f"Email will be sent in {delay} seconds.")
    sleep(delay) 
    send_email(to_email, subject, body)

print("Send a follow-up email")

# Fetch user input (email, subject, body)
to_email = input("Enter the recipient's email address: ").strip()
subject = input("Enter the subject of the email: ").strip()
body = input("Enter the body of the email or press ENTER to pick one of the templates: ").strip()
templates = ["1. Hello, I hope this email finds you well. Just following up on our last discussion.\n",
             "2. Hi, As per our discussion earlier, let's schedule a meeting next working day to look into the matter further."]

# Display templates if body is empty 
if not body:
    print("The email body is empty. Please choose from the following templates:")
    for n, template in enumerate(templates, start=1):
        print(f"{n}. {template}")
    
    # Ask user to choose a template
    try:
        template_choice = int(input("Enter the number of the template you want to use: "))
        if 1 <= template_choice <= len(templates):
            body = templates[template_choice - 1] 
            print(f"Using selected template:\n{body}")
        else:
            print("Invalid choice. Exiting.")
            exit(1)
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the template. Exiting.")
        exit(1)

# Send the email in a new thread
t1 = Thread(target=schedule_email, args=(to_email, subject, body, send_time))
t1.start()
sleep(5)
t1.join()   