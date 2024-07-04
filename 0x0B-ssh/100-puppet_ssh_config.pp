# Ensure the SSH config file exists
file { '/etc/ssh/ssh_config':
  ensure => 'file',
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

# Add configuration to use the specified private key
file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',
}

# Add configuration to refuse password authentication
file_line { 'Turn off passwd auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '^PasswordAuthentication',
}

