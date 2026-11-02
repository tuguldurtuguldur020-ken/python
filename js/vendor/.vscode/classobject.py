# class player:
#     def __init__(self, name, skins):
#         self.name=name 
#         self.skins = skins


# player1 = player("bat",1)
# player2 = player("saraa",2)
# print(player1.name,end=" ")
# print(player1.skins,end=" ")
# print(player2.name,end=" ")
# print(player2.skins,end=" ")

# 2
# class student:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
# student1 = student("naraa",17)
# student2 = student("temuulen",19)
# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)

# # 3
# class student:
#     def __init__(self, name, age, grade):
#         self.name=name
#         self.age=age
#         self.grade=grade

# student1 = student("bat",18, "12A")
# print(student1.name)
# print(student1.age)
# print(student1.grade)


# 4
# class student:
#     def __init__(self, name, score):
#         self.name=name
#         self.score=score

# student1 = student("bat",85)
# student2 = student("saraa",95)
# print(student1.name,end=" ")
# print(student1.score,end=" ")
# print(student2.name,end=" ")
# print(student2.score,end=" ")

# 5
# class student:
#     def __init__(self, name, onoo):
#         self.name=name
#         self.onoo=onoo
    
#     def add_score(self):
#         self.onoo +=20

# student1 = student("bat",80)
# student1.add_score()
# print(student1.onoo)


# 6

# class student:
#     def __init__(self, ner, nas, angi):
#         self.ner=ner
#         self.nas=nas
#         self.angi=angi
#     def show_info(self):
#         self.show_info
# student1 = student("saraa",19 , "12B")
# student1.show_info()
# print(student1.ner)
# print(student1.nas)
# print(student1.angi)


# 7
# class student:
#     def __init__(self, name, onoo):
#         self.name=name
#         self.onoo=onoo
#     def check_result(self):
#         self.check_result
#         if onoo > 60:
#             return tentssen
#         else:
#             return tentseegu
# student1 = student("bat", 75)
# student2 = student("naraa",45)
# print(student1.name)
# print(student1.onoo)
# print(student2.name)
# print(student2.onoo)


# 8
# class student:
#     def __init__(self, name, onoo):
#         self.name=name
#         self.onoo=onoo
    
#     def add_score(self):
#         self.onoo +=20

# student1 = student("bat",80)
# student1.add_score()
# print(student1.onoo)


# 9###################
# class student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def birthday(self):
#         self.score+=1
# student1 = student("saraa",18)
# student1.birthday()
# student1.birthday()
# # print(student1.name)
# print(student1.score)

# 10#################
# class Student:
#     def __init__(self, name, unelgee):
#         self.name=name
#         self.unelgee=unelgee
#     def get_grade(self):
#         if self.unelgee > 100:
#             print("buruu dun")
#         elif self.unelgee > 90:
#             print("A")
#         elif self.unelgee > 80:
#             print("B")
#         elif self.unelgee > 70:
#             print("C")
#         elif self.unelgee > 60:
#             print("D")
#         else:
#             print("F")
# student1 = Student("bat", 78)
# student2 = Student("saraa", 67)
# student1.get_grade()
# student2.get_grade()
# 11
# class Student:
#     # c = 0 
#     def __init__(self, name, irts):
#         self.name=name
#         self.irts=irts
#     def show_attendance(self):
#         self.irts+=0
# student1 = Student("bat", 2)
# student1.show_attendance()
# print(student1.name)
# print(student1.irts)
######################
# class Student:
#     # c = 0 
#     def __init__(self, name):
#         self.name=name
#     def attend(self):
#         self.attend()
#     def show_attendance(self):
#         self.irts+=1
# student1 = Student("bat", 2)
# student1.show_attendance()
# student1.attend()
# print(student1.name)
# print(student1.attend)

# 12
# class student:
#     def __init__(self, name, onoo, irts):
#         self.name=name
#         self.onoo=onoo
#         self.irts=irts 
#     def check_result(self):
#         if self.onoo > 60 and self.irts > 80:
#             print("tentslee")
#         else:
#             print("tentssengui")

# student1 = student("bat", 75, 68)
# student2 = student("naraa", 45, 89)
# student1.check_result()
# student2.check_result()


# 13
# class Student:
#     def __init__(self, name, onoo):
#         self.name=name
#         self.onoo=onoo
#     def show_scores(self):
#         print(self.score)
#     def add_score(self):
#         print(add_score)
#     def average(self):
#         print(onoo)
# student1 = student("bat",[80,90,70])
# student1.show_scores()
# student1.add_score(87)
# student1.average()


# shine dasgal######################################333
class phone:

    def __init__(self, brand, battery):
        self.brand=brand
        self.battery=battery 
    def use_phone(self):
        self.battery -= 10
    def charge(self):
        self.battery += 20
    def show_battery(self):
        print(f"tseneg: {self.battery}%")
brand = input("Utasnii ner: ")
battery = int(input("Tsenegiin huvi: "))
phone1 = phone(brand, battery)
phone1.use_phone()
phone1.show_battery()

phone1.charge()
phone1.show_battery()

