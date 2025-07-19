# birthday_countdown.py

import datetime
import random

# 🎁 Fun gift ideas
gift_ideas = [
    "A handwritten letter 💌",
    "Wireless earbuds 🎧",
    "Your favorite book 📖",
    "Custom mug ☕",
    "Plants or succulents 🪴",
    "A box of chocolates 🍫",
    "Movie night with popcorn 🍿",
    "Personalized keychain 🔑",
    "Online course subscription 🎓",
    "A beautiful dress"

]

def get_user_birthday():
    try:
        date_str = input("Enter your birthday (dd-mm): ")
        day, month = map(int, date_str.split("-"))
        today = datetime.date.today()
        this_year = today.year
        birthday = datetime.date(this_year, month, day)
        
        # If birthday already passed this year, set it for next year
        if birthday < today:
            birthday = datetime.date(this_year + 1, month, day)

        days_left = (birthday - today).days

        print(f"\n🎂 Your birthday is in {days_left} day(s)!")
        print("🎁 Here's a random gift idea for you:", random.choice(gift_ideas))

    except Exception as e:
        print("⚠️ Invalid input. Please enter date in dd-mm format. Example: 25-12")

# Run the program
print("🗓️ Mini Birthday Countdown 🎉")
get_user_birthday()
