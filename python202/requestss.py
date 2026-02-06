import requests 

# responsess = requests.get("https://github.com/mahesh-bhosle100/PYTHON_decorater_exception-handling_-_-LEGB_rule/tree/main")
# print(responsess.text)

import re
x = re.search("cat", "I have a cat")
print(x)

x = re.findall("a", "banana")   # ['a', 'a', 'a']
print(x)
x = re.findall(r"\d+", "Age 25, year 2024")  # ['25','2024']

print(x)
x = re.search(r"(\d+)-(\d+)", "Date 12-09").groups()
print(x)
x = pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
print(x)