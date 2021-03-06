import sys
import io

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='windows-1252')
for line in input_stream:
    # Setting some defaults
	emp_id = ""
	name = "-"
	salary = "-"
	country = "-"
	passcode = "-"

	line = line.strip()
	splits = line.split("\t")
	if len(splits) == 2: 
		emp_id = splits[0]
		name = splits[1]
	else:
		emp_id = splits[0]
		salary = splits[1]
		country = splits[2]
		passcode = splits[3]                   
	print (emp_id+"\t"+name+"\t"+salary+"\t"+country+"\t"+passcode)
