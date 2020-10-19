ref = "ATATCGT"

def suffixArray(s):
	''' creation du suffixe array avec leurs rangs ordonnés ''' 
	satups = sorted([(s[i:], i) for i in range(0, len(s)+1)])
	return map(lambda x: x[1], satups)

suffixArray(ref)

def bwt(t):
    ''' transformation de Burrow-wheeler ''' 
    global bw
    bw = []
    for si in suffixArray(t):
        if si == 0:
            bw.append('$')
        else:
            bw.append(t[si-1])
    print(''.join(bw))
    return ''.join(bw)


bwt(ref)


def rankBwt(bw):
	''' Retourne les rangs ''' 
	global tots
	tots = dict()
	ranks = []
	for c in bw:
		if c not in tots:
			tots[c] = 0
			ranks.append(tots[c])
		tots[c] += 1
	return ranks, tots


rankBwt(''.join(bw))


def firstCol(tots):
	''' retourne la premiere colonne ''' 
	first = {}
	totc = 0
	for c, count in sorted(tots.iteritems()):
		first[c] = (totc, totc + count)
		totc += count
	return first


firstCol(tots)


def reverseBwt(bw):
	''' Retourne le texte original de la transformation bw '''
	ranks, tots = rankBwt(bw)
	first = firstCol(tots)
	rowi = 0
	t = "$"
	while bw[rowi] != '$':
		c = bw[rowi]
		t = c + t
		rowi = first[c][0] + ranks[rowi]
	return t


reverseBwt(ref)