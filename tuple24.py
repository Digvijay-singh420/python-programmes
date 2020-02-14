#Write a Python program to count the elements in a list until an element is a tuple
t1=(1,2,3,5)
t2=(2,3,5,0)
t3=list(t1)
t4=list(t2)
t5=[]
for i in t3:
 for j in t4:
  if i==j:
   t5.append(i)
t6=tuple(t5)
print(t6)
