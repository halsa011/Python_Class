#  Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
# Data Files

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#     Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt (There are 87 values with a sum=445822)
#     Actual data: http://python-data.dr-chuck.net/regex_sum_309101.txt (There are 96 values and the sum ends with 776)

# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis. 
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import re
fname=raw_input('Enter File name:')
fh=open(fname)
num_list=list()
n_int_list=list()
for line in fh:
	if re.search('[0-9]+',line):
		num=re.findall('[0-9]+',line)
		for n in num:
			n_float=float(n)
			num_list.append(n_float)

print sum(num_list)


