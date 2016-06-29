#!/usr/bin/env python
import os
import random

train_f = open("./data/train_list.txt", "w")
valid_f = open("./data/valid_list.txt", "w")
fs = [ i for i in os.listdir("./data/train/") ]
random.shuffle(fs)
for f in fs:
	sp = f.split(".")
	label = None
	if sp[0] == "dog":
		label = 1
	elif sp[0] == "cat":
		label = 0
	imgid = int(sp[1])
	if imgid % 10 == 0:
		valid_f.write("{0} {1}\n".format(f, label))
	else :
		train_f.write("{0} {1}\n".format(f, label))
