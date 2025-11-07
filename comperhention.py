import math
# print("normal:") #normal
s1=[1,2,3]
s2=[4,5,6]
# x=[]
# for i in s1:
#     for j in s2:
#         if i!=j:
#             x.append((i,j))
# print(x)

# num=[]
# for i in range(10):
#     if i%2==0:
#         p=pow(i,2)
#         num.append(p)
# print(num)

# print("comperhention:") #comperhention

# squared=[x**2 for x in range(10) if x%2==0]
# print(squared)

# m=list(map(lambda i: i**2 ,range(10)))
# print(m)

# a=[(i,j) for i in s1 for j in s2 if i!=j]
# print(a)
# z=[n**3 for n in range(20)]
# print(z)

# n=["nima","tina","majid"]
# n_c=[ ch for s in n for ch in s ]
# print(n_c)

# x=[round(math.pi,i) for i in range(10)]
# print(x)

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
l=[]
for k in range(3):
    l_row=[]
    for row in matrix:
            l_row.append(row[k])
    l.append(l_row)
print(l)
        
g=[[row[k] for row in matrix]for k in range(3)]
print(g)
