import numpy as np

def entropy(p):
    _eps = 1e-10
    _enter = 0
    for v in p:
        if v > _eps:
            _enter += (-v*np.log2(v))
    return _enter

def information_gain(root, leaves):
    root_entropy = entropy(root/np.sum(root))
    leave_entropys = []
    leave_possi = []
    for leave in leaves:
        leave = leave / np.sum(leave)
        leave_entropys+= entropy(leave)
        leave_possi = np.sum(leave)/np.sum(leaves)
    return root_entropy - np.sum(np.array(leave_entropys)*np.array(leave_possi))



e1 = entropy([0.31,0.69])
print(e1)
info1 = information_gain([3,5], [[2,1],[1,3],[0,1]])
print(info1)

