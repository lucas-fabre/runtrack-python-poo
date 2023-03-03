def fonction(n):
    # if n == 0:
    #    return 1
    # else:
        return n * fonction(n - 1)

    
print(fonction(0))

#if n == 0 return 1; évite une erreur si quelqu'un venait à mettre un 0.
#else: return n * fonction(n - 1) == 