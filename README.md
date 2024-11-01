
# Whapy NoteAI

A simple Python script to automatically send WhatsApp messages using `pywhatkit`. This project is designed to help users send messages to multiple recipients with minimal effort.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)
- [License](#license)
- [Contributing](#contributing)
- [Downloads](#downloads)

## Features

- Send personalized messages to a list of phone numbers.
- Easy configuration of message content through a GUI.
- Automatically handles the timing for message delivery.

## Requirements

- Python 3.x
- `pywhatkit` library
- `tkinter` library (usually included with Python)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/akshay-k-a-dev/whapy-noteai.git
   cd whapy-noteai
   ```

2. Install the required package:
   ```bash
   pip install pywhatkit
   ```

3. Ensure you have the `numbers.txt` file in the same directory, containing the phone numbers (one per line) with the Indian country code (+91).

## Usage

1. Open the script `bot.py`:
   ```bash
   python bot.py
   ```

2. Use the GUI to upload your phone numbers file and enter your message.

3. Click the "Send Messages" button. Make sure you are logged into WhatsApp Web in your default browser. The script will open WhatsApp Web and send the messages as scheduled.

## Notes

- The script sends messages with a delay to avoid spamming WhatsApp.
- Ensure your internet connection is stable during execution.
- Adjust the sleep time if needed to accommodate your sending speed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests. Feel free to make any further adjustments as needed!

## Downloads

You can download the following files:

- [whapy.deb](dist/whapy.deb)
- [bot](dist/bot)


```
