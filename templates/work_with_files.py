#r(read), w(write), a(append), x

#w overwrite and doesn't create a new file
#a can create a new file and appends

#+ can also read
#w+ write and read, a+ append and read
#there are very weird mechanics with w+, a+. In writing when you write you move to the end of file and if you write you write only the end of file. 
#in appending it starts at the end
#it can be solved with seek(0) or adding additional reading



with open('demo.txt', 'r') as file:
    demo = file.readline()
    print(demo)


with open('output.txt', 'a+') as file:
    file.write(demo)
    file.write(",  and something ")
    file.seek(0)
    print(file.read())

with open('output.txt', 'w') as file:
    file.write("writing")

with open('output.txt', 'r') as file:
    print(file.read())

