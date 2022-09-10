
#Nhập dãy a và giá trị cần tìm kiếm x, đưa ra i sao cho a[i] là giá trị nhỏ nhất sao cho a[i] >= x, nếu không có in ra i = n + 1
#(n là số phần tử của dãy a)
a = input().split()
x = input()
n = len(a)

#bubblesort
for i in range(0, n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            tmp = a[j]
            a[j] = a[i]
            a[i] = tmp

#Tìm kiếm nhị phân giá trị
l = 0
r = n + 1
while r > l + 1:
    mid = (l + r) // 2
    print(mid, a[mid])
    
    if a[mid] >= x:
        r = mid
    else:
        l = mid
print(r)