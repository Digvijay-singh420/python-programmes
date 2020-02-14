#Write a Python program to replace last value of tuples in a list.
l=[(10,20,30),(40,50,60),(60,70,80)]
print([i[:-1]+(100,)for i in l])
