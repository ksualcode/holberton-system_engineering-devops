# Using Puppet

file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  match  => 'IdentityFile ~/.ssh/id_rsa',
  line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => 'PasswordAuthentication yes',
}
