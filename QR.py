# 🔐 Python QR Code Generator
A simple and practical **Python-based QR Code Generator** that allows users to convert text, URLs, contact information, and other data into scannable QR codes.

### 🚀 Features

* Generate QR codes from custom data
* Support for text and URLs
* Save QR codes as image files
* Simple and beginner-friendly Python implementation
* Uses the `qrcode` library

### 🛠️ Tech Stack

**Python | QRCode | PIL**

### 💡 How It Works

User enters data → Python encodes the data → QR code is generated → QR image can be scanned using any QR scanner.

This project helped me understand **Python libraries, data encoding, user input handling, and file generation**.



# ```````````````````````````````````````````````````````````````````````````````````````````````````````````````
import qrcode
name =input("Enter your name : ")
email =input("Enter your mail : ")
portfolio_link = input("Enter your link: ")

data =f"""
Name:{name}
Mail:{email}
Portfolio:{portfolio_link}"""


qr=qrcode.make(data)
qr.save("My_Detail_qr.png")
print("QR Code generated successfully!")

````````````````````````````````````````````````````````````````````````````````````````````````````````````````
