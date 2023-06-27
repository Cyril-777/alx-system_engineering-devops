# puppet manifest to auto install and config ubuntu/nginx
# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx server
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
    server {
      listen 80 default_server;

      location / {
        return 200 'Hello World!\n';
      }

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }
    }
  ",
  require => Package['nginx'],
}

# Enable Nginx default site
file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [Package['nginx'], File['/etc/nginx/sites-enabled/default']],
}
