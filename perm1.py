def perm(seq):
    if len(seq) <= 1:
        return [seq]

    p = []
    for i in range(len(seq)):
        sub_seq = seq[:i] + seq[i+1:]
        sub_p = perm(sub_seq)
        for sub in sub_p:
            p.append( [seq[i]] + sub )
    return p
