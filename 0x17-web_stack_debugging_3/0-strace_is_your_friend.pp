# This Puppet manifest fixes issues causing Apache to return a 500 error

# Fix the WordPress site by correcting the file extension in wp-settings.php
exec { 'Fix wordpress site':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => 'shell',
  onlyif   => 'test -f /var/www/html/wp-settings.php && grep -q ".phpp" /var/www/html/wp-settings.php',
}

# Ensure Apache is running after the fix
service { 'apache2':
  ensure => running,
  enable => true,
}

# Optional: Notify to restart Apache after the fix
notify { 'Restart Apache':
  refreshonly => true,
}

# Ensure Apache restarts if the fix command executes successfully
exec { 'Restart Apache':
  command => '/bin/systemctl restart apache2',
  subscribe => Exec['Fix wordpress site'],
  refreshonly => true,
}

