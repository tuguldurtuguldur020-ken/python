# Параметр ба аргумент гэж юу вэ?
# def greet(name):
#     print("Hello", name)

# greet("Bat")
# greet("Sara")

# Энд:
# - name — параметр. Функцэд утга хүлээн авах хувьсагч.
# - "Bat" болон "Sara" — аргумент. Функцэд өгч буй бодит утгууд.
# Үүнийг хайрцгаар төсөөлөөрэй:
# greet("Bat")
# Аргумент: "Bat"


# def greet(name):
# Параметр name нь "Bat" утгыг авна.


# print("Hello", name)
#########################

# def greet(name):
#     print("Сайн уу,", name)

# greet("Бат")
# greet("Сараа")

# 3. Хоёр параметртэй функц################

# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)


# Үүнийг алхам алхмаар ойлгоё:
# 1. add(5, 3) гэж дуудна.
# 2. a = 5, b = 3 болно.
# 3. return a + b нь 5 + 3-ыг бодно.
# 4. 8 гэсэн утга буцна.
# 5. print(result) нь 8 гэж хэвлэнэ.
# Санах зүйл:
# - def — функц үүсгэнэ.
# - parameter — функцийн хаалт доторх хувьсагч.
# - argument — функцэд дамжуулж буй бодит утга.
# - return — үр дүнг буцаана.
# - print() — дэлгэцэнд харуулна.




# # 4
# - *args — олон утгыг хүлээн авна.
# - args — утгуудыг tuple хэлбэрээр хадгална.
# - for num in args — утга бүрээр давтана.
# - result += num — тухайн утгыг нийлбэр дээр нэмнэ.
# Санах зүйл: args гэдэг нэрийг заавал хэрэглэх албагүй. *numbers гэж нэрлэж болно. Гол нь * тэмдэг юм.

# Argument гэдэг нь функцийг дуудахдаа хаалт дотор дамжуулж өгч байгаа бодит утга юм


# ner = ["bat", ["bold "]]
# def hello(n):
#     print("Сайн уу!",n)
# hello("a")

# def hello(name):
#     print("snu", name)
# hello("bat")
# hello("saraa")
# hello("bold")

# def nemeh(a,b):
#     print(a+b)
# nemeh(5,3)

# def too(n, * urjih = 3 ):

# def bodoh(une, shirheg =2):
#     return une * shirheg 
# a = bodoh(5000)
# b = bodoh(3000,4)
# print(a)
# print(b)
# print(a+b)
