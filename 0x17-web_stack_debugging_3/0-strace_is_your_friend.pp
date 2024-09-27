# 0-strace_is_your_friend.pp
# Puppet manifest to fix WordPress directory permissions

file { '/var/www/html/your_wordpress_directory':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

file { '/var/www/html/your_wordpress_directory/*':
  ensure => file,
  owner  => 'www-data',
  group  => 'www-data',
  mode   => '0644',
}

