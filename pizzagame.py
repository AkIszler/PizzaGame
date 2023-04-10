import time
#no reason for class, just practing using them. may use it later to expand on the game
class foodClass: # class for talking to user
    #get class set
    print("Welcome to the food value game!")
    #grab their fav food with the variable "their"
    their = input("what is your favorite food? ")
    print("interesting........")
    print("let me think")
    #do a stupid wait for lulz
    print("...")
    time.sleep(1)
    print("fine...")

    good_list = ["pasta", "chocolate", "burger", "steak", "pizza"]
    bad_list = ["apple", "oranges", "veggies", "soy",]

    if their in good_list:
        print ("Alright! %s is amazing!!!" % their)
    elif their in bad_list:
        print ("%s is bad, but I guess you're being healthy" % their)
    else:
        print ("I guess %s is okay" % their)
    more = "yes"
    while more == "yes":    
        more = input("Would you like to pick another food? yes or no: ")
        if more == "yes":
            print("perfect")
            their2 = input("what foods? ")
            print("interesting........")
            print("let me think")
            time.sleep(2)
            
            if their2 in good_list:
                print ("Alright! %s is amazing!!!" % their2)
            elif their2 in bad_list:
                print ("%s is bad, but I guess you're being healthy" % their2)
            else:
                print ("I guess %s is okay" % their2)

            print("...")
            print("so, do you believe me?")
            yes = True
            while yes == True:
                asnwer = input("y/n?: ")

                if asnwer == "y":
                    print("well thats just silly, im a computer")
                    break
                elif asnwer == "n":
                    print("well, good I wouldnt know, as i am a computer")
                    break
                elif asnwer != "y" or asnwer!= "n":
                    print("well, you dont know how to answer a question")
                    
    else: print("thanks for playing")
    more = "no"    
         
         



    