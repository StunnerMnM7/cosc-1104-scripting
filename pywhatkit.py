from pywhatkit import sendwhatmsg_instantly
from pywhatkit import sendwhats_image
from selenium.webdriver.common.keys import Keys
from threading import Thread
from time import sleep

# Function to send a text message
def send_msg(ph, msg):
    sendwhatmsg_instantly(f"+91{ph}", msg)  # Removed redundant f-string for `msg`
    print("Successfully Sent!")

# Function to send an image with a caption
def send_img(ph, img_path, caption, close_tab):
    sendwhats_image(f"+91{ph}", img_path, caption, close_tab)
    print("Image sent!")

# Options for the user to select between sending text or image
to_do = ["1. Send WhatsApp text message", "2. Send WhatsApp image message"]
for eachitem in to_do:
    print(eachitem)

# User choice input handling
try:
    choice = int(input("Please enter your choice (1 or 2): \n"))
except ValueError:
    print("Invalid choice! Please enter a number.")
    exit(1)

# Asking the user for the phone number
phone_number = input("Enter the phone number (without country code): ").strip()

# Sending messages based on user choice
if choice == 1:
    msg = input("Please enter your message: \n")
    t1 = Thread(target=send_msg, args=(phone_number, msg))
    t1.start()
    t1.join()

elif choice == 2:
    caption = input("Enter image caption: \n")
    img_path = "C:\\Users\\Admin\\Desktop\\default.bmp"  # Default image path
    close_tab = True  # Option to close tab after sending
    t2 = Thread(target=send_img, args=(phone_number, img_path, caption, close_tab))
    t2.start()
    t2.sleep(5)
    t2.join()

else:
    print("Invalid choice entered! Please select 1 or 2.")
