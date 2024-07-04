# Puppet manifest to install and configure Nginx

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Configure Nginx main configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm;

    server_name _;

    location / {
        return 200 'Hello World!';
    }

    location = /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
",
  notify => Service['nginx'],
}

# Ensure Nginx is listening on port 80
file_line { 'nginx_listen_port':
  path    => '/etc/nginx/nginx.conf',
  line    => '    listen 80;',
  match   => '^ *listen +80;',
  ensure  => present,
  notify  => Service['nginx'],
}

