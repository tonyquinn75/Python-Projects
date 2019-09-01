# #
# #
# # # character_name = "John"
# # # character_age = "35"
# # # print(" There was once a man called" + " " + character_name + ",");
# # # print("he was " + " " + character_age + ",");
# # # character_age = input("Pick an age")
# # # print("He really liked the name George");
# # # print("but  dodn't like being " + character_age + ",");
# # # num1 = input("Enter a number:")
# # # num2 = input("Enter another number")
# # # result = float(num1) + float(num2)
# # # print(result)
# #
# # # # <editor-fold desc="Description">
# # # color = input("Enter a color:")
# # # plural_noun = input("Enter a plural noun:")
# # # celebrity = input("Enter a celebrity name:")
# # # whitespace = " "
# # #
# # # print("Roses are " + color)
# # # print(plural_noun+whitespace+ "are blue")
# # # print("I love" + whitespace + celebrity)
# # # # </editor-fold>
# # # lucky_numbers = [4,8,16,32,64,128]
# # # friends = ["Kevin", "Karen","Jim", "Lynn","Flynn","Skinn","Jim"]
# # # print(friends)
# # # friends.extend(lucky_numbers)
# # # print(friends)
# # # friends.insert(1,"Kelly")
# # # print(friends)
# # # friends.pop(2)
# # # print(friends)
# # # print(friends.count("Jim"))
# # # #friends.sort()
# # # print(friends)
# #
# #
# # # coordinates = (4,5)
# # # print(coordinates[1])
# # x_val = input("Input x")
# # y_val = input("Input y")
# # name = input("What's the name")
# #
# #
# # # result = (x_val,y_val)
# # # print(result)
# # def add_2_numbers(x_val, y_val):
# #     a = x_val
# #     b = y_val
# #     return float(a )+ float(b)
# #
# #
# #
# # print(add_2_numbers(x_val, y_val))
# # print(name)
# # import p
#
# is_male = False
# is_tall = False
# if is_male or is_tall:
#     print("You are a male or tall or both")
# elif is_male and not (is_tall):
#     print("You are a short male")
# elif is_male and is_tall:
#     print("You are not a male but are tall")
# else:
#     print("You are neither  male nor tall")
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300,6,1100))
