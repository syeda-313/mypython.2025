# -*- coding: utf-8 -*-
"""day 4 python .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NjLdPMtl3Uy9G9AzQAPOL2IvbgrHCfyJ
"""

# list
syeda = [ 1.2,1.3,1.4,1.5]
syeda

#accesing items
print(syeda[3])

# modifying
syeda [2]=3
print(syeda)

syeda [3]=2
print(syeda)

#append
syeda.append(3)
syeda

# insert
syeda. insert(2,3.5)
syeda

#remove
syeda.remove(2)
syeda

syeda . remove(3.5)
syeda

# pop
syeda .pop(2)
syeda

# length
len(syeda)

# sort
syeda = [ 1.2,1.3,1.4]
syeda.sort()
print(syeda)

# sort
syeda = [ 2.3,2.4,1.2,1.4]
syeda.sort()
print(syeda)

# reverse
syeda=[2.3,1.3,1.4,1.4]
syeda.reverse()
print(syeda)

# iteration
for i in syeda:
   print(i)

# tuple
vijayapur = ( 1.2,1.3,1.4)
vijayapur

mountain=(1,3,4,5)
print(mountain)

# dictionary
b = {
    "name": "banana",
    "age": "10",
    " height": 5.6
}
print(b)

print(b["name"])

# modifying
b["syeda"]="name"
print(b)

#list creation

name = [1.2,3,4,5]
print(name)

# accesing
print(name[0])

print (name[3])

print(name[2])

# create a list and add an element at the end and another at a  specific index
name=[1,2,3,4]
print(name)
name.append (3)
print(name)
name. insert(2,3)
print(name)

# list removal
name . remove(3)
print(name)

# list removal using pop
numbers=[1,2,3,2]
numbers.pop(2)
print(numbers)

# list sorting
name=[6,1,4,5]
name. sort()
print(name)



# list reversal
name=[2,5,6,8]
name.reverse()
print(name)

# sum of list elements
numbers=[1,2,3,4]
print (sum(numbers))

# maximum and minimum function
ball=[2,4,6,8,10,12]
print(max(ball))
print(min(ball))

# count occurences
mountain = [1,2,2,3,4]
print(mountain. count(2))

# tuple creation and access by using indexing
ocean =( 1,2,3,4,5)
print(ocean)
print(ocean[2])

# dictionary creation
ocean = {
    "name": "indianocean",
    "depth":"5000",
    "colour": "blue"

}
print(ocean)

# accesing dictionary value by using key value
ocean={
    "name": "indianocean",
    "depth": "5000",
    "colour" :"blue"
}
for key, value in ocean. items():
  print(f"indianocean,blue")

# updating  elements from dictionary
asima = {
    "age": "27",
    "height":"5.6"

}
asima["age"]= "30"
asima["height"]= "5.6"
print(asima)

# addding elements from dictionary
asima = {
    "age": "27",
    "height":"5.6"

}
asima["age"]= "27"
asima["height"]= "5.6"
asima["hoppy"]= "hockey"
print(asima)

# iterating through a dictionary
ocean = {
   "name": "indianocean",
   "depth":"5000",
   "colour" : "blue"
   }
for key,value in ocean . items():
    print(key , value)

#removing elements from dictionary
ocean = {
   "name": "indianocean",
   "depth":"5000",
   "colour" : "blue"
   }
del ocean["colour"]
print(ocean)

# tuple unpacking

emotions=("happy","sad","angry")
happy , sad, angry= emotions
print(happy)
print(sad)
print(angry)

#merging list
list1=[1,3,2]
list2 =[4,5,6]
merged_list=list1+list2
print(merged_list)

# tuple to list ,list to tuple
phylum =[" plathyhelmintes","aschehelmintes","hydrozoa","arthopoda"]
phylum = tuple(phylum)
print(phylum)
phylum =( "plathyhelmintes","aschehelmintes","hydrozoa","arthopoda")
phylum = list(phylum)
print(phylum)

# tuple concatenation
laksdweep=(1,2,3)
misoram=(4,5,6)
laksdweepmisoram = laksdweep+misoram
print(laksdweepmisoram)

# merging two dictionaries
famous_person1={
    "name":"APJ abdul kalam",
    "profession": "president",
}
famous_person2 = {
    "name": "kohli",
    "profession": "cricketer",
}
famous_person1.update(famous_person2)
print(famous_person1,famous_person2)

# to check if a key exists or not in dictionary
asima = {
    "hobby":"hockey",
    "skin colour": "fair",
    "emotions":"angryness"
}
if "emotions" in asima:
  print("key  emotions exists")
else:
  print("key emotions does not exists")

# set creation and operation
a={1,2,3,4}
b={2,4,6,7}
a|b

a={1,2,3,4}
b={2,4,6,7}
a&b

a={1,2,3,4}
b={5,6,7,8}
b-a

# add and remove elements from sets
ball ={1,4,6,3,4,}
ball.add(4)
print(ball)
ball.remove(4)
print(ball)

# find common elements in two sets
a={1,3,4,5,6}
b= {2,3,5,6,7}
a&b

# converts list to set
my_list= [1,2,3,4,5]
my_list= set(my_list)
print(my_list)