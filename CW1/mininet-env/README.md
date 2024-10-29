# Mininet VM with Vagrant

First, from this directory, set up your VM:

```bash
# WARNING: This may take a few minutes
vagrant up
```

then you may access the VM via SSH by running:

```bash
# Note the -A to use SSH with agent forwarding. This will allow you to clone
# the repo inside the VM
vagrant ssh -- -A
```

Once inside the VM, you can test that Mininet has been installed properly by running:

```bash
sudo mn --test pingall
```

If you need to copy files from/to the VM, you can use the [vagrant-scp](https://github.com/invernizzi/vagrant-scp) plugin.
First, install it with:

```bash
vagrant plugin install vagrant-scp
```

then you can copy files to the VM using:

```bash
vagrant scp local_path/to/file remote:/path/to/file # in our case, remote name is `mnvm`
```

Remember to run `vagrant <ssh/scp>` at the path where you initialized the VM using `vagrant up`.
