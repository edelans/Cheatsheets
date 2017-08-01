
# current version of installed kernel :
```
uname -sr
```

# Upgrading Kernel in Ubuntu

- go to http://kernel.ubuntu.com/~kernel-ppa/mainline/ and choose the desired version
- download the .deb files for your system architecture

```
mkdir /tmp/kernel && cd /tmp/kernel
wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.12.4/linux-headers-4.12.4-041204_4.12.4-041204.201707271932_all.deb
wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.12.4/linux-headers-4.12.4-041204-generic_4.12.4-041204.201707271932_amd64.deb
wget http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.12.4/linux-image-4.12.4-041204-generic_4.12.4-041204.201707271932_amd64.deb
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
