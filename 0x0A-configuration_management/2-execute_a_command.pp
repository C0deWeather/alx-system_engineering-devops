# This manifest kills a process named killmenow

exec { 'kill killmenow process':
    command => 'pkill -f killmenow',
    path    => '/usr/bin:/bin:/usr/sbin:/sbin',
    onlyif  => 'pgrep -f killmenow',
}
