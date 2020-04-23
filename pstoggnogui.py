input = open("text.txt", "r")
output = open("cloud.xyz", "w")
n=1
for line in input:
        print(n)
        n = n + 1
        i=323
        output.write(str(i)+ line)
input.close()
output.close()