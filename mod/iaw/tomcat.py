#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

USUARIOS=12
PS_INI=8006
P_INI=8081
DIR="/home/"

puertos=[]
for u in xrange(0,USUARIOS):
	puertos.append((P_INI,PS_INI))
	P_INI=P_INI+1
	PS_INI=PS_INI+1

cont=1
for puerto,puerto_sh in puertos:
	os.system("tomcat7-instance-create -p %i -c %i %s" % (puerto,puerto_sh,DIR+"tomcat-"+str(cont)))
	cont=cont+1

