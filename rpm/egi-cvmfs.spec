Summary: EGI metapackage for OASIS and CVMFS
Name: egi-cvmfs
Version: 2
# The release_prefix macro is used in the OBS prjconf, don't change its name
%define release_prefix 3
Release: %{release_prefix}%{?dist}
License: ASL 2.0
BuildArch: noarch
# Note: cannot require an exact release number (after a dash) unless 
#   including the dist as well, e.g. -2%{?dist}
Requires: cvmfs = 2.7.1
Requires: cvmfs-config-egi = 2.4
Requires: cvmfs-x509-helper >= 1.2

%description
%{summary}

%prep
exit 0

%build
exit 0

%install
exit 0

%files

%changelog
* Fri Mar 27 2020 Dave Dykstra <dwd@fnal.gov> 2-3
- Undo the last change, since mutual Obsoletes doesn't work.  Instead
  cvmfs-config-{egi|osg} are made to conflict, which will also prevent
  osg-oasis and egi-cvmfs from both being installed.

* Fri Mar 27 2020 Dave Dykstra <dwd@fnal.gov> 2-2
- Add Obsoletes: osg-oasis to make it easy to switch from OSG to EGI
  configurations

* Thu Sep 19 2019 Dave Dykstra <dwd@fnal.gov> 2-1
- Update to cvmfs-2.7.1

* Thu Sep 19 2019 Dave Dykstra <dwd@fnal.gov> 1-4
- Update to cvmfs-x509-helper-1.2

* Mon Sep 09 2019 Dave Dykstra <dwd@fnal.gov> 1-3
- Update to cvmfs-2.6.3

* Wed Aug 14 2019 Dave Dykstra <dwd@fnal.gov> 1-2
- Update to cvmfs-2.6.2

* Thu Aug 08 2019 Dave Dykstra <dwd@fnal.gov> 1-1
- Initial version, based on osg-oasis-15-1
