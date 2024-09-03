#Video game inventory list 
import os,time
list = []

try:
  f=open("list.txt","a")
  f=open("list.txt","r")
  list = eval(f.read())
  f.close()

except:
  pass

def add():
  time.sleep(2)
  os.system("clear")
  print("Game Inventory list")
  print()
  item = input("input the item to add : > ").upper()
  list.append(item)
  print(item, "has been added to your inventory list")

def view():
  time.sleep(4)
  os.system("clear")
  print("Game inventory list ")
  print()
  view_list = []
  for item in list:
    if item not in view_list :
       print(f"{item}{list.count(item)}")
       view_list.append(item)


       #print("You have", item)
  time.sleep(2)

def remove():
  time.sleep(2)
  os.system("clear")
  print("Game Inventory list ")
  print()
  item =input("Iput the item to remove: > ")
  if item in list:
    list.remove(item)
    print(item, "has been removed")
  else:
    print("Cant find item to remove")

while True:
  time.sleep(2)
  os.system("clear")
  print("Game Inventory list ")
  print()
  menu = input("1. Add \n 2. View \n 3.Remove > ")
  if menu == "1":
    add()
  elif menu == "2":
    #menu == "2":
    view()
  else:
    remove()

  f = open("list.txt", "w")
  f.write(str(list))
  f.close()


