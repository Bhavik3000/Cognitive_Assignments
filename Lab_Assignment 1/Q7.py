# 7.1 Create, write, read:
with open("test_file.txt", "w") as f:
    f.write("Hello, File!")
with open("test_file.txt", "r") as f:
    print(f.read())
    
# 7.2 Append to a file:
with open("test_file.txt", "a") as f:
    f.write("\nNew line has been added.")
with open("test_file.txt", "r") as f:
    print(f.read())

# 7.3 Count lines:
with open("test.txt", "r") as f:
    print(len(f.readlines()))
