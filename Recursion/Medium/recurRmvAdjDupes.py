def rremove(string):
    # sotring original size for comparisson after the loop
    size = len(string)
    removal = set()

    for i, char in enumerate(string):
        if i + 1 == len(string):
            break
        # if the current and next char are the same, add them to a set of chars to be removed
        if char == string[i + 1]:
            removal.add(i)
            removal.add(i + 1)

    # with the set of indexes to be removed in mind, we create a "new" string
    string = "".join([char for n, char in enumerate(string) if n not in removal])

    # if no changes were made there are no conseccutive chars
    if size == len(string):
        return string

    # if there were changes, we must check again for conseccutive chars
    else:
        return rremove(string)


string = "abccbccba"
print(f"the recursively removed version of '{string}' is '{rremove(string)}'")
