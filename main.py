
# import json
# import random
# import string
# from pathlib import Path
# class Bank:
#     __database="data.json"
#     data=[]
#     try:
#         if Path(__database).exists():
#             with open(__database) as fs:
#                 data=json.loads(fs.read())
#     except Exception as err:
#         print(f"error occured ass{err}")        
    
#     @classmethod
#     def update_data(cls):
#         with open(cls.__database,'w') as fs:
#             json.dump(cls.data,fs)


#     @classmethod
#     def Generate_account(cls):
#         alpha = random.choices(string.ascii_letters,k=4)
#         digit = random.choices(string.digits,k=8)
#         id = alpha +digit
#         random.shuffle(id) 
#         return "".join(id)     

#     def createuser(self):
#         info={
#             "name":input("enter your name : "),
#             "email":input("enter your email : "),
#             "age":int(input("enter your age : ")),
#             "phonenumber":input("enter your phone number : "),
#             "pin":input("enter your pin : "),
#             "account" :bank.Generate_account(),
#             "balance":0
#         }
    
#         if info["age"]<18:    
#             print("your account cannot be created underage")

#         elif(len(info["phonenumber"])!=10 or len(info["pin"])!=4):
#             print("invalid input please try again")

#         else:
#             print(f"please keep youraccount number safe, your account number is {info['account']}")
#         Bank.data.append(info)
#         Bank.update_data()


#     def deposit_money(self):
#         ac = input("please enter your account number: ")
#         pin= int(input("please enter your 4 digit pin number: "))
#         # for i in bank.data:
#             # if i["account"]== ac and i["pin"]== pin:
#             #     user_data=i
#             #     break 
#         user_data= [i for i in Bank.data if i['AccountNo.']==ac and i["pin"]==pin]
#         if user_data== False:
#             print("sorry no data found for this user")
#         else:
#             amount = int(input("enter your amount : "))
#             if amount <0:
#                 print("amount is 0")
#             elif amount >10000:
#                 print("amount is greater than 10000")    
#             else:
#                 user_data[0]["balance"]+=amount
#                 print("money update succeffuly")

# bank=Bank()
# check=int(input("""press 1 for creating a new user account : 
# press 2 for creating a new user account : """))

# if check==1:
#     bank.createuser()
# if check==2:
#     bank.deposit_money()
# # ````````````````````````````````````````````````````````````````````````````````````````````
# from pathlib import Path
# import json
# import random
# import string
# class Bank:
#     __database = "data.json"
#     data = []
#     try:
#         if Path(__database).exists():
#             with open(__database) as fs:
#                 data = json.loads(fs.read())
#     except Exception as err:
#         print(f"Error occured as {err}")

#     @classmethod
#     def update_data(cls):
#         with open(cls.__database, 'w') as fs:
#             json.dump(cls.data,fs)
    
#     @classmethod
#     def Generate_account(cls):
#         alpha = random.choices(string.ascii_letters,k=4)
#         digit = random.choices(string.digits,k=8)
#         id = alpha + digit
#         random.shuffle(id)
#         return "".join(id)


#     def createuser(self):
#         info = {
#             "name": input("Enter your name: "),
#             "email": input("Enter your email: "),
#             "age": int(input("Enter your age: ")),
#             "phonenumber": int(input("Enter your phone number: ")),
#             "pin": input("Enter your pin: "),
#             "AccountNo.":Bank.Generate_account(),
#             "balance": 0
#         }

#         if info["age"] < 18:
#             print("Your account cannot be created. You are not balik...")

#         elif len(str(info["phonenumber"])) != 10 or len(info["pin"]) != 4:
#             print("Invalid input. Please try again later...")

#         else:
#             print(f"Please keep your account number safe: {info['AccountNo.']}")
#             Bank.data.append(info)
#             Bank.update_data()
    

