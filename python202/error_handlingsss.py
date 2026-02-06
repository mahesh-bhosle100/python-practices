# error  handlong
"""
syntax error 
exception error"""

#index  error

'''invalid index'''
# l = [1,2,3]
# print(l[10])

#  key error

# d = {"name" :"mahesh" , "age" :23}
# print(d["namee"])

# type error

# print(1+"2")



# value eroor

# print(int("a"))

# name error

# print(k)

# attribute  error  
# l = [1,2,3]
# print(l.upper())

# modulenotfound error

# import mathii
# print(math.sq(10))


# try :
#   print(int("a"))
# except :
#   print("sorry  not covert this ")  



try :
    with open("aa.txt" ,"r")as f:
        print(f.read())
    print("m")
    print(10/1)
    l = [1,2,3]
    print(l[100])
except FileNotFoundError :
    print("file not found  ")    
except NameError :
    print("variable  not define")
except ZeroDivisionError :
    print("not  divide  by zero  bhai ")       
except Exception as  e :
    print(e)     
    
    
    
''' specipic and generic  yad rakhna  
specipal  upper  dena  nad  
generic niche dena bhai  '''    

# else  
try :
    a = "mahesh"
    b = 10/1
except NameError: 
    print("name nahi ")   
except Exception:
    print("kuch to lafda hai")     
else :
    print(a)    
    
    
    
    
# finally     


try :
    a = "mahesh"
    b = 10/1
except NameError: 
    print("name nahi ")   
except Exception:
    print("kuch to lafda hai")     
else :
    print(a)    
    
finally :
    print("mai to kabhi bhi run ho sakta hu bhai  chaye  kuch bhi hio")
    
    

# raise  kar saktu  error  kuch  bhi 



# try :
#     print(fweefwfwe)
# except NameError :
#     print("nooooooooooooooooooooooo")     
# raise NameError("not  found")   
    
    
    
    
# class Bank :
#     def __init__(self ,balance):
#         self.balance  =balance
    
    
#     def withdraw(self,amount) :
#         if  amount < 0 :
#             raise Exception ("amount -ve nahi hota hai")
#         if  self.balance < amount :
#             raise Exception("paise nahi hai")
         
#         self.balance = self.balance -amount

# obj = Bank(1000)        
# try :
#     obj.withdraw(-9)
# except Exception as e :
#     print(e)
# else :
#     print(obj.balance)        
    
    
    
class SecurityError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def logout(self):
        print("log out")


class Git:
    def __init__ (self, name, email, password, device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self,  email, password, device):
        if device != self.device:
            raise SecurityError("lag gaya")

        if email ==  self.email and  password == self.password:
            print("welcome")
        else:
            print("login error")


obj = Git("mahesh", "mahesh111@gmail.com", "1234", "android")


try :
    obj.login("mahesh111@gmail.com", "1234", "windows")
except SecurityError as e:
    print(e)        
else :
    print(obj.name)

print ("done")