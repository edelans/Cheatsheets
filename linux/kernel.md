
# current version of installed kernel :
```
uname -sr
```

# Upgrading Kernel in Ubuntu

- go to http://kernel.ubuntu.com/~kernel-ppa/mainline/ and choose the desired version
- download the .deb files for your system architecture

```
mkdir /tmp/kernel && cd /tmp/kernel
wget -c https://kernel.ubuntu.com/~kernel-ppa/mainline/v4.20/linux-headers-4.20.0-042000_4.20.0-042000.201812232030_all.deb

wget -c https://kernel.ubuntu.com/~kernel-ppa/mainline/v4.20/linux-headers-4.20.0-042000-generic_4.20.0-042000.201812232030_amd64.deb

wget -c https://kernel.ubuntu.com/~kernel-ppa/mainline/v4.20/linux-image-unsigned-4.20.0-042000-generic_4.20.0-042000.201812232030_amd64.deb

wget -c https://kernel.ubuntu.com/~kernel-ppa/mainline/v4.20/linux-modules-4.20.0-042000-generic_4.20.0-042000.201812232030_amd64.deb

```

- install them

```
sudo dpkg -i *.deb
```

- reboot your machine

```
sudo reboot
```

- verify that the new kernel version is being used:

```
uname -sr
```



# Clean old kernels

view/list all installed kernels on your system.

    dpkg --list | grep linux-image

Find all the kernels that lower than your current kernel - 1 (just in case). When you know which kernel to remove run the commands below to remove the kernel you selected.

    sudo apt-get purge linux-image-x.x.x.x-generic


Finally, run the commands below to update grub2

    sudo update-grub2

Reboot your system.
