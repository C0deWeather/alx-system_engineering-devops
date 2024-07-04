#This Puppet script creates a file with the included attributes
file { '/tmp/school':
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}
