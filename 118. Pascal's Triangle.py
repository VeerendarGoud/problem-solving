def generate(numRows: int):

    pascal_array = []
    current_row_count = 0

    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        pascal_array = [[1], [1, 1]]
        current_row_count = 2

    while current_row_count < numRows:
        current_row = [1]
        pre_pascal_row = pascal_array[-1]

        for i in range(len(pre_pascal_row)):
            if i+1 < len(pre_pascal_row):
                current_row.append(pre_pascal_row[i]+pre_pascal_row[i+1])
        current_row.append(1)

        pascal_array.append(current_row)

        current_row_count += 1

    return pascal_array


numRows = 5

##
