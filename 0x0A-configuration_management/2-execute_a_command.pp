# Kills a process named killmenow

exec { 'processKill':
  command => 'pkill killmenow',
  provider => 'shell',
}
