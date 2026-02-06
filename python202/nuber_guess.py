import  random 
# game 
random_number = random.randint(1,100) 

while True :
    try :
        your_choice = int(input("enter a number"))
    except ValueError :
        print("plz enter only digit")
        continue
    
    if your_choice > random_number :
        print("chose small number")
    elif your_choice < random_number  :
        print("chose big number")
    
    else :
        print("win")
    break          


                