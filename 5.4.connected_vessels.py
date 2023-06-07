def interleave(*iterables):
    """
    Interleaves the members of one or more iterables into a single list.
    Parameters:
        *iterables (iterable): One or more iterables to interleave.
    Returns:
        A generator that yields interleaved members from the input iterables.
    Example:
        >> list(interleave('abc', [1, 2, 3], ('!', '@', '#')))
        ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
    """
    iterators = [iter(iterable) for iterable in iterables]
    while iterators:
        for iterator in iterators:
            try:
                yield next(iterator)
            except StopIteration:
                iterators.remove(iterator)

if __name__ == '__main__':
    print(list(interleave([1,2,3],['!', '@', '#'], "abc")))