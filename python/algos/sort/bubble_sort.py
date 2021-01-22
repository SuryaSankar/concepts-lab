def bubble_sort(lst):
    for end_ptr in reversed(range(len(lst))):
        for i in range(end_ptr):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
