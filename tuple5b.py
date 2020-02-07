t=()

while 1 :
	item=input('Enter the item')
	t=t+(item,)
	c=input('do you want continue y/n')
	if c.lower()=='n':
		break
print(t)
