# 0x0E. Web Stack Debugging #1

## Project Overview
This project is focused on debugging an Nginx installation to make it listen on port 80 of all the server’s active IPv4 IPs. By writing minimal Bash scripts, you'll ensure the server is configured correctly and running as expected.

## Files and Descriptions

| Filename                                                                 | Description                                                                                          |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| [`0-nginx_likes_port_80`](./0-nginx_likes_port_80)                        | Bash script that configures Nginx to listen on port 80 of all active IPv4 IPs on the server.          |
| [`1-debugging_made_short`](./1-debugging_made_short)                      | A shorter, more concise Bash script to ensure Nginx is properly configured to listen on port 80.      |

## What the Project Will Do
- Debug Nginx installation to ensure it's running and listening on port 80.
- Automate the configuration process with minimal commands in a Bash script.

## Usage
- Run the script `0-nginx_likes_port_80` to configure the server.
- Verify that Nginx is properly listening on port 80 by using `curl 0:80`.

