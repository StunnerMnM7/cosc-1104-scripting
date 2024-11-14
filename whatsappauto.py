from selenium.webdriver.common.keys import Keys
from threading import Thread
from pywhatkit import sendwhatmsg_instantly, sendwhats_image
from time import sleep

# Message function
def send_msg(ph, msg):
    sendwhatmsg_instantly(f"{ph}", msg) 
    sleep(2)
    Keys.ENTER
    print("Successfully Sent!")

# Image function
def send_img(ph, img_path, caption):
    try:
        sendwhats_image(f"{ph}", img_path, caption)
        sleep(8)
        Keys.ENTER
        print("Image sent!")
    except Exception as Er:
        print(f"Error occured while sending image: {Er}")

# Options for either text or image
to_do = ["1. Send WhatsApp text message", "2. Send WhatsApp image message"]
for eachitem in to_do:
    print(eachitem)

try:
    choice = int(input("Please enter your choice (1 or 2): \n"))
except ValueError:
    print("Invalid choice! Please enter a number.")
    exit(1) # exiting program with error code 1. 

# Asking the user for the phone number
c_code = input("Enter the country code (eg. 1 for CA or 91 for IN): ").strip()
number = input("Great! Now enter the 10-digit phone number: ").strip()
phone_number = f"+{c_code}{number}"

# Sending messages based on user input
if choice == 1:
    msg = input("Please enter your message: \n")
    t1 = Thread(target=send_msg, args=(phone_number, msg))
    t1.start()
    t1.join()

# Image with choice of default path and new path
elif choice == 2:
    try:    
        default_img_path = "M:/Git/Repositories/cosc-1104-scripting/default_image.png"
        caption = input("Enter image caption: \n")
        img_path = input("Enter the image file path or press ENTER to use default image: ").strip()
        if not img_path:
            img_path = default_img_path  
        t2 = Thread(target=send_img, args=(phone_number, default_img_path, caption,))
        t2.start()
        sleep(2)
        t2.join()
    except TypeError as Er:
        exit(1)
        

else:
    print("Invalid choice entered! Please select 1 or 2.")
