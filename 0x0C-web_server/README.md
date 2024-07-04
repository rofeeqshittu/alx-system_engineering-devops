---

# 0x0C. Web Server

## Project Overview
This project focuses on configuring a web server using Bash scripts. The tasks include setting up Nginx, handling DNS, and creating custom error pages. The goal is to automate these configurations to minimize manual repetitive tasks.

## Commands to Know
- `scp`
- `curl`

## Files and Their Functions

### 0-transfer_file
- **Description:** Transfers a file from the client to a server.
- **Usage:** 
  ```bash
  ./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
  ```

### 1-install_nginx_web_server
- **Description:** Installs Nginx on the web server and configures it to listen on port 80 and display "Hello World!".
- **Usage:**
  ```bash
  ./1-install_nginx_web_server
  ```

### 2-setup_a_domain_name
- **Description:** Registers and configures a domain name.
- **Usage:**
  ```bash
  ./2-setup_a_domain_name DOMAIN_NAME
  ```

### 3-redirection
- **Description:** Configures Nginx to redirect `/redirect_me` to another page with a "301 Moved Permanently" status.
- **Usage:**
  ```bash
  ./3-redirection
  ```

### 4-not_found_page_404
- **Description:** Configures Nginx to serve a custom 404 page containing the string "Ceci n'est pas une page".
- **Usage:**
  ```bash
  ./4-not_found_page_404
  ```

## Notes
- Scripts will be executed as the root user, so `sudo` is not necessary.
- Check Nginx logs in `/var/log/` if things do not work as expected.

