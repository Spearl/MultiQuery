#!/usr/bin/env python

import sys
import paramiko
import traceback
from multiprocessing import Pool, Lock

# Global stdout write lock to synchronize output
print_lock = Lock()

def query(target):
	username, hostname = target.split('@')
	port = 22

	# Check if non-standard port given
	if hostname.find(':') >= 0:
		hostname, portstr = hostname.split(':')
		port = int(portstr)

	try:
	    client = paramiko.SSHClient()
	    client.load_system_host_keys()
	    client.set_missing_host_key_policy(paramiko.WarningPolicy)

	    # Connect using system SSH agent for authentication
	    client.connect(hostname, port, username)

	    # Execute uptime on node
	    stdin, stdout, stderr = client.exec_command('uptime')

	    # Print results on stdout
	    print_lock.acquire()
	    for line in stdout:
	    	print line.strip('\n')
	    print_lock.release()
	    
	    client.close()

	except Exception, e:
	    print 'Caught exception: %s: %s' % (e.__class__, e)
	    traceback.print_exc()
	    try:
	        client.close()
	    except:
	        pass

def main():
	# Read destination nodes to be queried
	with open(sys.argv[1], 'r') as f:
		node_list = [ line.strip() for line in f ]

	# Create worker pool with process count equal to cpu_count (default)
	pool = Pool()

	# Query each node
	pool.map(query, node_list)

	# Wrap up
	pool.close()
	pool.join()

if __name__ == '__main__':
	main()