import numpy as np

def calculate(num_list):
    if len(num_list) < 9 or len(num_list) > 9:
        raise ValueError("List must contain nine numbers.")
    else:
        ar_1 = np.array(num_list)
        matrix = np.reshape(ar_1, (3, 3))
        m_shape = np.shape(matrix)
        ops = [np.mean, np.var, np.std, np.amax, np.amin, "plus"]
        calculations = {}

        for op in ops:
            if op == "plus":
                sum_matrix = [[], []]
                total = 0
                # Rows
                for i in range(m_shape[0]):
                    row_total = 0
                    col_total = 0
                    # Columns
                    for j in range(m_shape[1]):
                        row_total += matrix[i][j]
                        col_total += matrix[j][i]
                        total += matrix[i][j]
                    sum_matrix[0].append(col_total)
                    sum_matrix[1].append(row_total)
                sum_matrix.append(total)
                calculations["sum"] = sum_matrix
            else:
                col_op = list(op(matrix, axis=0))
                row_op = list(op(matrix, axis=1))
                matrix_op = op(matrix)
                mvsd = [col_op, row_op, matrix_op]
                if op == np.mean:
                    calculations["mean"] = mvsd
                elif op == np.var:
                    calculations["variance"] = mvsd
                elif op == np.std:
                    calculations["standard deviation"] = mvsd
                elif op == np.amax:
                    calculations["max"] = mvsd
                else:
                    calculations["min"] = mvsd

        return calculations
