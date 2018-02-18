fname=raw_input("Enter File name:")
fh=open(fname)
for line in fh:
	print line.rstrip().upper()