# From https://stackoverflow.com/questions/16560840/python-merge-dictionaries-with-custom-merge-function
def merge(A, B, f):
    # Start with symmetric difference; keys either in A or B, but not both
    merged = {k: A.get(k, B.get(k)) for k in A.viewkeys() ^ B.viewkeys()}
    # Update with `f()` applied to the intersection
    merged.update({k: f(A[k], B[k]) for k in A.viewkeys() & B.viewkeys()})
    return merged