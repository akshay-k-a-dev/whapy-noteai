import pywhatkit as kit
import time

# Read phone numbers from the file
with open('numbers.txt', 'r') as file:
    numbers = [line.strip() for line in file.readlines()]

# Define the message to send
message = "Hello! Put your message here"

# Send messages
for number in numbers:
    try:
        # Set the time to send the message (current time + 2 minutes)
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min + 2  # Schedule to send after 2 minutes
        
        # Adjust minute and hour if it exceeds 59
        if minute >= 60:
            minute -= 60
            hour += 1
            
        if hour >= 24:
            hour -= 24
        
        # Send the message
        kit.sendwhatmsg(number, message, hour, minute)
        
        # Sleep for a short period to avoid spamming WhatsApp
        time.sleep(15)  # Wait 15 seconds before sending the next message

    except Exception as e:
        print(f"Failed to send message to {number}: {e}")
