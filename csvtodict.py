path = input("Enter CSV path: ")
file = open(path, 'r')
lines = file.readlines()
file.close()

key = lines[0].strip().split(',')
print(key)

for l in lines[1:]:
    value = l.strip().split(',')
    rowd = {}

    for i in range(len(key)):
        rowd[key[i]] = value[i]

    print(rowd)
 