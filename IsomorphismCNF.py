# Import sage and suppress all the warnings
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    from sage.all import *


# TODO Add reformatting code into a separate function
# Reads a reformatted CNF file
def read_cnf_file(filename):
    File = open(filename)
    firstLine = File.readline()
    numRows = int(firstLine.split(" ")[0])
    numCols = int(firstLine.split(" ")[1])

    m = Matrix(nrows=numRows * 2, ncols=numCols + numRows)
    for n, i in enumerate(File.readlines()):
        split_line = i.split(" ")
        # print(n, i)
        for v in split_line:
            if int(v) < 0:
                m[(abs(int(v)) - 1 + (numRows)), n] = 1
            else:
                m[int(v) - 1, int(n)] = 1

    for i in range(numRows):
        m[i, numCols + i] = 2
        m[numRows + i, numCols + i] = 2

    return m

# Read in CNF file and generate matrix
m1 = read_cnf_file("./notebook/data/uf50-01.clean.2")
m2 = read_cnf_file("./notebook/data/uf50-02.clean.2")

# Generate graph from matrices
bm1 = BipartiteGraph(m1)
bm2 = BipartiteGraph(m2)

# Test for isomorphism of CNF graphs
print(bm1.is_isomorphic(bm2))