print("Welcome to Hunter x Hunter challenge")
start = input("Are you ready to take this challenge? Y or N\n")
if start == "Y":
    print("Let's start")
    print("You are hunting for a legendary treasure in the mountains of Hunter x Hunter")
    print("You have to fight monsters and collect treasures")
    des = input("Where do yo want to go left or right? type left or right\n")
    des.lower()
    if des == "left":
      des1 = input("You have reached a river, do you want to swim or wait? type swim or wait\n")
      des1.lower()
      if des1 == "wait":
        des2 = input("Now you have reached the doors. Which door do you wanna pick? Red, Blue or Yellow\n")
        des2.lower()
        if des2 == "yelllow":
          print("You have reached the treasure")
        else:
          print("Gameover")
          exit()
      else:
        print("Gameover")
        exit()
    else:
      print("Gameover")  
      exit()

else:
  print("Goodbye Loser")
  exit()