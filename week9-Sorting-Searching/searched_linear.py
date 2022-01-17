# alphabetical (order)

def linear_sorted(haystack, needle):
    index = 0
    while index < len(haystack) and haystack[index] < needle:
        index += 1
        return index if haystack[index] == needle else - 1