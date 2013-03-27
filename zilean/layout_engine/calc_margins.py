def calc_margins(cl, fl, s):

    margins = []
    for column in s:

        cp = cl.index(column)
        fp = fl.index(column)
        shift = fp - cp

        margin = 0
        if shift == 0:
            margin = 0
        if shift > 0:
            before = fl[cp:fp]
            for c in before:
                margin += c.width
            for i in range(0, shift):
                cl.insert(cp, None)
        if shift < 0:
            after = fl[shift:]
            for c in after:
                margin -= c.width
            cl.insert(fp, cl.pop(cp))
            cl.pop(fp + 1)

        margins.append(margin)
    return margins


