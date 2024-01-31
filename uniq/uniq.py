def uniq(inseq):
    have = set()
    for elem in inseq:
        if elem not in have:
            yield elem
            have.add(elem)
