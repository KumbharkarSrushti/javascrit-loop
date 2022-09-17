#  let n = 5;
#  let string = "";
# // for (let i = 1; i <= n; i++) {
# //   for (let j = 0; j < n - i; j++) {
# //     string += " ";
# //   }
# //   for (let k = 0; k < i; k++) {
# //     string += "*";
# //   }
# //   string += "\n";
# // }
# // console.log(string);


# i=1
# while i<=5:
#     j=1
#     while j<=5-i:
#         print("",end="")
#         j=j+1
#     k=1
#     while k<=i:
#         print("*",end="")
#         k=k+1
#     print()
#     i=i+1

# num_rows = int(input("Enter the number of rows"));
# k = 8
# for i in range(0, num_rows):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 2
#     for j in range(0, i+1):
#         print("* ", end="")
#     print()

i=0
while i<=5:
    j=1
    while j<=5-i:
        print(" ",end="")
        j=j+1
    k=0
    while k<i+1:
        print("*",end="")
        k=k+1
    i=i+1
    print()







# size = 5
# for i in range(size):
#     for j in range(1, size - i):
#         print(" ", end="")
#     for k in range(0, i + 1):
#         print("*", end="")
#     print()
