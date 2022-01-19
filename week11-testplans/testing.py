# range the last one is not considered
# the last in any condition is not considered
# t = 'y' + 3 is wrong
# == compare the data (is compare the data/type)
# [2:5] print the 2nd to 4th (not included last)
# %f, %e produces lowercase output, and %F, %E produces uppercase output.

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)
