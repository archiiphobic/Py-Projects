item_name= ["apple","orange","diary","pen","bread"]
item_prices= [1.0, 2.50, 3.00, 4.50, 5.00]
item_stock= [100, 20, 50, 10, 40]
ans= True
password= "Archie@123"
while ans== True:
  print("WHAT DO YOU WANT TO DO? :")
  print("1. View Inventory [ENTER 1]" )
  print("2. Purchase Item [ENTER 2]")
  print("3. Restock Item [ENTER 3]")
  print("4. Exit [ENTER 4]")
  print("5. RESET PASSWORD [ENTER 5]")
  instruction= int(input("ENTER YOUR COMMAND:"))
  if instruction== 1:
    epass = input("Enter password to see inventory:") 
    if epass==password:
        print("Item", "-"*21 , "item_price", "-"*15 , "item_stock", "-"*15)
        l= len(item_name)
        for i in range(l):
            if item_stock[i]<5:
                warning="[LOW STOCK!!]"
            else:
                warning=""
            print(item_name[i],warning, " "*(25-(len(item_name[i])+len(warning))), item_prices[i], " "*(25- len(str(item_prices[i]))), item_stock[i], " "*(25- len(str(item_stock))))
    else:
        print("WRONG PASSWORD ENTERED!!")
  elif instruction== 2:
    item= input("Enter name of item:")
    stock= int(input("Enter quantity:"))
    if item not in item_name:
       print("THIS ITEM IS NOT IN THE INVENTORY.")
    else:
       i= item_name.index(item)
       if stock> item_stock[i]:
        print("Error: Not enough stock in inventory")
       else:
        total = (stock*item_prices[i])
        item_stock[i]= item_stock[i]-stock 
        print("Your total is:",total)
  elif instruction== 3:
    epass= input("Enter password to restock items:")
    if epass== password:
        print("RESTOCKING ITEMS IN THE INVENTORY")
        it= input("Enter item to be restocked:")
        st= int(input("Enter number of items adding to inventory:"))
        if it in item_name:
            ind= item_name.index(it)
            item_stock[ind] += st 
        else:
            item_name.append(it)
            item_stock.append(st)
            p= float(input("Enter price of new item:"))
            item_prices.append(p)
    else:
       print("WRONG PASSWORD ENTERED!!!")
  elif instruction== 4:
    ans= False 
  elif instruction== 5:
    og= input("Enter og password: ")
    if og== password:
       print("PASSWORD MUST HAVE: 8 characters(min), uppercase letters, lowercase letters, special characters and digits")
       new= input("Enter new password:")
       lp= len(new)
       u=0
       s=0
       sc=0
       d=0
       for x in new:
          if x.isupper():
            u+=1
          elif x.islower():
             s+=1
          elif x in ['!','@','#','$','%','^','&','*','-','_','~','/']:
             sc+=1
          elif x in ['0','1','2','3','4','5','6','7','8','9']: 
             d+=1
          else:
             print("YOU ENTERED AN INVALID CHARACTER> PLEASE TRY AGAIN.") 
       if u==0 or s==0 or sc==0 or d==0:
          print("GIVEN PASSWORD DOESN'T QUALIFY> PLEASE TRY AGAIN")
       else:
          password= new      
    else:
       print("WRONG PASSWORD ENTERED!!!") 
  else:
    print("WRONG COMMAND ENTERED!")




    

