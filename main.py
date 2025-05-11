
print("Hey! I am AI Bot. What is your name? : ")
name = input('Please type')
print(f"Nice to meet you, {name}!")
print("How are you feeling today? write (good/bad) : ")
mood = input().lower()
if mood == "good":
    print("Oh I am glad to hear that")
elif mood == "bad":
    print("I am sorry to hear that. Hope things will get better soon.")
else:
    print("I see. Sometimes it's difficult to put feelings into words.")
print(f"It was nice chatting with you {name}. Goodbye!")
