import os,sys

comment ={
	'.m': "%",
	'.c': "//",
	'.cpp': "//",
	'.py': "#"
	}


def sign(filename):
	sign_file = open("signature.txt",'r')
	name,ext = os.path.splitext(filename)
	print ext

	if ext not in comment.keys() or (name=="sign" and ext==".py") or "ext"==".txt":
		print "Cannot comment file: " + filename + " .\nFile not in database.\n"
		return

	file_in = open(filename,'r')
	code = ""

	for i in sign_file.readlines():
		code+=comment[ext] + i 
	
	code+="\n"

	for i in file_in.readlines():
		code += i 

	file_out = open(filename,'w')
	file_out.write(code)

	print "Signed file: " + filename +" ."


def walk(dir):

	for file in [file for file in os.listdir(dir) if not file in [".",".."]]:
		filepath = os.path.join(dir,file)
		if os.path.isdir(filepath):
			walk(filepath)
		else:
			sign(filepath)


if __name__ == "__main__":

	sign_out = open("signature.txt",'w')

	print("Enter signature (End with ';' on a new line):\n\n")

	sentinel = ";"
	sign_txt = '\n'.join(iter(raw_input,sentinel))
	print sign_txt
	sign_out.write(sign_txt)
	sign_out.close()
	
	dir = os.path.dirname(os.path.realpath(__file__))
	
	walk(dir)