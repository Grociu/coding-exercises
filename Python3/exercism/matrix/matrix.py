class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_as_lists = self.parse_matrix()

    def parse_matrix(self):
        """Takes the origial string and turns it into a list of lists."""
        stage1 = self.matrix_string.splitlines()
        stage2 = [row_string.split() for row_string in stage1]
        for i in range(len(stage2)):
            for j in range(len(stage2[i])):
                stage2[i][j] = int(stage2[i][j])
        return stage2

    def row(self, index):
        """For a given number, returns that row of the matrix a list."""
        return self.matrix_as_lists[index-1]

    def column(self, index):
        """From a given number, returns that column of the matrix as a list."""
        return [
            self.matrix_as_lists[i][index-1]
            for i in range(len(self.matrix_as_lists))]
