fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
words=list()
delete_list=list()

for line in fh:
	lst=line.split()
	words.extend(lst)

words.sort()

for i in range(len(words)-1):
	if words[i]== words[i+1]:
		delete_list.append(words[i])

for i in delete_list:
	words.remove(i)

print words