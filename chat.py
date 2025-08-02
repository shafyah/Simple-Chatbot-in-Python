print("welcome to your chat bot ")
while True:
    user_input = input("you:")
    if user_input.lower () in ["good luok", "goodby" ,"exit", "quit"]:
        print ("chat bot , good bay")
        break 
    elif "what is your name" in user_input:
        print ("my name is shafaih bot ")

    elif "how are you" in user_input:
        print ("i'm fine ")

    elif "thank you" in user_input:
        print ("you welecome ")


    else:
        print ("sory i didnt understand")