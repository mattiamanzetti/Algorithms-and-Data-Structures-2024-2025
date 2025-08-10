# Compute the Pascal's Triangle using recursion
#
#         1           n = 0
#       1   1         n = 1
#     1   2   1       n = 2
#   1   3   3   1     n = 3
# 1   4   6   4   1   n = 4
# ...
#
# You can print the triangle like this:
#
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# ...
#
# NOTE: You can use iterative loop(s) inside recursion


def pascal(n):
    if n == 0:
        return [1]
    
    i = 1
    while i <= n:       
        lst = [1]
        lst_rec = pascal(n-1)
        for index in range(n-1):
            lst.append(lst_rec[index] + lst_rec[index + 1])
        lst.append(1)
        i += 1
        return lst

         
if __name__ == "__main__":
    n = 15
    for i in range(n+1):
        print(pascal(i))

