# Configuration management :computer:
[![Twitter Carlos](https://img.shields.io/twitter/follow/cbarros27?label=CarlosBarros&style=social)](https://twitter.com/cbarros27)


In this project, I started working with Puppet as a configuration management tool. I practiced writing Puppet 
manifest files to create a file, install a package, and execute a command.

## Tasks :page_with_curl:

* **0. Create a file**
  * [0-create_a_file.pp](./0-create_a_file.pp): Puppet manifest file that
  creates a file `holberton` in the `/tmp` directory.
    * File permissions: `0744`.
    * File group: `www-data`.
    * File owner: `www-data`.
    * File content: `I love Puppet`.

* **1. Install a package**
  * [1-install_a_package.pp](./1-install_a_package.pp): Puppet manifest file
  that install puppet-lint version 2.1.1.

* **2. Execute a command**
  * [2-execute_a_command.pp](./2-execute_a_command.pp): Puppet manifest file
  that kills the process `killmenow`.


## Authors :black_nib:
**Carlos Barros** [Portfolio](https://carlosbarros.netlify.app/)
                  [Github](https://github.com/cbarros7)
                  [LinkdIn](https://www.linkedin.com/in/carlosbarros7/)
                  [Tableau Public](https://public.tableau.com/profile/carlos.barros#!/?newProfile=&activeTab=0)

