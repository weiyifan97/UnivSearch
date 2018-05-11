# locate a string in a po (a list of strings)
# partial order: 's' in 'sd' => 's' >= 'sd'

def g(a, b):
    if a in b:
        if a != b:
            return True
    else:
        return False

def minim(po):
    m = po[:]
    for n1 in po:
        for n2 in po:
            if g(n1, n2):
                m.remove(n1)
                break
    return m

def maxim(po):
    m = po[:]
    for n1 in po:
        for n2 in po:
            if g(n2, n1):
                m.remove(n1)
                break
    return m

def ancestors(n1, po):
    a = []
    for n2 in po:
        if g(n2, n1):
            a.append(n2)
    return a

def descendants(n1, po):
    d = []
    for n2 in po:
        if g(n1, n2):
            d.append(n2)
    return d

def parents(node, po):
    return minim(ancestors(node, po))

def children(node, po):
    return maxim(descendants(node, po))
