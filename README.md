## MultiQuery

Written by Landon Spear (phyujin@gmail.com) as a project for Yola
6/30/13

This is going to be a multi-process script designed to query several hundred servers in parallel for their uptime and print the results on stdout. 

I'm using paramiko (https://github.com/paramiko/paramiko) to handle the SSH connections. The argument MultiQuery takes should be a file containing all desination nodes in the form "username@hostname[:port]". It is assumed that all nodes can be authenticated against the system's known_hosts file and remote authentication can be achieved through the system's ssh_agent (since entering passwords would be far too slow).

To run: ./MultiQuery [target file]

Current status: parallel solution but output still in race condition
