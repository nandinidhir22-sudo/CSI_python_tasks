# light=input("enter the light:")
# if light=="green":
#     print("go!")
# elif light == "yellow":
#     print("stop")
# else:
#     print("wait")
# list=[]
# i=0
# while i<3:
#     list.append(input("enter movie "))
#     i+=1

# print(list)

# list1=list.copy()
# list1.reverse()
# if list1 == list:
#     print("pallindrome")
# else:
#     print("not")

# list=["C","D", "A","A","B", "B","A"]
# print(list.sort())

# dict= {
#     "name":"nandini",
#     "class":"good",
#     "dictionsry":{
#         "sports":True,
#         "food":True,
#         "else":False
#     }
# }
# print(dict["name"])
# print(dict["class"])
# print(dict["dictionsry"])
# print(dict["dictionsry"]["food"])

# set={1,2,3,4,5}
# print(set)
# print(type(set))

#empty set:
# set1= {1,2,3,4,5}
# set2={9,7,5,2,1,4,6,9,0}
# print(set1.union(set2))
# print(set1.intersection(set2))

# tup= (1,2,3,4,4,5,6,7,8,9,5,3,12,1,3,6,56,87,98,2434,7,4,23,212)
# x=2434
# i=0
# for el in tup:
#     if (el==x):
#         print("found at",i)
#     i+=1     

# for i in range(2,20,2) :
#     print(i)  

# num=5
# sum=0
# for i in  range(1,num+1):
#     sum=sum+i
# print(sum)

# num=5
# fac=1
# for i in  range(1,num+1):
#     fac=fac*i
# print(fac)

# def sum(a,b):
#     s=a+b
#     return s
# print(sum(3,4))

# def show(n):
#     if n==0:
#         return
#     else:
#         print(n)
#         show(n-1)
# show(5)

# class Student:
#     name= "nandini"
# s1=Student()
# print(s1.name)

# class cars:
#     color="blue"
#     model="e class"
#     branc="merc"
# car1=cars()
# print(car1.branc)

# class student:
#     name="nandini"
#     section="it-2"
#     def __init__(self):
#         print(self)
#         print("adding new student to database...")
# s1=student()

# class student:
#     college_name="akg"
#     def __init__(self, fullname,surname,marks):
#         self.name=fullname+surname
#         self.marks=marks
#     @staticmethod
#     def hello():
#         print("welcome!")

#     def get_marks(self):
#         return self.marks

# s1=student("nandini","dhir",98)
# print(s1.college_name)
# print(s1.marks)
# print(s1.name)
# print(s1.hello())
# print(s1.get_marks())

# class car:
#     def __init__(self):
#         self.accelerator = False
#         self.breakk = False
#         self.clutch = False
#     def start(self):
#         self.accelerator = True
#         self.breakk = False
#         self.clutch = True
#         print("car started")

# car1=car()
# car1.start()

class Account:
    def __init__(self,balance,acc_num):
        self.balance= balance
        self.acc_num=acc_num
    def debit(self,debamount):
        self.balance= self.balance-debamount
       # print("after debit",self.balance)
        print("after debit",self.get_bal())
    def credit(self,credamount):
        self.balance=self.balance+credamount
        #print("after credit",self.balance)
        print("after credit",self.get_bal())
    def  get_bal(self):
        return self.balance
        #print("balance=",self.balance)

acc1= Account(10000,12345)
print(acc1.balance)
print(acc1.acc_num)
acc1.debit(1000)
acc1.credit(3000)