#     def Deposite_money(self):
#         Ac = input("Please enter your account number: ")
#         pin = input("Enter your 4 digit pin: ")
#         for i in Bank.data:
#             if i["AccountNo."] == Ac and i["pin"] == pin:
#                 userdata = i
#                 break
#         user_data = [i for i in Bank.data if i["AccountNo."]==Ac and i["pin"]==pin]
#         if user_data==False:
#             print("Sorry no data found for this user")
#         else:
#             amount = int(input("Enter your amount: "))
#             if amount < 0:
#                 print("Amount is 0")
#             elif amount > 50000:
#                 print("Amount is greater than 10,000")
#             else:
#                 user_data[0]["balance"] += amount
#                 Bank.update_data()
#                 print("Money updated successfully")
#     def Withdraw_money(self):  
#         Ac = input("Please enter your account number: ")
#         pin = input("Enter your 4 digit pin: ")
#         for i in Bank.data:
#             if i["AccountNo."] == Ac and i["pin"] == pin:
#                 userdata = i
#                 break
#         user_data = [i for i in Bank.data if i['AccountNo.']==Ac and i["pin"]==pin]
#         if user_data==False:
#             print("Sorry no data found for this user")
#         else:
#             amount = int(input("Enter your amount wothdraw_money: "))
#             if amount < 0:
#                 print("Amount is 0")
#             elif amount > 10000:
#                 print("Amount is greater than 10,000")
#             else:
#                 if user_data[0]["balance"]<amount:
#                     print("insuffcient amount")
#                 else:           
#                     user_data[0]["balance"] -= amount
#                     Bank.update_data()
#                     print("Money withdraw successfully")          
#     def details(self):
#         Ac = input("enter the account number : ")
#         pin =input("enter  your pin : ")
#         user_data = [i for i in Bank.data if i['AccountNo.']==Ac and i["pin"]==pin]
#         if user_data == False:
#             print("no user found this account number.")
#         else:
#             for i in user_data[0]:
#                 print(f"{i} -> {user_data[0][i]}")
#     def update_details(self):
#         Ac = input("enter the account number : ")
#         pin =input("enter  your pin : ")
#         user_data = [i for i in Bank.data if i['AccountNo.']==Ac and i["pin"]==pin]
#         if not user_data:
#             print("no user found this account number.")
#         else:
#             print("your cannot change your account number.")
#             print("now update your details and skip it if don't want to change")
#             newdata ={
#                 "name":input("enter  your name : "),
#                 "age" :input("enter your age : "),
#                 "email":input("enter your email: "),
#                 "phonenumber":input("enter your phone number : "),
#                 "pin":input("enter your pin : ")                      
#                      } 
#             if newdata["name"]=="":
#                 newdata["name"]= user_data[0]["name"] 

#             if newdata["age"]=="":
#                 newdata["age"]= user_data[0]["age"]

#             if newdata["email"]=="":
#                 newdata["email"]= user_data[0]["email"]

#             if newdata["phonenumber"]=="":
#                 newdata["phonenumber"]= user_data[0]["phonenumber"]

#             if newdata["pin"]=="":
#                 newdata["pin"]= user_data[0]["pin"]

#             newdata['AccountNo.']=user_data[0]['AccountNo.']
#             newdata["balance"]= user_data[0]["balance"]

#             for i in user_data[0]:
#                 if user_data[0][i]==newdata[i]:
#                     continue
#                 else:
#                     if newdata[i].isnumeric():
#                         user_data[0][i]=int(newdata[i])
#                     else:
#                         user_data[0][i]=newdata[i]
#         Bank.update_data()
#         print("update successffuly")
#     def delete_user(self):
#         Ac = input("enter the account number : ")
#         pin =input("enter  your pin : ")
#         user_data = [i for i in Bank.data if i['AccountNo.']==Ac and i["pin"]==pin]
#         if not user_data:
#             print("no user found this account number.")   
#         else:
#             Bank.data.remove(user_data[0])
#             Bank.update_data()
#             print("account deleted successfuly")    
    

# bank = Bank()
# check = int(input("""
# Press 1 to create a bank account:-
# Press 2 for depositing money:-
# press 3 for withdraw money:-
# press 4 for details :- 
# press 5 for updating data :- """))

# if check == 1:
#     bank.createuser()

# if check == 2:
#     bank.Deposite_money()

# if check ==3:
#     bank.Withdraw_money()
# if check ==4:
#     bank.details()
# if check==5 :
#     bank.update_details()   

