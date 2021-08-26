f = open("my_textFile.txt", "w")
f.write(""" 
There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"r+" - For both reading and writing, returns an error if the file does not exist
In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
""")
f.close()

f = open("my_textFile.txt", "r")
methodsFile = f.read()
splitMetods = methodsFile.split("\n")
counter = 0
for x in splitMetods:
   counter += 1
print(counter)
