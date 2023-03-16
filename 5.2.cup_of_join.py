def join(*ls, seq='-'):
    """
    Concatenates multiple lists into a single list, with an optional separator between them.
    Parameters:
        *lists (list): One or more lists to concatenate.
        sep (str, optional): The separator to insert between lists. Default is "-".
    Returns:
        A new list that contains the members of all input lists, with the separator between each pair of lists.
    Example:
        >> join([1, 2], [3, 4], [5, 6], sep=':')
        [1, 2, ':', 3, 4, ':', 5, 6]
    """
    output_list = []
    for index, curr_list in enumerate(ls):
        output_list.extend(curr_list)
        if index < len(ls) - 1:
            output_list.append(seq)
    return output_list

#test the function
if __name__ == '__main__':
    print(join([1,2,3], [4,5,6]))