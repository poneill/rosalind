def get_input():
    import sys
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def split_on(xs, pred):
    """Split xs into a list of lists each beginning with the next x
    satisfying pred, except possibly the first"""
    indices = [i for (i,v) in enumerate(xs) if pred(v)]
    return [xs[i:j] for (i,j) in zip([0]+indices,indices+[len(xs)]) if i != j]

def parse_fasta_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    chunks = split_on(lines,lambda line:line.startswith(">"))
    parsed_chunks = [(chunk[0].strip(),"".join([line.strip()
                                                for line in chunk[1:]]))
                     for chunk in chunks]
    return parsed_chunks

def sliding_window(seq,w,verbose=False):
    i = 0
    n = len(seq)
    while i < n - w + 1:
        if verbose:
            if i % verbose == 0:
                print i
        yield seq[i:i+w]
        i += 1
