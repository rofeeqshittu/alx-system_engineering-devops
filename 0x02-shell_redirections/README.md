0. A script that prints “Hello, World”, followed by a new line to the standard output.
1. A script that displays a confused smiley "(Ôo)'.
2. Display the content of the /etc/passwd file.
3. Display the content of /etc/passwd and /etc/hosts
4. Display the last 10 lines of /etc/passwd
5. Display the first 10 lines of /etc/passwd
6. Write a script that displays the third line of the file iacta.
7. Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
8. Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
9. Write a script that duplicates the last line of the file iacta.
10. Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
11. Write a script that counts the number of directories and sub-directories in the current directory.
12. Create a script that displays the 10 newest files in the current directory.
13. Create a script that takes a list of words as input and prints only words that appear exactly once.
14. Display lines containing the pattern “root” from the file /etc/passwd
15. Display the number of lines that contain the pattern “bin” in the file /etc/passwd

$ ./15-countthatword
81
$ 

Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.

$ ./16-whatsnext
root:*:0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1:System Services:/var/root:/usr/bin/false
_uucp:*:4:4:Unix to Unix Copy Protocol:/var/spool/uucp:/usr/sbin/uucico
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
_networkd:*:24:24:Network Services:/var/networkd:/usr/bin/false
--
_cvmsroot:*:212:212:CVMS Root:/var/empty:/usr/bin/false
_usbmuxd:*:213:213:iPhone OS Device Helper:/var/db/lockdown:/usr/bin/false
_dovecot:*:214:6:Dovecot Administrator:/var/empty:/usr/bin/false
_dpaudio:*:215:215:DP Audio:/var/empty:/usr/bin/false
$
