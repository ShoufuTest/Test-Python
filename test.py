#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-02-17
# @Author  : Shoufu (gyming@outlook.com)
# @Version : 2.7.6
from math import e



from matplotlib.pyplot import axis, plot, text, title, savefig, show
from numpy import linspace
from numpy.lib.scimath import power

x = linspace(-4, 4, 200)
f1 = power(10, x)
f2 = power(e, x)
f3 = power(2, x)

plot(x, f1, 'r', x, f2, 'b', x, f3, 'g', linewidth=2)
axis([-4, 4, -0.5, 8])
text(1, 7.5, r'$10^x$', fontsize=16)
text(2.2, 7.5, r'$e^x$', fontsize=16)
text(3.2, 7.5, r'$2^x$')
title('A simple example', fontsize=16)

savefig('power.png', dpi=75)
show()
