#! /usr/bin/env python
import numpy as np
import numpy.linalg as la

wWWWWWWWWWWWWWWWWWWtest3
rho1 = np.load('./rho1.npy')
u1, s1, vt1 = la.svd(rho1, full_matrices = False)
rho2 = np.load('./rho2.npy')
u2, s2, vt2 = la.svd(rho2, full_matrices = False)

print la.norm(rho1-rho2)
#print la.norm(s1-s2)
print la.norm(vt1-vt2)


