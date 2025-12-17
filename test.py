grid = [["l", "l", "1"], ["l", "l", "l"], ["l", "l", "l"]]


for item in grid:
    modified_grid = ""
    modified_grid += "| ".join(item)
    print(modified_grid)
