d = {}

try:
    del d[1]
except:
    pass

d = {
    1:{
        2: 'x'
    }
}

del d[1][2]

print d