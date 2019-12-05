# egi-cvmfs
Meta-package to install cvmfs configured for EGI.

Installation instructions will be updated here once egi-cvmfs is
available in the EGI UMD yum repository.

Meanwhile the best complete installation for EGI is to yum install
cvmfs, cvmfs-config-egi, and cvmfs-x509-helper from 
[EGI UMD](http://repository.egi.eu/category/umd_releases/distribution/umd-4/)
and install egi-cvmfs (which requires the other three packages) from 
[cvmfs-contrib-egi](https://build.opensuse.org/repositories/home:cvmfs:contrib-egi)
(click the down arrow under desired release and find rpm in noarch
directory).
