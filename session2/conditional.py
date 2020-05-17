# # # print('ban la nguoi nhu the nao')
# # # i = int(input("nhap mot so bat ky ban thich"))
# # # if i<=20:
# # #     print('you are nice')
# # # elif i<=40:
# # #     print('ok how are you today')
# # # elif i<=60:
# # #     print('hehe')
# # # elif i<= 80:
# # #     print("leu leu")
# # # else:
# # #     print('you are supper man')


# # # tinh ham bac hai
# # print('tính hàm bậc hai')
# # a = int(input("nhập vào giá trị a =  "))
# # b = int(input('nhập vào giá trị b =  '))
# # c = int(input('nhập vào giá trị c =  '))
# # delta = (b*b) - (4*a*c)
# # if delta < 0:
# #     print('phương trình vô nghiệm ')
# # elif delta == 0 :
# #     print('phương trình có nghiệm, x = ', -(b/(2*a)))
# # else:
# #     print('phương trình có nghiệm, x= ', (-b+ delta**(1/2)/(2*a)), (-b- delta**(1/2))/(2*a))


# while True:
#     print('you cant stop me')


accout_username = 'mindx'
accout_password = '123'

running = True
while running:

    username = input('username')
    password = input('password')
    if username == accout_username and password == accout_password:
      print("hello")
      running = False
    else:
        print('leu leu')
