z = open('omnisia.txt',)
v = set()
for s in ps:
    ps = s.split()
    for i in ps:
        v.add(i.rstrip('\n'))
z.close()
print(len(v)) 