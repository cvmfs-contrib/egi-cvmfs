# egi-cvmfs
egi-cvmfs is a meta-package to install the CernVM File System
([cvmfs](https://cvmfs.readthedocs.io/en/stable/cpt-overview.html))
configured for [EGI](https://www.egi.eu).

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

## Package repository setup

If you are using a Debian or Ubuntu host then follow the instructions for
apt on the
[CERN cvmfs downloads page](https://cernvm.cern.ch/portal/filesystem/downloads)
and on the
[cvmfs-contrib home page](https://cvmfs-contrib.github.io).  The egi-cvmfs
package isn't on Debian, but the instructions are here so skip ahead to the
[installing section below](#installing).

For RHEL based hosts, you have a choice between using the standard EGI UMD yum
repository and the CERN cvmfs plus cvmfs-contrib yum repositories:

1.  If you choose to use the EGI UMD repository for RHEL hosts, set it up
    by installing the appropriate umd-release rpm shown in the
    [UMD-4](http://repository.egi.eu/category/umd_releases/distribution/umd-4/)
    documentation.

2.  If you're not using EGI UMD, first follow the yum instructions at the
    top of the [CERN cvmfs downloads
    page](https://cernvm.cern.ch/portal/filesystem/downloads).  Next,
    the cvmfs-contrib setup needed for the EGI cvmfs installation on
    RHEL is a little more complicated than a standard cvmfs-contrib
    setup because unlike on Debian there can only be one cvmfs-config-*
    rpm in each yum repository.  Run these commands as root to set up
    both the cvmfs-contrib repository and the additional
    cvmfs-contrib-egi yum repository:


    ```
    yum install -y https://ecsft.cern.ch/dist/cvmfs/cvmfs-contrib-release/cvmfs-contrib-release-latest.noarch.rpm
    cp /etc/yum.repos.d/cvmfs-contrib.repo /tmp
    mv -f /tmp/cvmfs-contrib.repo /etc/yum.repos.d
    yum-config-manager --enable cvmfs-contrib-egi >/dev/null
    ```

    The `cp` and `mv` cause a copy of the file to be made instead of a
    symlink to a file that's not supposed to be changed.

## <a name="installing"></a>Installing EGI cvmfs

To install EGI cvmfs on RHEL hosts do
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

These instructions should work even if you are replacing a previous
CVMFS installation based on cvmfs-config-default.  On Debian/Ubuntu, if
you did replace cvmfs-config-default then also clean up deleted files
with
```
dpkg --purge cvmfs-config-default
```
