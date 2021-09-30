def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    matrix = []
    f = open(csv_file_path)
    lines = f.readlines()
    for line in lines:
        tokens = line.split(',')
        matrix.add(tokens)
    return matrix
