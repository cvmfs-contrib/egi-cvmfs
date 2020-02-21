# egi-cvmfs
egi-cvmfs is a meta-package to install the CernVM File System
([cvmfs](https://cernvm.cern.ch/portal/filesystem)) configured for
[EGI](https://www.egi.eu).

This github repository has the source code of course but it is also
available as a pre-built package, and instructions on how to install it
and all of cvmfs are below.

EGI cvmfs installation is very similar to the Open Science Grid
([OSG](https://opensciencegrid.org)) installation, so rather than
repeating all their
[instructions](https://opensciencegrid.org/docs/worker-node/install-cvmfs),
you will be directed below to follow most of them.
The main differences are in the package repository setup and the install
command.

## Preparation

Before starting the installation process, consider the following:

* **User IDs:** If it does not exist already, the installation will
  create the `cvmfs` Linux user.
* **Group IDs:** If they do not exist already, the installation will
  create the Linux groups `cvmfs` and `fuse`.
* **Network:** The host will need network access to a local squid server
  such as the
  [squid distributed by CERN](https://twiki.cern.ch/twiki/bin/view/Frontier/InstallSquid).
  It is also available in the EGI UMD (setup details below).
  The squid will need out-bound access to cvmfs stratum 1 servers on
  the internet.
* **Disk space:** Sufficient (~25GB) cache space reserved, preferably
  in a separate filesystem.

If your host already has a CERN cvmfs installation on it, on a Red Hat
Enterprise Linux (RHEL) based host do this as root:
```
rpm -e --nodeps cvmfs-config-default
```
or on a Debian or Ubuntu host do:
```
dpkg -r --force-depends cvmfs-config-default
```
During the time there is no cvmfs-config-* package installed, mounted
cvmfs repositories should continue to work but other repositories will
not be able to be mounted.

## Package repository setup

If you are using a Debian or Ubuntu host then follow the instructions for
apt on the
[CERN cvmfs downloads page](https://cernvm.cern.ch/portal/filesystem/downloads)
and on the
[cvmfs-contrib home page](https://cvmfs-contrib.github.io).  The egi-cvmfs
package isn't on Debian, but the instructions are here so skip ahead to the
[installing section below](#installing).

For RHEL based hosts, you have a choice between using the standard EGI UMD yum
repository and the CERN cvmfs yum repositories for the cvmfs rpms.  In
addition, the egi-cvmfs rpm itself is currently only in the community
supported cvmfs-contrib-egi repository.  A future release of EGI UMD will have
egi-cvmfs, but for now both choices need to also use cvmfs-contrib.

If you choose to use the EGI UMD repository for RHEL hosts, set it up
by installing the appropriate umd-release rpm shown in the
[UMD-4](http://repository.egi.eu/category/umd_releases/distribution/umd-4/)
documentation.

If you're not using EGI UMD, then follow the yum instructions at the top of the
[CERN cvmfs downloads page](https://cernvm.cern.ch/portal/filesystem/downloads).

The cvmfs-contrib setup needed for the EGI cvmfs installation on RHEL is
a little more complicated than a standard cvmfs-contrib setup because
unlike on Debian there can only be one cvmfs-config-* rpm in each yum
repository.  Run these commands as root to set up both the cvmfs-contrib
repository and the additional cvmfs-contrib-egi yum repository:
```
yum install -y https://ecsft.cern.ch/dist/cvmfs/cvmfs-contrib-release/cvmfs-contrib-release-latest.noarch.rpm
cp /etc/yum.repos.d/cvmfs-contrib.repo /tmp
mv -f /tmp/cvmfs-contrib.repo /etc/yum.repos.d
yum-config-manager --enable cvmfs-contrib-egi >/dev/null
```
The `cp` and `mv` cause a copy of the file to be made instead of a
symlink to a file that's not supposed to be changed.

## <a name="installing"></a>Installing EGI cvmfs

To install EGI cvmfs on RHEL hosts do:
```
yum install egi-cvmfs
```
or on Debian/Ubuntu hosts do
```
apt-get install cvmfs-config-egi cvmfs cvmfs-x509-helper
```

Then proceed to follow the OSG cvmfs instructions starting at 
[Automount setup](https://opensciencegrid.org/docs/worker-node/install-cvmfs/#automount-setup).
On Debian/Ubuntu hosts follow the EL7 instructions for "Automount setup."
