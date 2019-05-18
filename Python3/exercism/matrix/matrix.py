class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_as_lists = self.parse_matrix()

    def parse_matrix(self):
        """The origial string is turned into a list of lists of integers."""
        return [[int(num) for num in rows] for rows in [
            row_str.split() for row_str in self.matrix_string.splitlines()]]

    def row(self, index):
        """For a given number, returns that row of the matrix a list."""
        return self.matrix_as_lists[index-1]

    def column(self, index):
        """From a given number, returns that column of the matrix as a list."""
        return [
            self.matrix_as_lists[i][index-1]
            for i in range(len(self.matrix_as_lists))]
