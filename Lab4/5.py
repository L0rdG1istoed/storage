m = int(input())
d = int(input())

if d < 1 or d > 31 or m < 1 or m > 12:
    print(-1)

else:
    if m == 1:
        d1 = 0
    elif m == 2:
        d1 = 31
    elif m == 3:
        d1 = 59
    elif m == 4:
        d1 = 90
    elif m == 5:
        d1 = 120
    elif m == 6:
        d1 = 151
    elif m == 7:
        d1 = 181
    elif m == 8:
        d1 = 212
    elif m == 9:
        d1 = 243
    elif m == 10:
        max_days = 31
        d1 = 273
    elif m == 11:
        max_days = 30
        d1 = 304
    else:
        d1 = 334



    print(365 - (d1 + d))
