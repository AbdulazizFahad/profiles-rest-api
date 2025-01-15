# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.boot_timeout = 600
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048" # Set memory to 2GB
    vb.cpus = 2        # Allocate 2 CPU cores
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update -y || true
    sudo apt-get install -y python3-venv zip || true

    # Disable apt-daily services
    systemctl disable apt-daily.service || true
    systemctl disable apt-daily.timer || true

    # Add Python alias
    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
end
