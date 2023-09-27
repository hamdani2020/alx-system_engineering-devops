# Install and configure Nginx
package { 'jfryman-nginx':
  ensure => installed,
}

include nginx

class { 'nginx':
  manage_repo    => true,
  package_source => 'nginx-stable',
}

nginx::resource::server { '18.209.180.135':
  listen_port      => 80,
  www_root         => '/var/www/html/',
  vhost_cfg_append => { 'rewrite' => '^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent' },
}

file { 'index':
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
}
