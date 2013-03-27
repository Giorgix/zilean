"""
Improvements
    the algorithm must work with different sizes for each element.
"""

"""
TO calculate the margins of an element DO:
    check if next element is in the final layout, if not exit
    find the position of the next element in the current layout
    find the position of the next element in the final layout
    work out the amount to be shifted for next element
    work out the margin
    append the element and his margin to the list of margins
    if the margin is 0 or positive, that means that the next element is shifted forwards, insert
    blank spaces in the current layout
    if the margin is negative, that means that the element is shifted backwards, remove 1 blank
    space from the current layout
    increment the next element counter and call the function again with the new current layout
"""
margins = []
final_layout = [3, 1, 2]


def cal_margin(current_layout=[1, 2, 3], next_element=1):

    if next_element not in final_layout:
        return
    else:
        element_position_in_current_layout = current_layout.index(next_element)
        element_position_in_final_layout = final_layout.index(next_element)
        shift = (element_position_in_final_layout - element_position_in_current_layout) + 1

        margin = shift * 33
        margins.append((next_element, margin))

        if margin >= 0:
            for i in range(0, shift):
                current_layout.insert(0, current_layout.index(next_element))

        else:
            if 0 in current_layout:
                current_layout.remove(0)
        cal_margin(current_layout, next_element=next_element + 1)


if __name__ == '__main__':

    cal_margin()
    print margins
