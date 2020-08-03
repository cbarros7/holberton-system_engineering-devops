# Execute a command
exec { 'pkill -f killmenow':
  path     => '/usr/bin:/usr/local/bin/:/bin',
}
 
