
largest = None
smallest = None
while True:
	input=raw_input("Enter a number: ")
	if input == "done":
		break
	try:
		num = int(input)
	except:
		print "Invalid input"
		continue
	if largest is None : largest=num
	elif num > largest: largest=num
#	print largest

	if smallest is None: smallest=num
	elif num < smallest: smallest=num
#	print smallest

print "Maximum is", largest
print "Minimum is", smallest