#!/usr/bin/env python
fout = open("submission.csv", "w")
with open("./result.txt", "r") as f:
	for l in f:
		sp = l.split(",")
		img = sp[0].split("/")[3].split(".")[0]	
		label = sp[1]
		fout.write("{0},{1}".format( img, label ))
fout.close()
