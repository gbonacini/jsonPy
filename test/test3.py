import jsonPy
import time
import subprocess

t0=time.time()
t1=0
t2=0

command="python ./genJunitReport.py -nValueClass -d'"

junit='test3BaseLibrary|getValueException%'

try:
	jsonPy.open("./jsons/sample.null.json")
	jsonPy.getStringValueByPath("root.menu.xxxxxxxtitle")
except:
	print "Test3 - jsonPy.getStringValueByPath exception: pass"
	t2=time.time()
	junit+=str(t2-t0)
	t1=t0
else:
	print "Test3: fail"
	t2=time.time()
	junit+=str(t2-t0)
	t1=t0
	junit+='@Exception Expected'
	command+=junit + "' -o. -t" + str(t1-t0)
	exit(-1)

t2=time.time()
junit+=str(t2-t1)
t1=t2
junit+='|test3BaseLibrary|OpenException%'

try:
	jsonPy.open("./jsons/xxxxsample.null.json")
except:
	print "Test3 - jsonPy.open exception: pass"
else:
	print "Test3: fail"
	t2=time.time()
	junit+=str(t2-t1)
	junit+='@Exception Expected'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(-1)

t2=time.time()
junit+=str(t2-t0)
junit+='|'

command+=junit + "' -o. -t" + str(t2-t0)
subprocess.call(command, shell=True)  

exit(0)

