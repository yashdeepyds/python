f=open("justfile.txt","a")
f.write("\nheeeee")
# for i in f:
#     print(i)
f.close()
f=open("justfile.txt")
content = f.read()
print(content)
f.close()