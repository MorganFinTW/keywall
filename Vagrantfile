# -*- mode: ruby -*-
# vi: set ft=ruby :

# Might help reducing cpu usage
$enable_serial_logging = false


Vagrant.configure("2") do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true

  config.vm.synced_folder "~/", "/vagrant-home"

  # If things break again, `VBoxManage list vms`, and put the GUID without
  # curly braces at .vagrant/machines/default/virtualbox/id
  # Bring up the machine via VirtualBox and add the insecure public key
  # to authorized_keys. Then uncomment the two lines below and power off
  # that VirtualBox VM and run `vagrant reload` here.
  # Comment it out again once the new key is in place.
  # config.ssh.insert_key = true
  # config.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/bionic64"
  config.vm.hostname = "keywall.vm"

  # VirtualBox Specific Customization
  config.vm.provider :virtualbox do |vb|
    # Use VBoxManage to customize the VM. For example to change memory:
    vb.customize ["modifyvm", :id, "--memory", "1024"]
    vb.customize ["modifyvm", :id, "--natnet1", "10.12/16"]
    # set timesync parameters to keep the clocks better in sync
    # sync time on start
    vb.customize [
        "guestproperty", "set", :id,
        "/VirtualBox/GuestAdd/VBoxService/--timesync-set-start", 1
    ]
    # at 5 second drift, the time will be set and not "smoothly" adjusted
    vb.customize [
        "guestproperty", "set", :id,
        "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 5000
    ]
  end
  #
  # View the documentation for the provider you're using for more
  # information on available options.

  # Enable shell provisioning to bootstrap puppet
  config.vm.provision :shell, :path => "vagrant/bootstrap.sh"
end
