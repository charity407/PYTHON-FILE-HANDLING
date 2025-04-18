#Create a program that reads a file and writes a modified version to a new file.
file = open("input.text", "r")

#writes a modified version to a new file.
file2 = open("output.txt", "w")


#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
try:
    filename = input("Enter the filename: ")
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:   
    print("Error: File not found.")
except IOError:
    print("Error: File cannot be read.")
finally:
    file.close()
