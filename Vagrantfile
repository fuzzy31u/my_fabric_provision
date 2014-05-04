# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "centos64"

  config.vm.provision :fabric do |fabric|
    fabric.fabfile_path = "./provision.py"
    fabric.tasks = ["execute"]
  end
end
