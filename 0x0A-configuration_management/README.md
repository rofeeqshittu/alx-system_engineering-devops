## Introduction
Welcome to my Configuration Management project using Puppet! This README documents my journey and work on the tasks for the 0x0A. Configuration Management project. As a software engineering student, I will be solving these tasks and pushing the solutions to GitHub.

### Installation
#### Puppet Installation
```bash
apt-get install -y ruby=1:2.7+1 --allow-downgrades
apt-get install -y ruby-augeas
apt-get install -y ruby-shadow
apt-get install -y puppet
```

#### Puppet-lint Installation
```bash
gem install puppet-lint
```

## Tasks
### Task 0: Create a File
Using Puppet, create a file in `/tmp`.

**Requirements:**
- File path is `/tmp/school`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains `I love Puppet`

**Example:**
```bash
puppet-lint 0-create_a_file.pp
puppet apply 0-create_a_file.pp
ls -l /tmp/school
cat /tmp/school
```

### Task 1: Install a Package
Using Puppet, install Flask from pip3.

**Requirements:**
- Install Flask
- Version must be `2.1.0`

**Example:**
```bash
puppet apply 1-install_a_package.pp
flask --version
```

### Task 2: Execute a Command
Using Puppet, create a manifest that kills a process named `killmenow`.

**Requirements:**
- Must use the `exec` Puppet resource
- Must use `pkill`

**Example:**
```bash
puppet apply 2-execute_a_command.pp
```

**Files**: 
- `0-create_a_file.pp`
- `1-install_a_package.pp`
- `2-execute_a_command.pp`

---
