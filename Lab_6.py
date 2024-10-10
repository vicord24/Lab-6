

def ready_or_not():
    name = input("what is your name?")
    user_response = input("Are you ready to use GitHub? (yes/no): ")
    if user_response.lower() == "yes":
        print( name + ", Great! Let's begin.")
    else:
        print(name + ", you have to be ready.")

ready_or_not()