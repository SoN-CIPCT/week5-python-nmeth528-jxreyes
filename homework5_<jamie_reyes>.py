fruits = ["mango", "pineapple", "banana", "blackberry", "watermelon", "kiwi"]
print(fruits)
first_two = fruits[:2]
first_message = "The first two items in the list are: " + ", ".join(first_two)
print(first_message)
middle_two = fruits[2:4]
second_message = "The middle two items in the list are: " + ", ".join(middle_two)
print(second_message)
third_two = fruits[0:6:5]
third_message = "The first and last items in the list are: " + ", ".join(third_two)
print(third_message)

 

print("\nMenu")
menu = ("sushi", "sashimi", "ramen", "udon", "curry")
for item in menu:
    print(item)

print("\nNew Menu")
new_menu = ("teriyaki",) + menu[1:2] + ("yakisoba",) + menu[3:]
for item in new_menu:
    print(item)