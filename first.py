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

def show(n):
    if n==0:
        return
    else:
        print(n)
        show(n-1)

show(5)