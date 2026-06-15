with open("file.txt",mode='w') as file:
    file.write("hello world")

with open("file.txt",mode='r') as file:
    print(file.read())


with open("file.txt",mode='w') as file:
    file.write("hello agas\n")

with open("file.txt", mode='a') as file:
    file.write("Assalamu alaikum")