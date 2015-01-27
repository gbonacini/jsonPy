import sys
import os
import getopt
import datetime
import time
import re

def usage():
	print("Usage:\n")
	print(" [-n <test_class_name> -d <test_results> -o <output_directory> | -t <elapsed_time> ] | [ -h ]\n")
	print(" * test_result is a string formatted as: '<test_class>|<unit_test>%<unit_test_time>[@erro_description]")
	print(" * elapsed_time is specified in seconds + fractions of seconds\n")
	print("Example:\n")
	print("python genJunitReport.py -nCLASS -d'testJsonAddr|Integrity Path Test%10.1@DivisionByZero|' -o. -t100\n")
        sys.exit(-1)

try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:d:o:t:h', ['nameOfTestClass=', 'resultDescription=', 'outputDirectory=', 'elapsedTime=', 'help'])
except getopt.GetoptError:
    usage()

if(len(opts) == 0):
    usage()
	
testClass = ''
resultDesciption = ''
outputDirectory = ''
elapsedTime = '0.0'
for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
    elif opt in ('-n', '--nameOfTestClass'):
        testClass = arg
    elif opt in ('-d', '--resultDescription'):
        resultDesciption = arg
    elif opt in ('-o', '--outputDirectory'):
        outputDirectory = arg
    elif opt in ('-t', '--elapsedTime'):
        elapsedTime = arg
    else:
        usage()

if(not os.path.isdir(outputDirectory)):
	print("Wrong Path.") 
	sys.exit(-1)
if( testClass == '' or resultDesciption == '' or outputDirectory == ''):
	usage()
	
timeStamp = datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%dT%H:%M:%S')
fileName = outputDirectory + "/" + testClass + ".xml"

oFile = open(fileName, "w")

nerr = len(re.findall('@', resultDesciption))
ntest = 0
tests = {}
temp = resultDesciption.split('|')
if(len(temp) >= 2):
	for i in range(0, len(temp)-1, 2):
		tests[temp[i]] = temp[i+1]
		ntest += 1 

compilerString = (os.popen("$(which cc) -v 2>&1").read()).replace("\n", " ")

template = ''

template += "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
template += " <testsuites disabled=\"0\" errors=\"%d\" failures=\"%d\" name=\"%s\" tests=\"%d\" time=\"%s\">\n" % (nerr, nerr, testClass, ntest, elapsedTime)
template += "  <testsuite name=\"%s\" errors=\"%d\" tests=\"%d\" failures=\"%d\" time=\"%s\" timestamp=\"%s\">\n" % (testClass, nerr, ntest, nerr, elapsedTime,  timeStamp)
template += "   <properties>\n"
template += "     <property name=\"cc.vendor\" value=\"%s\"/>\n" % ( compilerString if compilerString else 'Not available')
template += "     <property name=\"compiler.debug\" value=\"on\"/>\n"
template += "   </properties>\n"
for tst in (tests.keys()): 
#	die ("Message Wrong Format") if(tests{tst} !~ /[%]/ or tests{tst} =~ /[@].*[%]/ or tst =~ /[@%]/ 
	descriptions = re.split(r'[@%]', tests[tst])
	partialtime = descriptions[1] if len(descriptions)>=2 else 0
	template += "   <testcase classname=\"%s\" name=\"%s\" time=\"%s\">\n" % (tst, descriptions[0], partialtime) 
	if(len(descriptions)>=3):
		template += "     <failure message=\"%s failure\">%s</failure>\n" % (tst, descriptions[2])
	template += "   </testcase>\n"
template += " </testsuite>\n"
template += "</testsuites>"

oFile.write(template)

oFile.close()

