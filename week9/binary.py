
def binary(haystack, needle):
    start = 0
    end = len(haystack) - 1
    middle = (start + end) // 2
    while end > start and haystack[middle] != needle:
        if haystack[middle] > needle:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start + end) // 2
    return middle if haystack[middle] == needle else - 1