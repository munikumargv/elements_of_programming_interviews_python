def rearrange(a):
    for i in range(len(a)):
        a[i:i+2] = sorted(a[i:i+2], reverse=i % 2)
