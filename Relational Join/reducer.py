import sys
import io
 
prev_emp_id = None
prev_name = None
prev_salary = None
prev_country = None
prev_passcode =None


input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='windows-1252')
for line in input_stream:
    line = line.strip()
 
    emp_id,name,salary,country,passcode = line.split('\t')

    if prev_emp_id == emp_id:
    	if name != '-':
    		print (emp_id+"\t"+name+"\t"+prev_salary+"\t"+prev_country+"\t"+prev_passcode)
    	else:
    		print (emp_id+"\t"+prev_name+"\t"+salary+"\t"+country+"\t"+passcode)
    else:
    	prev_emp_id= emp_id
    	prev_name = name
    	prev_salary = salary
    	prev_country = country
    	prev_passcode = passcode