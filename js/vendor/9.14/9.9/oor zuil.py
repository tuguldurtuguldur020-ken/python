# import random
# hp = 100
# enemy_hp = 100
# print("BATTLE START")

# while hp > 0 and enemy_hp > 0:
#     print("\nCHinii HP:", hp)
#     print("Daisnii HP:", enemy_hp)
#     action = input("1 = Attack, 2 = Heal: ")
#     if action =="1":
#         damage = random.randint(10, 30)
#         enemy_hp -=damage
#         print(F" CHI {damage} damage hiilee!")
#     elif action == "2":
#         heal = random.randint(10, 20)
#         hp +=heal
#         print(F" {heal} HP sergeeev!")
#     else:
#         print("Buruu songolt")

#     if enemy_hp > 0:
#         damage = random.randint(5, 20)
#         hp -=damage
#         print(F" Daisan {damage} damage hiilee!")
# if hp <=0:
#     print("CHI ylagdlaa")
# else:
#     print("CHI ylla")













# Давхар List + шалгалт
# Жишээ нь 18-аас дээш насныхны нэрийг хэвлэе.

# students = [
#     ["Bat", 17],
#     ["Sara", 19],
#     ["Bold", 20]
# ]

# for i in students:
#   if i [1] >=18:
#     print(i[0])




# Dict-д утга өөрчлөх


# student = {
#     "name": "Bat",
#     "age": 17
# }

# student["age"] = 18

# print(student)






# 6. Dict-д шинэ key/value нэмэх

# student = {
#     "name": "Bat",
#     "age": 17
# }

# student["score"] = 90

# # print(student)

# output 
# {'name': 'Bat', 'age': 17, 'score': 90}


# a = int(input("nasaa oruul:"))
# if a > 18:
#     print("nasand hursen")
# else:
#     print("nasand hureegu")