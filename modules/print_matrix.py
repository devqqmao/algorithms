def print_matrix(matrix):
    """
    # Prints matrix in a grid
    """
    print('\n'.join([' '.join(['{:4}'.format(el) for el in item]) for item in matrix]))
