# egi-cvmfs
egi-cvmfs is a meta-package to install the CernVM File System
([cvmfs](https://cernvm.cern.ch/portal/filesystem)) configured for
[EGI](https://www.egi.eu).

This github repository has the source code of course but it is also
available as a pre-built package, and instructions on how to install it
and all of cvmfs are below.

EGI cvmfs installation is very similar to the Open Science Grid
([OSG](https://opensciencegrid.org)) installation, so rather than
repeating all their instructions,
all that is shown here is the differences between the EGI and OSG
installations.  The only differences are in the package repository setup
and the install command.

## Preparation

First, read the introduction and follow the "Before Starting" section in the
[OSG cvmfs installation instructions](https://opensciencegrid.org/docs/worker-node/install-cvmfs), except for the last step to "Prepare the required
Yum repositories."

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

For RHEL based hosts, you have a choice between using the standard EGI UMD yum
repository and the CERN cvmfs yum repositories for the cvmfs rpms.  In
addition, the egi-cvmfs rpm itself is currently only in the community
supported cvmfs-contrib-egi repository.  A future release of EGI UMD will have
egi-cvmfs, but for now both options need to use cvmfs-contrib.

For Debian or Ubuntu hosts, use CERN cvmfs and cvmfs-contrib.  The
egi-cvmfs meta package is not available there, but the installation
instructions are still on this page.

### EGI UMD repository setup

Set up the EGI UMD repository by installing the appropriate umd-release
rpm shown in the
[UMD-4](http://repository.egi.eu/category/umd_releases/distribution/umd-4/)
documentation.

### CERN cvmfs repository setup

If you're not using EGI UMD, then follow the instructions at the top of the
[CERN cvmfs downloads page](https://cernvm.cern.ch/portal/filesystem/downloads)
and choose yum for RHEL hosts and apt for Debian or Ubuntu hosts.

### cvmfs-contrib setup

For Debian or Ubuntu hosts follow the standard instructions for setting up
apt on the [cvmfs-contrib home page](https://cvmfs-contrib.github.io).

For RHEL hosts there is an extra step because unlike on Debian there can
only be one cvmfs-config-* rpm in each yum repository.  Run these
commands as root to set up both the cvmfs-contrib repository and the
additional cvmfs-contrib-egi yum repository:
```
yum install -y https://ecsft.cern.ch/dist/cvmfs/cvmfs-contrib-release/cvmfs-contrib-release-latest.noarch.rpm
cp /etc/yum.repos.d/cvmfs-contrib.repo /tmp
mv -f /tmp/cvmfs-contrib.repo /etc/yum.repos.d
yum-config-manager --enable cvmfs-contrib-egi >/dev/null
```

## Installing EGI cvmfs

To install EGI cvmfs on RHEL hosts do:
```
yum install egi-cvmfs
```
or on Debian/Ubuntu hosts do
```
apt-get install cvmfs-config-egi cvmfs cvmfs-x509-helper
```

Then follow the remainder of the OSG cvmfs instructions starting at 
[Automount setup](https://opensciencegrid.org/docs/worker-node/install-cvmfs/#automount-setup).
On Debian/Ubuntu hosts follow the EL7 instructions for "Automount setup."
