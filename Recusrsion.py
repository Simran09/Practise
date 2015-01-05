def power(n, p):
    """ Return n to the power p. works only for positive integers """
    if p == 0:
        return 1
    else:
        return n * power(n, p - 1)
    

if __name__ == '__main__':
    print power(2,23)

