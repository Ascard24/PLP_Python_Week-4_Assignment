# Question 1
with open("input.txt", "r") as infile:
    content = infile.read()

modified_content = content.upper()

with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been read, modified, and written to output.txt")

# Question 2
try:
    filename = input("Enter the filename: ")
    
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print("An unexpected error occurred:", e)
