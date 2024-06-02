def mine_location(field):
    for index_row, row in enumerate(field):
        for column_index, i in enumerate(row):
            if i == 1:
                return [index_row, column_index]
    