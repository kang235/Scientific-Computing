#!/usr/bin/env python # polynomial.py
class Polynomial(object):
	def __init__(self, coeff = []):
		self.coeff = coeff[:]
	def __str__(self):
		r = ''
		n = 0
		for e in reversed(self.coeff):
			p = len(self.coeff) - n - 1	
			c = ''
			s = ''
			if e == 0:
				pass
			elif e > 0:
				s = '+ '
			else:
				s = '- '
			
			if e == 0:
				pass
			elif e == 1:
				pass
			elif e == -1:
				c = '- '
			else:
				c = s + str(abs(e)) + ' '
			
			if e == 0:
				pass
			elif p == 0 and e == 1:
				r += '+ 1'
			elif p == 0 and e == -1:
				r += '- 1'
			elif p == 0 and abs(e) != 1 and e != 0:
				r += c
			elif p == 1:
				r += c + 'x '
			else:
				r += c + 'x^' + str(p) + ' '
			n += 1
		if (r[0:2] == '+ '):	
			r = r[2:]
		return r
	def __repr__(self):
		return str(self)
	def deg(self):
		d = -1
		coeff = self.coeff[:]
		while coeff != [] and coeff[-1] == 0:
			del coeff[-1]
		l = len(coeff)
		if coeff == []:
			pass
		elif l == 1 and coeff[0] == 0:
			pass
		else:
			d = l - 1
		return d 
	def __add__(self, new):
		p1 = self.coeff
		p2 = new.coeff
		if len(p1) < len(p2):
			p1, p2 = p2, p1
		p3 = p1[:]
		for i, e in enumerate(p2):
			p3[i] += e	
		while p3 != [] and p3[-1] == 0: 
			del p3[-1]
		return Polynomial(p3)
	def __sub__(self, new):
		coeff = [ -i for i in new.coeff[:]]		
		return self + Polynomial(coeff)
	def __mul__(self, new):
		if self.coeff == [] or new.coeff == []:
			return 0
		n = 0
		c1 = self.coeff[:]
		l = len(new.coeff)
		p = Polynomial([])
		for c in new.coeff:
			c2 = [0]*(l+n)
			c2[n:] = [x * c for x in c1]
			p += Polynomial(c2)
			n += 1
		return p
	def __call__(self, new):
		if (self.deg() < 1): return self
		sc = self.coeff[:]
		while sc != [] and sc[-1] == 0:
			del sc[-1]
		sc.reverse()
		nc = new.coeff[:]
		while nc != [] and nc[-1] == 0:
			del nc[-1]
		l = len(sc)		
		p = Polynomial()
		for i, e in enumerate(sc):
			if i == 0:
				c = [x * sc[0] for x in nc]
				p = Polynomial(c) + Polynomial([sc[1]])
			elif i > 0 and i + 1 < l:
				p = p * new + Polynomial([sc[i + 1]])
			else:
				pass				
		return p
if __name__ == '__main__':
	p = Polynomial([-2, 1, 0])
	print("degree of " + str(p) + " is " + str(p.deg()))
	T = [None]*12
	T[0] = Polynomial([1])
	print(T[0])
	T[1] = Polynomial([0, 1])
	print(T[1])
	two_x = Polynomial([0, 2])
	for k in range(2, 12):
		T[k] = two_x * T[k-1] - T[k-2]
		print(T[k])
	T3oT2 = T[3](T[2])
	print(T3oT2)
	c0_5 = Polynomial([0.5])
	print(T3oT2(c0_5))
	print(Polynomial()*p)

