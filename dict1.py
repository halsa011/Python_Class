

# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the g
# reatest number of mail messages. The program looks for 'From ' lines and takes the second word 
# of those lines as the person who sent the mail. The program creates a Python dictionary that maps 
# the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum 
# loop to find the most prolific committer.
#---------------------------------------------------------------------------------------------------- 
counts=dict()
maillist=list()
name=raw_input("Enter file:")
if len(name) <1 : name="mbox-short.txt"
fhand=open(name)

for line in fhand:
	if line.startswith('From '):
		words=line.split()
		maillist.append(words[1])
		#print maillist

#print maillist[1].split('@')

for ad in maillist:
	counts[ad]=counts.get(ad,0)+1

countvalue=counts.values()
countvalue.sort()
maxcount=countvalue[len(countvalue)-1]

for key in counts:
	if counts[key]==maxcount:
		print key,counts[key]
