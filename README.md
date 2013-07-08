## MultiQuery

Written by Landon Spear (phyujin@gmail.com) as a project for Yola
6/30/13

This is going to be a multi-process script designed to query several hundred servers in parallel for their uptime and print the results on stdout. 

To run: ./MultiQuery [target file]

 The argument MultiQuery takes should be a file containing all desination nodes in the form "username@hostname[:port]". I'm using paramiko (https://github.com/paramiko/paramiko) to handle the SSH connections. It is assumed that all nodes can be authenticated against the system's known_hosts file and remote authentication can be achieved by public key authentication through the system's ssh_agent.

 Parallelism is achieved with a worker pool from the multiprocessing library. The pool simply maps the query function on the array of destination addresses.


Current status: multi-process parallel solution with output synchronization through global write lock
