a=int(input())
b=int(input())
c=int(input())
a_b=(a+b)>c
b_c=(b+c)>a
c_a=(c+a)>b
greater_than=a_b and b_c and  c_a
print(greater_than)
