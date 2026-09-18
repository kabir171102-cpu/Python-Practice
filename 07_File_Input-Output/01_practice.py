# ====================================================================================
# Question 1- Create a file named student.txt and write.
# ====================================================================================

f = open("student.txt", "w")
f.write("Aman\nPython\nAI Engineer")
f.close()

# ====================================================================================
# Question 2- Read the entire contents of student.txt and print them.
# ====================================================================================

f = open("student.txt", "r")
data = f.read()
print(data)
f.close()

# ====================================================================================
# Question 3- Read only the first line of student.txt.
# ====================================================================================

f = open("student.txt", "r")
data = f.readline()
print(data)
f.close()

# ====================================================================================
# Question 4- Append the text: (GitHub)
# ====================================================================================

f = open("student.txt", "a")
f.write("\nGitHub")
f.close()

# ====================================================================================
# Question 5- Overwrite the entire file with:  "Machine Learning"
# ====================================================================================

f = open("student.txt", "w+")
f.write("Machine Learning")
f.close()

# ====================================================================================
# Question 6- Create a new file named marks.txt and write five marks,one on each line.
# ====================================================================================

# num = "90\n85\n78\n88\n95"
f = open("marks.txt", "w")
f.write("90\n85\n78\n88\n95")   # or-  f.write(num)
f.close()

# ====================================================================================
# Question 7- Read marks.txt and print all its contents.
# ====================================================================================

f = open("marks.txt", "r")
data = f.read()
print(data)
f.close()

# ====================================================================================
# Question 8- Read marks.txt line by line using readline().
# ====================================================================================

f = open("marks.txt", "r")
line = f.readline()
while line != "":
    print(line, end="")
    line = f.readline()

f.close()

# ====================================================================================
# Question 9- Create a file named notes.txt using x mode and write.
# ====================================================================================

f = open("notes.txt", "x")
f.write("Python File Handling")
f.close()

# ====================================================================================
# Question 10- Open a file in a+ mode, read its contents, then append: (OpenAI)
# ====================================================================================

f = open("student.txt", "a+")

f.seek(0)
data = f.read()
print(data)

f.write("\nOpenAI")
f.close()