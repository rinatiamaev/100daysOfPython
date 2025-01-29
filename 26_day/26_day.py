list = [1,2, 3]
new_list = []
# for n in list:
#     add1 = n + 1
#     new_list.append(add1)

new_list = [n + 2 for n in list]


print(new_list)

name = "HIVE HELSINKI"

name_list = [letter for letter in name]
print(name_list)


list_range = [n * 2 for n in range(1, 5)]
print(list_range)

real_madrid = ["Mbappe", "Vini", "Lunin", "Modrich"]

short_names = [name.upper() for name in real_madrid if len(name) > 4]

print(short_names)


nbrs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squar_nbr = [n * n for n in nbrs]

print(squar_nbr)

even_nbrs = [n for n in nbrs if n % 2 == 0]

print(even_nbrs)

# result [3, 6, 5, 33, 12, 7, 42, 13]

txtfile1=open('file1.txt')

L1=[]
for line in txtfile1:
    L1.append(line.rstrip())

print(L1)

txtfile2=open('file2.txt')

L2=[]
for line in txtfile2:
    L2.append(line.rstrip())

print(L2)
result = [int(n) for n in L1 if n in L2]
print(result)

txtfile1.close()
txtfile2.close()