#Write a Python program to remove an empty tuple(s) from a list of tuples.
#Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
ls=[(), (), ('',)]
l=[]
for i in ls:
	if len(i)!=0:
	  l.append(i)
print(l)
