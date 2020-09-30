#Using strace, find out why Apache is returning a 500 error

file { '/var/www/html/wp-includes/class-wp-locale.phpp':
  ensure => file,
  source => '/var/www/html/wp-includes/class-wp-locale.php',
  mode   => '0664'
}
