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