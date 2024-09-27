# 0x12. Web Stack Debugging #2

## Overview
This project is part of the **ALX Software Engineering** program. It focuses on debugging common web stack issues, particularly user permissions and Nginx configuration. The goal is to understand the infrastructure behind web servers, learn secure configurations, and apply debugging techniques for troubleshooting web servers.

Key objectives:
- Running software as a non-root user.
- Configuring Nginx to run under a limited-privilege user for security.
- Refactoring solutions to improve efficiency.

## Concepts Covered
- Web stack debugging.
- Process management in Linux (e.g., using `ps` to inspect processes).
- Security practices: Running web services as non-root users.
- Bash scripting and managing user permissions in Linux.

## Project Structure

| **Filename**                  | **Description**                                                                                     |
|-------------------------------|-----------------------------------------------------------------------------------------------------|
| `0-iamsomeoneelse`             | Bash script to run the `whoami` command as a user passed as an argument.                            |
| `1-run_nginx_as_nginx`         | Configures Nginx to run as the `nginx` user and listen on all active IP addresses on port 8080.     |
| `100-fix_in_7_lines_or_less`   | Refactor the solution from task 1 to be no more than 7 lines long.                                  |

---

## Tasks

### 0. Run Software as Another User
The **root** user has full control over the system, but it's safer to run certain commands as non-root users to prevent irreversible mistakes. In this task, you will write a script that runs the `whoami` command as a different user passed as an argument.

| **Filename**       | **Description**                                                                                     |
|--------------------|-----------------------------------------------------------------------------------------------------|
| `0-iamsomeoneelse`  | Bash script that accepts one argument (a username) and runs the `whoami` command as that user.      |

**Example**:
```bash
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root

---

### 1. Run Nginx as Nginx
Running web services such as Nginx as the `root` user is risky because it allows full control of the server. A better security practice is to run Nginx as a less-privileged user. In this task, you will configure Nginx to run as the `nginx` user and listen on all active IPs on port 8080.

| **Filename**          | **Description**                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------|
| `1-run_nginx_as_nginx` | Bash script that configures Nginx to run as the `nginx` user and listen on port 8080 on all active IPs.               |

**Example**:
After running the script, verify that Nginx is running as the `nginx` user:
```bash
root@ubuntu:~# ps auxff | grep ngin[x]
nginx      884  0.0  0.0  77360  2744 ?        Ss   19:16   0:00 nginx: master process /usr/sbin/nginx
nginx      885  0.0  0.0  77712  2772 ?        S    19:16   0:00  \_ nginx: worker process
root@ubuntu:~# nc -z 0 8080 ; echo $?
0

