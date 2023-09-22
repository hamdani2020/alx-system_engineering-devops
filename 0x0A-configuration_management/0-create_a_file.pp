# This create create a file with the following content
file {'/tmp/school':
  mode    => '7044',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
