class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_list = self.matrix_string.splitlines()
   
    def row(self, index):
        """ Divides the list of splitlines strings into 
        a list of individual numbers.
        Then gets a list of numbers at i=index-1.
        """
        return [int(i) for i in self.matrix_list[index-1].split()]

    def column(self, index):
        """ From each list of rows, get a new list of item at index-1."""
        return [self.row(i+1)[index-1] for i in range(len(self.matrix_list))]