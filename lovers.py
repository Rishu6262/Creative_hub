text = """LOVE & RELATIONSHIP ❤️

This is a fun beginner-friendly Python project that combines Python fundamentals with a creative relationship-themed experience.

Features:
• Accepts multiple lover names using loops and lists.
• Asks the user whether they are currently in love.
• Generates a random Love Score between 70% and 100%.
• Displays random romantic quotes using random.choice().
• Allows the user to write a personalized love message.
• Provides a gift menu with Jewelry, Rose Flowers, Chocolates & Teddy Bear, and Hug options.
• Includes a separate flow for users who are not currently in love.
• Offers different reasons such as being single, focusing on a career, having a past relationship, waiting for the right person, or not being ready.
• Allows users to write a message to their ex or choose silence.

Technologies Used:
Python, random module, lists, loops, conditional statements, user input, and string methods.

Purpose:
This project is mainly created for practicing Python programming concepts in a fun and interactive way. It can be extended further with Turtle graphics, OpenCV image-to-drawing effects, GUI popups, animations, and a smart gift recommendation system.

Note:
The project is intended for learning and entertainment purposes."""
```


import random
import turtle
import cv2
import os
import time


import faker
fake = faker.Faker()

n= random.randint(1, 100)
names = []

n = int(input("Enter the number of lovers names you want to enter: "))

for i in range(n):
    name = input(f"Enter your lovers name : {i + 1}: ")
    names.append(name)
name = " , ".join(names)
print(names)    

l = int(input("Are you in love with her? (1 for Yes, 0 for No): "))  
if l==1:
    print("You are in love!")
    print("Your lover's name is:", name)
    n = int(input("Enter the numbers of years you have been in a relationship: "))
    print("You have been in a relationship with her for", n, "years.")
    print("\n")
    print("surprise her with a gift!")
    print("❤️ Loves")
    print("🥰 sweetHEART")
    print("😍 LifeLine")
    print("😘 kiss")
    print("\n")
    love_score = random.randint(70, 100)
    print("Your Love Score:", love_score, "% ❤️")
    print("\n")
    quotes = [
    "You are my favorite person ❤️",
    "Love is not something you find, it's something you build 🥰",
    "Every love story is beautiful 💕",
    "Make her smile today 😊"
]

    print(random.choice(quotes))
    message = input("Do you share any special message for her : ")
    print("\n 💌 Your message :")
    print(" I❤️You ", name)
    print(message)
    print("\n")
    print("Here are some gift for her :")
    # print()
    print("1. 💎 Jewelry")
    print("2. 🌹 Rose Flowers")
    print("3. 🍫 Chocolates & Teddy bear")
    print("4. 🤗 hug you with full night")
    print("\n")

    # choice = int(input("Enter your choice of gift (!-4): "))

elif l==0:
    print("you are currently not in love!")
    print("\n why are you not in love with her ?")
    print("1. I am single by choice.")
    print("2. I am focused on my career.")
    print("3. I had a past relationship.")
    print("4. I am waiting for the right person.")
    print("5. I am not ready for a relationship.")
    why = int(input("Enter your reason: "))
    # print("Reason:", why)
    if why == 1:
        print("\n😎 That's completely fine!")
        print("Enjoy your single life and focus on yourself.")
    elif why == 2:
        print("\n📚 Career Mode: ON!")
        print("First build your career, then build your love story. 🚀")
    elif why == 3:
        print("\n💔 Past is past.")
        print("Take your time and focus on yourself.")
    elif why == 4:
        print("\n💕 Waiting for the right person.")
        print("Don't settle for less. The right person will come along.")
    elif why == 5:
        print("\n😴 No problem!")
        print("Relationship is not compulsory. Enjoy your life! 😎")

    else:

        print("\n❌ Invalid choice!")    
    message = input(
            "\nDo you want to write a message to your ex? (yes/no): "
        )

    if message.lower() == "yes":

            ex_message = input("💌 Write your message: ")

            print("\n💌 Your message:")
            print(ex_message)

    else:
        print("\n👍 No message. Sometimes silence is better.")

else:    
    print("Your lover's name is:", name)    