# # # ````````````````````````````````````````````````````````````````````````````````````````````
import json
import random 
import string
from pathlib import Path
class Bank:
    __database="data.json"
    data=[]
    try:
        if Path(__database).exists():
            with open(__database) as fs:
                data=json.loads(fs.read())
    except Exception as err:
        print(f"error occured as {err}")
    
    @classmethod
    def Generate_acc(cls):
        alpha=random.choices(string.ascii_letters,k=4)
        digit=random.choices(string.digits,k=8)
        id=alpha+digit
        random.shuffle(id)
        return "".join(id)
    @classmethod
    def update_data(cls):
        with open(cls.__database,'w') as fs:
            json.dump(cls.data,fs)

    def createuser(self):
        info={
            "name":input("enter your name : "),
            "email":input("enter your email : "),
            "age":int(input("enter your age : ")),
            "phonenumber":input("enter your phone number : "),
            "pin":input("enter your pin : "),
            "account" :Bank.Generate_acc(),
            "balance":0
        }
    
        if info["age"]<18:    
            print("your account cannot be created underage")

        elif(len(info["phonenumber"])!=10 or len(info["pin"])!=4):
            print("invalid input please try again")

        else:
            print(f"please keep your account number safe, your account number is {info['account']}")
            Bank.data.append(info)
            Bank.update_data()

    def deposit_money(self):
        ac=input("Enter your account number : ")
        pin=input("enter your pin : ")
        userdata=[i for i in Bank.data if i["AccountNo."]==ac and i["pin"]==pin]
        # for i in Bank.data:
        #     if i["account"]==ac and i["pin"]==pin:
        #         userdata=i
        #         break
        if not userdata:
            print("No data found for this user ")
        else:
            amount=int(input("Enter your amount : "))
            if amount<500:
                print("Amount is less than 500")
            elif amount>10000:
                print("amount is greater than 10000")
            else:
                userdata[0]["balance"]+=amount
                Bank.update_data()
                print("balance updated")

    def withdrawl_money(self):
        ac=input("Enter your account number : ")
        pin=input("enter your pin : ")
        userdata=[i for i in Bank.data if i["AccountNo."]==ac and i["pin"]==pin]
        if not userdata:
            print("No data found for this user ")
        else:
            amount=int(input("Enter your amount : "))
            if amount<500:
                print("Amount is less than 500")
            elif amount>10000:
                print("amount is greater than 10000")
            else:
                if userdata[0]["balance"]<amount:
                    print("Insufficient amount")
                else:
                    userdata[0]["balance"]-=amount
                    Bank.update_data()
                    print("money withdrawl,balance updated")

    def details(self):
        ac=input("Enter your account number : ")
        pin=input("enter your pin : ")
        userdata=[i for i in Bank.data if i["ccount"]==ac and i["pin"]==pin]
        if not userdata:
            print("No data found for this user ")
        else: 
            for i in userdata[0]:
                print(f"{i} -> {userdata[0][i]}")

    def update_user(self):
        ac=input("Enter your account number : ")
        pin=input("enter your pin : ")
        userdata=[i for i in Bank.data if i["AccountNo."]==ac and i["pin"]==pin]
        if not userdata:
            print("No data found for this user ")
        else: 
            print("you can not change your account number")
            print("now update your details and skip it if you don't want to change")
            newdata={
                "name":input("enter your name : "),
                "age":input("enter your age : "),
                "email":input("enter your email : "),
                "phonenumber":input("enter your number : "),
                "pin":input("enter your pin : ")
            }
            if newdata["name"]=="":
                newdata["name"]=userdata[0]["name"]
            if newdata["age"]=="":
                newdata["age"]=userdata[0]["age"]
            if newdata["email"]=="":
                newdata["email"]=userdata[0]["email"]
            if newdata["phonenumber"]=="":
                newdata["phonenumber"]=userdata[0]["phonenumber"]
            if newdata["pin"]=="":
                newdata["pin"]=userdata[0]["pin"]
            newdata["account"]=userdata[0]["account"]
            newdata["balance"]=userdata[0]["balance"]

            for i in userdata[0]:
                if userdata[0][i]==newdata[i]:
                    continue
                else:
                    if newdata[i].isnumeric():
                        userdata[0][i]=int(newdata[i])
                    else:
                        userdata[0][i]=newdata[i]

        Bank.update_data()
        print("Details updated successfully!!")

    def delete_user(self):
        ac=input("Enter your account number : ")
        pin=input("enter your pin : ")
        userdata=[i for i in Bank.data if i["account"]==ac and i["pin"]==pin]
        if not userdata:
            print("No data found for this user ")
        else: 
            Bank.data.remove(userdata[0])
            Bank.update_data()
            print("account deleted !!")

bank=Bank()
check=int(input("""
press 1 for creating a new user account
press 2 for depositing money
press 3 for withdrawl money
press 4 for your details
press 5 to update your details
press 6 to delete user
enter your response
"""))

if check==1:
    bank.createuser()

if check==2:
    bank.deposit_money()

if check==3:
    bank.withdrawl_money()

if check==4:
    bank.details()

if check==5:
    bank.update_user()

if check==6:
    bank.delete_user()