def floodFill(img, x, y, new_clr, old_clr=None):
    # makes sure that the old colour is stored in the function the very first time it's called
    if old_clr == None:
        old_clr = img[x][y]

    # if the image is already the new colour, we don't want to change it
    if img[x][y] == new_clr:
        return 0

    # if the cell we're at is the old colour, its been reached adjacently and must be changed to the new colour
    elif img[x][y] == old_clr:
        img[x][y] = new_clr
        if x + 1 < len(img):
            floodFill(img, x + 1, y, new_clr, old_clr)
        if x - 1 >= 0:
            floodFill(img, x - 1, y, new_clr, old_clr)
        if y + 1 < len(img[x]):
            floodFill(img, x, y + 1, new_clr, old_clr)
        if y - 1 >= 0:
            floodFill(img, x, y - 1, new_clr, old_clr)
        return 1

    else:
        return 0


img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

x = 1
y = 1

new_clr = 3
floodFill(img, x, y, new_clr)

print(img)
