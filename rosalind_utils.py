from collections import Counter

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
    parsed_chunks = [(chunk[0].strip()[1:],"".join([line.strip()
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

def hamming(xs,ys):
    return sum(zipWith(lambda x,y:x!=y,xs,ys))

def zipWith(f,xs,ys):
    return map(lambda(x,y):f(x,y),zip(xs,ys))

def fac(n):
    from math import gamma
    return gamma(n+1)

def choose(n,k):
    return fac(n)/(fac(k) * fac(n-k))

def group_by(xs,n):
    chunks = [xs[i:i+n] for i in range(0,len(xs),n)]
    assert(xs == concat(chunks))
    return chunks

def group_codons(seq):
    codons = [seq[i*3:(i+1)*3] for i in range(len(seq)/3)]
    assert seq == "".join(codons)
    return codons

def translate(codon):
    alphabet = "DNA" if "T" in codon else "RNA"
    trans_table = (dna_trans_table if alphabet == "DNA" else rna_trans_table)
    if len(codon) == 3:
        for aa in trans_table:
            if codon in trans_table[aa]:
                return aa
    else:
        return "".join(map(translate,group_codons(codon)))

dna_trans_table = {"A":["GCA","GCC","GCG","GCT"],
                     "R": ["AGA","AGG","CGA","CGC","CGG","CGT"],
                     "N": ["AAT", "AAC"],
                     "D": ["GAT", "GAC"],
                     "C": ["TGT", "TGC"],
                     "E": ["GAA", "GAG"],
                     "Q": ["CAA", "CAG"],
                     "G": ["GGA","GGC","GGG","GGT"],
                     "H": ["CAT", "CAC"],
                     "I": ["ATT", "ATC", "ATA"],
                     "L": ["TTA", "TTG", "CTA","CTC","CTG","CTT"],
                     "K": ["AAA", "AAG"],
                     "M": ["ATG"],
                     "F": ["TTT", "TTC"],
                     "P": ["CCA","CCC","CCG","CCT"],
                     "S": ["AGT", "AGC", "TCA","TCC","TCG","TCT"],
                     "T": ["ACA","ACC","ACG","ACT"],
                     "W": ["TGG"],
                     "Y": ["TAT", "TAC"],
                     "V": ["GTA","GTC","GTG","GTT"],
                     "": ["TAA", "TAG","TGA"]}

rna_trans_table = {"A":["GCA","GCC","GCG","GCU"],
                     "R": ["AGA","AGG","CGA","CGC","CGG","CGU"],
                     "N": ["AAU", "AAC"],
                     "D": ["GAU", "GAC"],
                     "C": ["UGU", "UGC"],
                     "E": ["GAA", "GAG"],
                     "Q": ["CAA", "CAG"],
                     "G": ["GGA","GGC","GGG","GGU"],
                     "H": ["CAU", "CAC"],
                     "I": ["AUU", "AUC", "AUA"],
                     "L": ["UUA", "UUG", "CUA","CUC","CUG","CUU"],
                     "K": ["AAA", "AAG"],
                     "M": ["AUG"],
                     "F": ["UUU", "UUC"],
                     "P": ["CCA","CCC","CCG","CCU"],
                     "S": ["AGU", "AGC", "UCA","UCC","UCG","UCU"],
                     "T": ["ACA","ACC","ACG","ACU"],
                     "W": ["UGG"],
                     "Y": ["UAU", "UAC"],
                     "V": ["GUA","GUC","GUG","GUU"],
                     "": ["UAA", "UAG","UGA"]}

def consensus(motif):
    """Return the consensus of a motif"""
    cols = transpose(motif)
    return "".join([char for (char,count) in
                    map(lambda col:max(Counter(col).items(),key=lambda (b,c):c),
                        cols)])

def transpose(xxs):
    """Transpose a list of the form [[a1,a2...],[b1,b2..]...] into a
    list of the form [[a1,b1,...],[a2,b2,...]...]"""
    return zip(*xxs)
