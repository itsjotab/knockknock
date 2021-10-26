print ('Want to hear a Knock Knock joke ?')

answer = input("yes or no ?: ")
if "yes" in answer:
    print("knock Knock")
    reply = input("answer or type help for help here: ")
    if "who is it" in reply:
        print("Me")
        asking = input("You know what comes next: ")
        if "me who" in asking:
            print("Me too! Hahahahaha ... aint I hilarious ?")
    elif "help" in reply:
        print("You not getting any help! *SMH*")
    else:
        print("WRONG ANSWER BRO!!")
else:
    print("You are Lameeeeeee and You Suck !!!! *middle finger*")
