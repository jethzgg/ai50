from nim import train, play

ai = train(10000)
play(ai)
while True:
    again = str(input("Again? (Yes or No) "))
    again = again.replace(" ","")
    again = again.upper()
    if again != "YES" and again != "NO":
        print("Yes or No !")
        again = str(input("Again? (Yes or No) "))
        again = again.rstrip()
        again = again.upper()
    else: 
        if again == "NO": break
        else: play(ai)

        

    
    
