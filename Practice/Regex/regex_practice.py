import re
import os


# inline citation
# (alphanumeric, number)



with open("Practice/Regex/research.txt", encoding="utf8") as file:
    content = file.read()

with open("Practice/Regex/Employee/Sellers/International/Japan.txt", encoding="utf8") as file:
    japan_sales = file.read()

with open("Practice/Regex/Employee/Sellers/Local/California.txt", encoding="utf8") as file:
    california_sales = file.read()

def citation_check(file):
    citation = r"\([a-zA-Z0-9\s]+\, \d{4,}\)"
    print(re.findall(citation, file))

# citation_check(content)

result = []

def find_numner(file):
    phone_number = r"\d{3}-\d{3}-\d{4}"
    phone_list = re.findall(phone_number, file)
    for phone in phone_list:
        result.append(phone)

for folder, subfolder, files in os.walk("Practice/Regex/Employee"):
    for f in files:
        with open(os.path.join(folder, f), encoding="utf8") as my_file:
            if(f != ".DS_Store"):
                content = my_file.read()
                find_numner(content)

print(result)