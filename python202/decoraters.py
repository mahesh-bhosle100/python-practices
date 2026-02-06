# import time 

# def timer(func) :
#     def wrap() :
#         start = time.time()
#         func()
#         end = time.time()
#         h = start-end
#         print("time taken", func.__name__ ,h)
#     return wrap    
# @ timer
# def  show() :
#     for i in range (10000):
#         print("hello mahesh")  
#         time.sleep(1)
# show()              






# import time 

# def timer(func) :
#     def wrap(*args) :
#         start = time.time()
#         func(*args)
#         end = time.time()
#         h = start-end
#         print("time taken", func.__name__ ,h)
#     return wrap    
# @ timer
# def  show(a) :
#     for i in range (10000):
#         print("hello mahesh" ,i)  
#         time.sleep(1)
# show(1)              





def check(data_type) :
    def wrap(func) :
        def inner_wrap(*args) :
            if type(*args) == data_type:
                func(*args)
            else :
                raise TypeError("ye nahi chalega")
        return inner_wrap
    return wrap
     
        
        

@check(int)
def sq(num) :
    print(num**2)
sq(1)    