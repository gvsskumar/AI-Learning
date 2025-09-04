# File handling in Python allows you to create, read, write, and delete files.
# It is important when you want to store data permanently (outside program execution).

# Modes in File Handling
# "r" → Read (default) – error if file does not exist
# "w" → Write – creates new file or overwrite existing
# "a" → Append – adds content at the end
# "x" → Create – error if file already exists
# "b" → Binary mode (e.g., images, videos)
# "t" → Text mode (default)

# Opening a File
f = open("test.txt", "w")
f.write("Hello Python")
f.close()

# Reading a File
f = open("test.txt", "r")
print(f.read())
f.close()

# Deleting a File
import os
os.remove("test.txt")

# Closing a File
f = open("test.txt", "w")
f.write("Hello Python")
f.close()

# Context Manager
with open("test.txt", "w") as f:
    f.write("Hello Python")

# Reading a File
with open("test.txt", "r") as f:
    print(f.read())

# Writing a File
with open("test.txt", "w") as f:
    f.write("Hello Python")

# Appending a File
with open("test.txt", "a") as f:
    f.write("Hello Python")

# Deleting a File
import os
os.remove("test.txt")

# Read File Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read File Line by Line
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Read Specific Number of Characters
with open("example.txt", "r") as file:
    print(file.read(10))

# Read Specific Number of Lines
with open("example.txt", "r") as file:
    print(file.readlines(2))

# Delete a File
import os

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted.")
else:
    print("File does not exist.")

    

