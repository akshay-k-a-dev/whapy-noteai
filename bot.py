import pywhatkit as kit
import time
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to send messages
def send_messages():
    # Read phone numbers from the file
    try:
        with open(file_path.get(), 'r') as file:
            numbers = [line.strip() for line in file.readlines()]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file: {e}")
        return
    
    message = message_entry.get("1.0", tk.END).strip()
    
    # Check if media file is selected
    media_file = media_path.get()
    
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
            if media_file.lower().endswith(('.jpg', '.jpeg', '.png')):
                kit.sendwhats_image(number, media_file, message, wait_time=15)
            else:
                kit.sendwhatmsg(number, message, hour, minute)
            
            # Sleep for a short period to avoid spamming WhatsApp
            time.sleep(15)  # Wait 15 seconds before sending the next message
        
        except Exception as e:
            print(f"Failed to send message to {number}: {e}")
            messagebox.showwarning("Warning", f"Failed to send message to {number}: {e}")
    
    messagebox.showinfo("Success", "Messages sent successfully!")

# Function to upload the file
def upload_file():
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if path:
        file_path.set(path)

# Function to upload media file
def upload_media():
    path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg;*.jpeg;*.png"), ("Videos", "*.mp4;*.mov;*.avi")])
    if path:
        media_path.set(path)

# GUI setup
app = tk.Tk()
app.title("Whap-NOTEAI")
app.geometry("400x400")

file_path = tk.StringVar()
media_path = tk.StringVar()

# Title label
title_label = tk.Label(app, text="Whap-NOTEAI", font=("Helvetica", 20, "bold"))
title_label.pack(pady=10)

# Upload file button
upload_button = tk.Button(app, text="Upload Number List", command=upload_file)
upload_button.pack(pady=10)

# Text area for message
message_label = tk.Label(app, text="Enter your message:")
message_label.pack(pady=5)

message_entry = tk.Text(app, height=5, width=40)
message_entry.pack(pady=10)

# Upload media button
media_button = tk.Button(app, text="Upload Media File", command=upload_media)
media_button.pack(pady=10)

# Send button
send_button = tk.Button(app, text="Send Messages", command=send_messages)
send_button.pack(pady=20)

app.mainloop()
