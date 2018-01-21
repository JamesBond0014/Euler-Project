below_20 = [0,len("one"),len("two"),len("three"),len("four"),len("five"),len("six"),len("seven"),len("eight"),len("nine"),len("ten"),len("eleven"),
            len("twelve"),len("thirteen"),len("fourteen"),len("fifteen"),len("sixteen"),len("seventeen"),len("eighteen"),len("nineteen")]
above_20 = [len("twenty"),len("thirty"),len("forty"),len("fifty"),len("sixty"),len("seventy"),len("eighty"),len("ninety")]
hundred = len("hundred")
len_and = len("and")
count = 1000
total = 0
def how_long(i):
    length = 0
    adjust = 0
    if (i<20):
        return( below_20[i])
    if (i<100):
        curr = str(i)
        first =  int(curr[0])
        second = int(curr[1])
        return (above_20[first-2] + how_long(second))
    if (i<1000):
        curr = str(i)
        first = int(curr[0])
        second = int(curr[1:3])
        if (second == 0):
            adjust = -3
        return (how_long(first)+hundred+len_and+how_long(second)+adjust)
    else:
        return len("onethousand")

total = 0

print(how_long(200))
for i in range(1,count+1):
    
    total += how_long(i)
    
print(total)