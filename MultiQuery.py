#!/usr/bin/env python

import sys
from Queue import Queue

def main():
	# Destination nodes to be queried
	node_list = Queue()
	with open(sys.argv[1], 'r') as f:
		for line in f:
			node_list.put(line.strip())

	# Collection of query responses to be consumed by write thread
	log_entries = Queue()

	while q.empty() is False:
		print q.get()

	print "Done!"



if __name__ == '__main__':
	main()