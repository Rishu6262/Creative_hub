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



























































































# # def draw_image(image_name, title):
# #     base_dir = os.path.dirname(os.path.abspath(__file__))
# #     image_path = os.path.join(base_dir,image_name)
# #     img = cv2.imread(image_path)


# # import turtle
# # import cv2
# # import os
# # import time


# # # =========================================================
# # # IMAGE CONTOUR DRAWING FUNCTION
# # # =========================================================

# # def draw_image(image_name, title):
# #     """
# #     Image ko OpenCV contours mein convert karke
# #     Turtle se draw karta hai.
# #     """

# #     # -----------------------------------------------------
# #     # 1. Python file ka folder
# #     # -----------------------------------------------------

# #     base_dir = os.path.dirname(os.path.abspath(__file__))

# #     # Image ka complete path
# #     image_path = os.path.join(base_dir, image_name)

# #     # -----------------------------------------------------
# #     # 2. Image Load
# #     # -----------------------------------------------------

# #     img = cv2.imread(image_path)

# #     if img is None:
# #         print(f"❌ Error: Could not load '{image_path}'")
# #         return

# #     print(f"✅ Image loaded: {image_path}")

# #     # -----------------------------------------------------
# #     # 3. Resize Image
# #     # -----------------------------------------------------

# #     target_width = 650

# #     h, w = img.shape[:2]

# #     target_height = int((h / w) * target_width)

# #     img_resized = cv2.resize(
# #         img,
# #         (target_width, target_height),
# #         interpolation=cv2.INTER_AREA
# #     )

# #     # -----------------------------------------------------
# #     # 4. Convert to Grayscale
# #     # -----------------------------------------------------

# #     gray = cv2.cvtColor(
# #         img_resized,
# #         cv2.COLOR_BGR2GRAY
# #     )

# #     # -----------------------------------------------------
# #     # 5. Threshold
# #     # -----------------------------------------------------

# #     _, thresh = cv2.threshold(
# #         gray,
# #         70,
# #         255,
# #         cv2.THRESH_BINARY
# #     )

# #     # -----------------------------------------------------
# #     # 6. Find Contours
# #     # -----------------------------------------------------

# #     contours, hierarchy = cv2.findContours(
# #         thresh,
# #         cv2.RETR_TREE,
# #         cv2.CHAIN_APPROX_NONE
# #     )

# #     # -----------------------------------------------------
# #     # 7. Turtle Screen
# #     # -----------------------------------------------------

# #     screen = turtle.Screen()

# #     screen.setup(
# #         width=850,
# #         height=850
# #     )

# #     bg_color = "#181b22"

# #     screen.bgcolor(bg_color)

# #     screen.title(title)

# #     # -----------------------------------------------------
# #     # 8. Turtle Pen
# #     # -----------------------------------------------------

# #     pen = turtle.Turtle()

# #     pen.hideturtle()

# #     # Fast drawing
# #     pen.speed(0)

# #     pen.pensize(1.5)

# #     # -----------------------------------------------------
# #     # 9. Center Image
# #     # -----------------------------------------------------

# #     offset_x = target_width / 2
# #     offset_y = target_height / 2

# #     # -----------------------------------------------------
# #     # 10. Colors
# #     # -----------------------------------------------------

# #     gold_stroke = "#D49B24"

# #     gold_fill = "#F5C842"

# #     # -----------------------------------------------------
# #     # 11. Draw Contours
# #     # -----------------------------------------------------

# #     if hierarchy is not None:

# #         for i, h_info in enumerate(hierarchy[0]):

# #             area = cv2.contourArea(contours[i])

# #             # Tiny noise skip
# #             if area < 15:

# #                 continue

# #             # Very large contour skip
# #             if area > (
# #                 target_width *
# #                 target_height *
# #                 0.45
# #             ):

# #                 continue

# #             # -------------------------------------------------
# #             # Calculate contour depth
# #             # -------------------------------------------------

# #             depth = 0

# #             parent = h_info[3]

# #             while parent != -1:

# #                 depth += 1

# #                 parent = hierarchy[0][parent][3]

# #             # -------------------------------------------------
# #             # Hole handling
# #             # -------------------------------------------------

# #             if depth % 2 == 1:

# #                 pen.pencolor(gold_stroke)

# #                 pen.fillcolor(bg_color)

# #             else:

# #                 pen.pencolor(gold_stroke)

# #                 pen.fillcolor(gold_fill)

# #             # -------------------------------------------------
# #             # First point
# #             # -------------------------------------------------

# #             pen.penup()

# #             first_pt = contours[i][0][0]

# #             pen.goto(
# #                 first_pt[0] - offset_x,
# #                 offset_y - first_pt[1]
# #             )

# #             pen.pendown()

# #             # -------------------------------------------------
# #             # Start Fill
# #             # -------------------------------------------------

# #             pen.begin_fill()

# #             # Draw contour points

# #             for pt in contours[i][1:]:

# #                 x = pt[0][0] - offset_x

# #                 y = offset_y - pt[0][1]

# #                 pen.goto(x, y)

# #             # Close contour

# #             pen.goto(
# #                 first_pt[0] - offset_x,
# #                 offset_y - first_pt[1]
# #             )

# #             # Finish fill

# #             pen.end_fill()

# #             pen.penup()

# #     # -----------------------------------------------------
# #     # 12. Keep Window Open
# #     # -----------------------------------------------------

# #     turtle.done()


# # # =========================================================
# # # MAIN PROGRAM
# # # =========================================================


# # print("\n" + "=" * 45)

# # print("       ❤️ LOVE GIFT SHOP ❤️")

# # print("=" * 45)

# # print()

# # print("1. 💎 Jewelry")

# # print("2. 🌹 Rose Flowers")

# # print("3. 🍫 Chocolate & Teddy Bear")

# # print("4. 🤗 Hug")

# # print()


# # # ---------------------------------------------------------
# # # User Gift Choice
# # # ---------------------------------------------------------

# # choice = int(
# #     input("Enter your gift choice (1-4): ")
# # )


# # # =========================================================
# # # Gift Selection
# # # =========================================================

# # if choice == 1:

# #     print("\n💎 Creating Jewelry...")

# #     draw_image(
# #         "images.jpeg",
# #         "💎 Jewelry For Your Love"
# #     )


# # elif choice == 2:

# #     print("\n🌹 Creating Roses...")

# #     draw_image(
# #         "rose.jpg",
# #         "🌹 Roses For Your Love"
# #     )


# # elif choice == 3:

# #     print("\n🍫 Creating Chocolate & Teddy...")

# #     draw_image(
# #         "chocolate.jpg",
# #         "🍫 Chocolate & Teddy Bear"
# #     )


# # elif choice == 4:

# #     print("\n🤗 Creating Hug...")

# #     draw_image(
# #         "hug.jpg",
# #         "🤗 A Big Hug For Your Love"
# #     )


# # else:

# #     print("\n❌ Invalid choice!")

# #     print("Please enter a number between 1 and 4.")
