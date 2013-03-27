def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                #nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

if __name__ == '__main__':

    p = all_perms(['A', 'B', 'C', 'D'])
    i = 0
    for e in p:
        print e
        i += 1
    print i
