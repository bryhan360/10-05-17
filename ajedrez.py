#coding:utf-8

for fil in xrange(1,9,1):
	for col in xrange(1,9,1):
			if (fil == 1 or
				fil == 3 or 
				fil == 5 or
				fil == 7):
				if (col % 2 == 0):
					print "[_]",
				else: 
					if (col % 2 == 1):
						print "//",
				
			else:
				if (col % 2 == 0):
					print "//",
				else: 
					if(col % 2 == 1):
						print "[_]",
	print ""
