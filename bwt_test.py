ref = "ATATCGT"

def suffixArray(s):
	''' creation du suffixe array avec leurs rangs ordonnés ''' 
	satups = sorted([(s[i:], i) for i in range(0, len(s)+1)])
	return map(lambda x: x[1], satups)

suffixArray(ref)

def bwt(t):
    ''' transformation de Burrow-wheeler ''' 
    bw = []
    for si in suffixArray(t):
        if si == 0:
            bw.append('$')
        else:
            bw.append(t[si-1])
    print(''.join(bw))
    return ''.join(bw)


bwt(ref)
