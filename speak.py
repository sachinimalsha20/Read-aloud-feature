import pyttsx3
engine = pyttsx3.init()
x='q'
while (x=='q'):
    word=input("Enter what you what to pronouns : ")
    engine.say(word)
    engine.runAndWait()
    x=input("Do You Want To Try It Then Click 'q' If No then Click 'e'")
if(x=='e'):
    print("Thank You For Testing")
    exit()
