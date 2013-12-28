EPIGENESIS
----------

Use the power of distributed computing to reveal the plaintext of a given hash.

For more information, join #epigenesis on freenode.


""This project is for research purposes""
Details about the special protocol is below (#protocol).

IMPORTANT: THE SYSTEM LACKS FOR ANY AUTHENTICATION OR SECURITY FOR NOW.

The system consists of three apps:
* The cooperation server:
	1- Receives job requests and add them to the queue.
	2- Handles the Join/Depart of worker nodes.
	3- Provides information and statistics about the job queue and current tasks.
	4- Notifies worker nodes and clients when there's any update (about data, or even the program).
	5- Divides the problem (job) into sub-problems (tasks) and distributed them to clients (as intervals).

* The worker node:
	1- Receives tasks from the cooperation server.
	2- Runs the task.
	3- Provides statistics about the status when asked.
	4- Returns result upon completing the task.
	5- Accepts commands from cooperation server (i.e., abortion, new task, ...etc).

* The client:
	1- Requests jobs from cooperation server.
	2- Requests statistics.


-- The cooperation server is based on HTTP, one route (path) is for clients (requesters) and the another one is for worker nodes.


Protocol
--------
	We use JSON-based protocol, with the following specifications:
		1- 

Server Specifications
---------------------
	1- Listens on port: TCP/5852.
	2- Handle logins and roles on path ('<host>/login/'). -- Not implemented yet --
	3- 
