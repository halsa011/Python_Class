largest=None
smallest=None
# num=float(rawinput("Enter a number"))

for value in [9,41,12,3]:
	if smallest is None:
		smallest=value
	elif value< smallest:
		smallest=value

print smallest