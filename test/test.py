import jsonPy
import time
import subprocess

t0=time.time()
t1=0
t2=0

command="python ./genJunitReport.py -nBaseClass -d'"
junit='test1BaseTest|Open%'

try:
	jsonPy.open("./jsons/sample.null.json")
except:
	t1=time.time()
	junit+=str(t1-t0)
	junit+='@Invalid Input File'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	print "Parsing input file: failed."
	exit(-1)
else:
	t1=time.time()
	junit+=str(t1-t0)

junit+='|test1BaseTest|Get%'

try:
	if ( jsonPy.getStringValueByPath("root.menu.title") != 'SVG Viewer'):
		print "String value extraction #1: failed."
		t2=time.time()
		junit+=str(t2-t1)
		junit+='@Unexpected Value'
		print "Match element: failed."
		command+=junit + "' -o. -t" + str(t1-t0)
		subprocess.call(command, shell=True)  
		exit(-1)
except:
	t2=time.time()
	junit+=str(t2-t1)
	junit+='@Invalid json url'
	print "Get element: failed."
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(-1)
else:
	t2=time.time()
	junit+=str(t2-t1)
	junit+='|'

command+=junit + "' -o. -t" + str(t2-t0)
subprocess.call(command, shell=True)  
print "Test1: pass"
exit(0)
