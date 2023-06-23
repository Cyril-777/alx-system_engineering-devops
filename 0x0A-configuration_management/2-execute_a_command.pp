# Using Puppet, create a manifest that kills a process named killmenow.
exec { 'kill':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
