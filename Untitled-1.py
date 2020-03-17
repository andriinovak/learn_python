import re


file_name = 'this_is.my file,, 34436436 hello'
result = re.split(r'[^a-zA-Z0-9]', file_name)

emails = 'hello baddy, please replay too exam@email.COM or bohdan@wasd.com wasd@name.12345'
emai = 'roman@wasd.com'
email_re = re.compile(r'\w{1,12}@\w{1,8}\.[a-z]{1,8}', flags=re.IGNORECASE)
print(email_re.findall(emails))
# for i in email_adres:
#     print(i.group())
