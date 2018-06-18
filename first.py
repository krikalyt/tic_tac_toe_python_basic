a = [" "," "," "," "," "," "," "," "," "];
def board():
    print( a[0] + "|" + a[1] + "|" + a[2])
    print( a[3] + "|" + a[4] + "|" + a[5])
    print( a[6] + "|" + a[7] + "|" + a[8])


def user1():
   print("user 1 turn ")
   placefor1 = int (input("at which place you want to put your value\n"));
   if(placefor1>0 and placefor1<10 and a[placefor1-1]==" "):
       a[placefor1-1] = "0";
       board()
       if(a[0]=="0" and a[4]=="0" and a[8]=="0"):
           return print("User 1 won")
       elif(a[6]=="0"and a[4]=="0" and a[2] == "0"):
           return  print("user 1 won")
       elif(a[0]=="0"and a[1]=="0" and a[2] == "0"):
           return  print("user 1 won")
       elif (a[3] == "0" and a[4] == "0" and a[5] == "0"):
           return print("user 1 won")
       elif (a[6] == "0" and a[7] == "0" and a[8] == "0"):
           return print("user 1 won")
       elif (a[0] == "0" and a[3] == "0" and a[6] == "0"):
           return print("user 1 won")
       elif (a[1] == "0" and a[4] == "0" and a[7] == "0"):
           return print("user 1 won")
       elif (a[2] == "0" and a[5] == "0" and a[8] == "0"):
           return print("user 1 won")
       user2()
   else:
       print("enter valid number")
       user1()



def user2():
    print("user 2 turn")
    placefor2 = int(input("at which place you want to put your value\n"));
    if (placefor2 > 0 and placefor2 < 10 and a[placefor2-1]==" "):
        a[placefor2 - 1] = "X";
        board()
        if (a[0] == "X" and a[4] == "X" and a[8] == "X"):
            return print("User 2 won")
        elif (a[6] == "X" and a[4] == "X" and a[2] == "X"):
            return print("user 2 won")
        elif (a[0] == "X" and a[1] == "X" and a[2] == "X"):
            return print("user 2 won")
        elif (a[3] == "X" and a[4] == "X" and a[5] == "X"):
            return print("user 2 won")
        elif (a[6] == "X" and a[7] == "X" and a[8] == "X"):
            return print("user 2 won")
        elif (a[0] == "X" and a[3] == "X" and a[6] == "X"):
            return print("user 2 won")
        elif (a[1] == "X" and a[4] == "X" and a[7] == "X"):
            return print("user 2 won")
        elif (a[2] == "X" and a[5] == "X" and a[8] == "X"):
            return print("user 2 won")
        user1()
    else:
        print("enter valid number")
        user2()

board()
user1()
