# notify
Simple notification system to manage distributed notifications

A simple notification system to track completion of jobs on remote
systems. Once you start a task that takes more time than you are
willing to wait for completion without switching to something else,
set up the task to call the notify executable to send a message to
the rest server.

A get_message script running in the background polls for new messages
under your username and uses notify-send to notify you of task completion.
