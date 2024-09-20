import re

# email = input("Please enter youe email: ")
regex = r"\b[a-zA-Z0-9._+%-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}\b"
regex2 = r"\b[^@]+@[^@]+\.[^@]\b" # 提高容忍度，簡化判斷
# 在 Regex 中 +- 放一起有區間的意思，要避免

def check_email(email):
    if re.fullmatch(regex, email):
        print("It's valid email address")
    else:
        print("It's not valid")
    
email1 = "lawrence891106@gmail.com"
email2 = "global-earth@green.org.us"
email3 = "hello.com.tw"

check_email(email1)
check_email(email2)
check_email(email3)