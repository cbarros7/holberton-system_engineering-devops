# Processes and signals :computer:

In this project, I learned about handling process ID's and signals in Bash
using `ps`, `pgrep`, `pkill`, `pkill`, `exit`, and `trap`.

## Requeriments :bookmark_tabs:

* Allowed editors: ```vi```, ```vim```, ```emacs```
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* All files should end with a new line
* The first line of all your Bash scripts should be exactly ```#!/usr/bin/env bash```
* Your Bash script must pass Shellcheck (```version 0.3.3-1~ubuntu14.04.1``` via ```apt-get```) without any error
* All your files must be executable

## Tasks :page_with_curl:

* **0. What is my PID**
  * [0-what-is-my-pid](./0-what-is-my-pid): Bash script that displays its own PID.

* **1. List your processes**
  * [1-list_your_processes](./1-list_your_processes): Bash script that displays a
  list of currently running processes.
  * Shows all processes for all users, including those not featuring a TTY.
  * Processes are displayed in a user-oriented hierarchy.

* **2. Show your Bash PID**
  * [2-show_your_bash_pid](./2-show_your_bash_pid): Bash script that displays lines
  containing the `bash` keyword based on the script defined in `1-list_your_processes`.

* **3. Show your Bash PID made easy**
  * [3-show_your_bash_pid_made_easy](./3-show_your_bash_pid_made_easy): Bash script
  that displays the PID along with the process name of processes who name contains the
  word `bash`.

* **4. To infinity and beyond**
  * [4-to_infinity_and_beyond](./4-to_infinity_and_beyond): Bash script that displays
  `To infinity and beyond` indefinitely with a `sleep 2` in between each iteration.

* **5. Kill me now**
  * [5-kill_me_now](./5-kill_me_now): Bash script that kills the
  [4-to_infinity_and_beyond](./4-to_infinity_and_beyond) process using `kill`.

* **6. Kill me now made easy**
  * [6-kill_me_now_made_easy](./6-kill_me_now_made_easy): Bash script that kills the
  [4-to_infinity_and_beyond](./4-to_infinity_and_beyond) process using `pkill`.

* **7. Highlander**
  * [7-highlander](./7-highlander): Bash script that displays `To infinity and beyond`
  indefinitely with a `sleep 2` in between each iteration.
  * Displays `I am invincible!!!` upon receiving a `SIGTERM` signal.

* **8. Beheaded process**
  * [8-beheaded_process](./8-beheaded_process): Bash script that kills the process
  [7-highlander](./7-highlander).

## Quick start :runner:
Git clone the repository:

```
git clone https://github.com/cbarros7/holberton-system_engineering-devops.git
```

## Bugs :loudspeaker:
No known bugs.


## Authors :black_nib:
**Carlos Barros** [Github](https://github.com/cbarros7)
                  [LinkdIn](https://www.linkedin.com/in/carlosbarros7/)
                  [Twitter](https://twitter.com/cbarros27)
                  [Medium](https://medium.com/@cbarros7)