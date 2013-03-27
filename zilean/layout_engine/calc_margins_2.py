from collections import namedtuple


Column = namedtuple('Column', 'name width')
A = Column('A', 40)
B = Column('B', 25)
C = Column('C', 35)
#D = Column('D', 15)


structure = [A, B, C]
fl = [C, B, A]
cl = structure[:]


def get_margins(cl=cl):
    """
    FOR EACH column in the structure DO:
        work out the current position of the column in the current layout
        work out the final position of the column in the final layout
        work out the shift, that is the number of necesary moves to move the column from his
        current position in the current layout to his final position in the final layout.
        if the shift is equal or gretaer than 0 do:
            work out the columns that goes before column in the final layout, that is the columns
            in final layout that are between column current position and column final position
            for each before column:
                sum their widths
            insert number of 'blanks' columns equal to the amount of shift
            in the current position of the column
        if the shift is less than 0 do:
            work out the columns that goes after column in the final layout, that is the
            columns in final layout that are between column final position and column current position
            for each after column do:
                take off the widths
            delete the column from the current layout
            insert the column in the final position in the current layout
            remove the 'blank' column that goes immediately after column final position
    """
    margins = []
    for column in structure:

        cp = cl.index(column)
        fp = fl.index(column)
        shift = fp - cp

        margin = 0
        if shift >= 0:
            before = fl[cp:fp]
            for c in before:
                margin += c.width
            for i in range(0, shift):
                cl.insert(cp, None)

        if shift < 0:
            after = fl[fp:cp]  # fl[shift:] this works for all 3 columns permutations
            for c in after:
                if c is not None:  # dont needed for work with 3 columns permutations
                    margin -= c.width
            cl.insert(fp, cl.pop(cp))
            cl.pop(fp + 1)
        margins.append((column.name, margin))
    return margins

if __name__ == '__main__':

    print get_margins()
