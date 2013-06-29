#!/usr/bin/env python

import sys
from Queue import Queue

def main():
	with open(sys.argv[1], 'r') as f:
		q = Queue()
		for line in f:
			q.put(line)



if __name__ == '__main__':
	main()