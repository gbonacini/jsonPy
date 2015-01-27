import jsonPy
import time
import subprocess

t0=time.time()
t1=0
t2=0

command="python ./genJunitReport.py -nUtilsClass -d'"

junit='test2BaseLibrary|Open%'

if ( jsonPy.open("./jsons/booleans.json") <= 0):
	print "Parsing input file: failed."
	t2=time.time()
	junit+=str(t2-t0)
	t1=t0
	junit+='@Invalid file'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(-1)

t2=time.time()
junit+=str(t2-t0)
t1=t0
junit+='|test2BaseLibrary|isValid1%'

if ( not jsonPy.isValid("root.status")):
	# This element exists
	print "Check element existance #1: failed."
	t2=time.time()
	junit+=str(t2-t1)
	t1=t2
	junit+='@Invalid url'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(-1)

t2=time.time()
junit+=str(t2-t1)
t1=t2
junit+='|test2BaseLibrary|isValid2%'

if ( jsonPy.isValid("root.xxxxx")):
	# This element doesn't exist
	print "Check element existance #2: failed."
	t2=time.time()
	junit+=str(t2-t1)
	t1=t2
	junit+='@Invalid url'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(-1)

t2=time.time()
junit+=str(t2-t1)
t1=t2
junit+='|test2BaseLibrary|isBoolean-getValue1%'

if ( not jsonPy.isBoolean("root.status")):
	# This element is a boolean
	print "Check element type #1: failed."
	t2=time.time()
	junit+=str(t2-t1)
	t1=t2
	junit+='@Invalid url'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(-1)
else:
	if(jsonPy.getBoolValueByPath("root.status")):
		# This element is a boolean with value false
		print "Check element bool value #1: failed."
		t2=time.time()
		junit+=str(t2-t1)
		t1=t2
		junit+='@Unexpected value'
		command+=junit + "' -o. -t" + str(t1-t0)
		subprocess.call(command, shell=True)  
		exit(-1)

t2=time.time()
junit+=str(t2-t1)
t1=t2
junit+='|test2BaseLibrary|isBoolean-getValue1%'

if ( not jsonPy.isBoolean("root.flag")):
        # This element is a boolean
        print "Check element type #2: failed."
	t2=time.time()
	junit+=str(t2-t1)
	t1=t2
	junit+='@Unexpected type'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
        exit(-1)
else:
	if(not jsonPy.getBoolValueByPath("root.flag")):
		# This element is a boolean with value true
		print "Check element bool value #2: failed."
		t2=time.time()
		junit+=str(t2-t1)
		t1=t2
		junit+='@Unexpected value'
		command+=junit + "' -o. -t" + str(t1-t0)
		subprocess.call(command, shell=True)  
		exit(-1)

t2=time.time()
junit+=str(t2-t1)
t1=t2
junit+='|test2BaseLibrary|isString1%'

if ( jsonPy.isString("root.status")):
	# This element is a boolean
	print "Check element type #2: failed."
	t2=time.time()
	junit+=str(t2-t1)
	t1=t2
	junit+='@Unexpected type'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(-1)

t2=time.time()
junit+=str(t2-t1)
t1=t2
junit+='|test2BaseLibrary|isNumber-getValue1%'

if ( not jsonPy.isNumber("root.postalCode")):
	# This element is a number
	print "Check element type #3: failed."
	t2=time.time()
	junit+=str(t2-t1)
	t1=t2
	junit+='@Unexpected type'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(-1)
else:
	if( int(jsonPy.getNumericValueByPath("root.postalCode")) != 10021):
		# This element is a number
		print "Numeric element extraction #1: failed."
		t2=time.time()
		junit+=str(t2-t1)
		t1=t2
		junit+='@Unexpected value'
		command+=junit + "' -o. -t" + str(t1-t0)
		subprocess.call(command, shell=True)  
		exit(-1)

t2=time.time()
junit+=str(t2-t1)
t1=t2
junit+='|test2BaseLibrary|isString-getValue2%'

if ( not jsonPy.isString("root.message")):
	# This element is a string
	print "Check element type #4: failed."
	t2=time.time()
	junit+=str(t2-t1)
	t1=t2
	junit+='@Unexpected type'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(-1)
else:
	if( jsonPy.getStringValueByPath("root.message") != "hello"):
		# This element is a string
		print "String element extraction #1: failed."
		t2=time.time()
		junit+=str(t2-t1)
		t1=t2
		junit+='@Unexpected value'
		command+=junit + "' -o. -t" + str(t1-t0)
		subprocess.call(command, shell=True)  
		exit(-1)

t2=time.time()
junit+=str(t2-t0)
junit+='|'

command+=junit + "' -o. -t" + str(t2-t0)
subprocess.call(command, shell=True)  
print "Test2: pass"
exit(0)
