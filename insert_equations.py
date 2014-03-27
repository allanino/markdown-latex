import urllib2
import re
import sys

RENDERER_URL = "http://latex.codecogs.com/png.latex"

def percent_encode(match):
	return "![equation](" + RENDERER_URL + "?" + urllib2.quote(match.group().encode("utf-8")) + ")"

def replace_equations(s):
	return re.sub("\$\$(.*?)\$\$", percent_encode, s)

if __name__ == "__main__":
		# If no argument passed, encode README in the current directory
		if len(sys.argv) == 1:
			filename = "README"
			try:
				in_file = open(filename, "r")
			except:
				print "README not found."
				sys.exit(0)

		# If argument passed, see if it is README, then open file
		if len(sys.argv) == 2:
			filename = sys.argv[1]
			try:
				in_file = open(filename, "r")
			except:
				print "File not found."
				sys.exit(0)		

		# Read README content, encode equatins and save to REAMD.md in the same folder
		text = in_file.read()
		in_file.close()
		out_text = replace_equations(text)
		out_file = open(filename+".md", "w")
		out_file.write(out_text)
