# Puppet script to automate fixing a typo causing apache 500 server error

$file_to_edit = '/var/www/html/wp-settings.php'

exec { 'fix_phpp_typo':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
