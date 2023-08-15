# puppet script to increase the limit of open files for a user

$file_to_edit = '/etc/security/limits.conf'

exec { 'increase-hard-file':
  command => "sed -i '/holberton hard/s/5/60000/' ${file_to_edit}",
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file':
  command => "sed -i '/holberton soft/s/4/60000/' ${file_to_edit}",
  path    => '/usr/local/bin/:/bin/'
}
