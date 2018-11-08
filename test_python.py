#! /usr/bin/env python
import numpy.linalg as la

rho1 = np.load('./rho1.npy')
u1, s1, vt1 = la.svd(rho1, full_matrices = False)
rho2 = np.load('./rho2.npy')
u2, s2, vt2 = la.svd(rho2, full_matrices = False)

print la.norm(rho1-rho2)
print la.norm(s1-s2)
print la.norm(vt1-vt2)


XXXX---



print s1
print s2
print vt1.shape
print vt2.shape


#print vt1[22]
#print vt2[22]

s1[s1 < 1e-13] = 0.0
rho1_re = u1.dot(np.diag(s1).dot(vt1))

s2[s2 < 1e-13] = 0.0
rho2_re = u2.dot(np.diag(s2).dot(vt2))
print "renomalization"

print la.norm(rho1_re - rho2_re)


pewewey
print la.norm(s3-s4)
QQQ

print la.norm(vt3-vt4)
print vt3[-1] # use
