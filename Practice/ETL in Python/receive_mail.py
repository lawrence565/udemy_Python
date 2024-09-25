import imaplib
import email as em
import os
from dotenv import load_dotenv

load_dotenv()

M = imaplib.IMAP4_SSL("imap.gmail.com")
email = "lawrence891106@gmail.com"
password = os.getenv("GMAIL_APP_PASSWORD")
M.login(email, password)
M.select("inbox") # 選擇要互動的資料夾
result, ids = M.search(None, "FROM service@vocus.cc")
id = (ids[0].split())[0]
fetch_result, fetch_content = M.fetch(id, "(RFC822)")
raw_content = fetch_content[0][1]
email_content = raw_content.decode("utf-8")
email_message = em.message_from_string(email_content)

for part in email_message.walk():
    if part.get_content_type() == "text/html":
        body = part.get_payload(decode=True)
        print(body)