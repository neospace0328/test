def multiple_table():
    """99乘法表"""

    row = 1

    while row <= 9:
        col = 1
        while col <= row:
            print("%d*%d=%d" % (row, col, row * col), end="\t")
            col += 1
        print("")
        row += 1


multiple_table()
