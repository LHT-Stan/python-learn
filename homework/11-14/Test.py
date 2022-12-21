lst = [[0 * 3 for i in range(3)] for j in range(3)]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mid_h = 0
mid_l = int(len(lst) / 2)
grid = len(lst[0])
count = max(nums)
for i in range(grid*grid, 0, -1):
    lst[mid_h][mid_l] = count
    mid_h = (mid_h - 1) % grid
    mid_l = (mid_l - 1) % grid
    count = count - 1
    if lst[mid_h][mid_l] != 0:
        mid_h = (mid_h+grid+1+1) % grid
        mid_l = (mid_l+grid+1) % grid
for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end=" ")
    print()
