def cigar_function(x):
    sum_term = sum([xi**2 for xi in x[1:]])
    return x[0]**2 + 1e6 * sum_term
