# Kill the process naed killmenow
exec { 'pkill killmenow':
  path    => '/usr/bin',
}
