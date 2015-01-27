import jsonPy
import time
import subprocess

errorString=''
t0=time.time()
t1=0

command="python ./genJunitReport.py -nExceptionClass -d'"
junit='test4BaseTest|exception%'

try:
        jsonPy.open("./jsons/sample.null.json")
	jsonPy.getStringValueByPath("xxxroot.menu.title")
except jsonPy.JsonPyError,e:
	errorString=(e.args)[0]

t1=time.time()
junit+=str(t1-t0)
if(errorString=="Invalid Json node"):
	print("Test4: pass")
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(0)
else:
	print("Test4: fail")
	junit+='@Unexpected result'
	command+=junit + "' -o. -t" + str(t1-t0)
	subprocess.call(command, shell=True)  
	exit(-1)

