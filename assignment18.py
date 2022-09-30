# 1. Write a python program to create and print a dictionary which stores your information.
# (name, age, gender …..)
# 2. Write a python program to access the items of a dictionary by referring to its key
# name.
# 3. Write a python program to get a list of the values from a dictionary.
# 4. Write a python program to change the value of a specific item by referring to its key
# name.
# 5. Write a python program to print all key names in the dictionary, one by one.
# 6. Write a python program to create a dictionary that contains three dictionaries.
# (nested)
# 7. Write a python program to create three dictionaries, then create one dictionary that
# will contain the other three dictionaries.
# 8. Write a python program to convert two lists into a dictionary in a way that item from
# list1 is the key and item from list2 is the value.
# 9. Write a python program to merge two python dictionaries into one dictionary.
# 10. Write a python program to get the key of lowest value from the dictionary.
# sample_dict = {
# 'C': 92,
# 'Java': 66,
# 'Python': 85
# # }

# 1) ......................................
# dict={}
# while True:
#     ans=input("Enter your ans [y/n] : ")
#     if ans=='y' or ans=='Y':
#         for e in range(1,2):
#             value=input("Enter your data %d : "%e)
#             key=input("Enter key value %d : "%e)
#             dict[key]=value
#         print(dict,type(dict))
#     else:
#         break

# 2) ........................................
# d1={  "name":"harikesh",
#        "age":18,
#         'address':"kannauj"
#    }
# for k in d1:
#     print(d1[k])


# 3) ......................................
# d2={  "name":"harikesh",
#        "age":18,
#         'address':"kannauj"
#    }
# l2=[]    
# for e in d2:
#     l2.append(d2[e])
# print(l2)


# 4) ..................................
# d1={  "name":"harikesh",
#        "age":18,
#         'address':"kannauj"
#    }
# # ..............................
# # d1['name']='pankaj'
# # print(d1)
# # ............................
# while True:
#     a=input("Enter  [y/n] to change name and enter [m/n] to change age : ")
#     if a=='y' or a=='Y':
#         # naam=input("Enter another name to change : ")
#         d1['name']=input("Enter another name to change : ")
#         print(d1)
    
#     elif a=="m" or a=='M':
#          d1['age']=int(input("Enter another age to change : "))
#         print(d1)
        
#     elif a=="x" or a=='X':
#         new_key=input("Enter new key : ")
#         new_value=input("enter new value : ")
#         d1[new_key]=new_value
#         print(d1)
        
#     else:
#         break


# 5) .....................................
# d1={  "name":"harikesh",
#        "age":18,
#         'address':"kannauj"
#    }
# for k in d1:
#     print(k)


# 6) ..................................
# d3={  "name":"harikesh",
#        "age":18,
#         'address': {
#                         'village':"makhanahan",
#                         'post':'amari',
#                         'habbits' : {
#                                         'playing':'chess',
#                                         'coding': "Python"
#                                      }
#                     }
        
#    }

# print(d3)


# 7) ..........................................
# d4={  "name":"harikesh",
#        "age":18,
#         'address': {
#                         'village':"makhanahan",
#                         'post':'amari',
#                         'habbits' : {
#                                         'playing':'chess',
#                                         'coding': "Python"
#                                      }
#                     }
        
#    }

# d5={}
# print(type(d5))
# for e in d4:
#     print(d5[e])



# 8) .................................................
# l1=["name","Age","Gender","Adress"]
# l2=["Harikesh",18,"Male","Kannauj"]
# dic=dict(zip(l1,l2))
# print(dic)
  
# 9) ..................................................
# d1={  "name":"harikesh",
#        "age":18,
#         'address':"kannauj"
#    }
        
# d2= {
# 'C': 92,
# 'Java': 66,
# 'Python': 85
# }
# d1.update(d2)   
# print(d1)


# 10) ...............................................
# d = {
# 'C': 66,
# 'Java': 66,
# 'Python': 85
# }
# # print(min(d.values()))
# for key in d:
#     if d[key]<=min(d.values()):
#         print(d[key])
