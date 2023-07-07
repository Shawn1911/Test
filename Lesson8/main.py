# import bcrypt
#
# password = '123'
# bytes = password.encode('utf-8')
#
# salt = bcrypt.gensalt()
# hash = bcrypt.hashpw(bytes, salt)
#
# new_password='12345'
# bytes_password=password.encode('utf-8')
# print(bcrypt.checkpw(bytes_password,hash))



# import httpx
#
# response = httpx.get("https://www.etutorialspoint.com/images/article_images/send_smtp_mail.jpg")
# d=response.content
# with open("img.png" , "wb") as f:
#     f.write(d)



# import bcrypt
#
# password1 = b"123456"
# hashed1 = bcrypt.hashpw(password1 , bcrypt.gensalt())
#
# password2 = b"123456"
#
# if bcrypt.checkpw(password2 , hashed1):
#     print('YES')
# else:
#     print('NO')


import request

r = request.get("https://jsonplaceholder.typicode.com/posts")

print(r.text)