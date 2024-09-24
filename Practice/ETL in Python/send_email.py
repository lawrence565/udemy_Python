import smtplib

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()

email = "lawrence891106@gmail.com"
password = ""
# getpass.getpass("Enter your password: ") 可以在 Terminal 安全的獲取密碼
print(smtp_obj.login(email, password))

from_address = "pythonemail@gmail.com"
to_address = "5655566haha@gmail.com"
subject = input("Enter email subject: ")
message = input("Enter email messgae: ")
full_messgae = "Subject: " + subject + "\n" + message

result = smtp_obj.sendmail(from_address, to_address, full_messgae)
if result == {}:
    print("Success!!!")
smtp_obj.quit()