# It kills a process call killmenow
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => shell,
}
