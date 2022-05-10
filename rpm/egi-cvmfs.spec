Summary: EGI metapackage for CVMFS
Name: egi-cvmfs
Version: 4
# The release_prefix macro is used in the OBS prjconf, don't change its name
%define release_prefix 3
Release: %{release_prefix}%{?dist}
License: ASL 2.0
BuildArch: noarch
# Note: cannot require an exact release number (after a dash) unless 
#   including the dist as well, e.g. -2%{?dist}
Requires: cvmfs = 2.9.2
Requires: cvmfs-config-egi = 2.6
Requires: cvmfs-x509-helper >= 2.2

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
* Tue May 10 2022 Dave Dykstra <dwd@fnal.gov> 4-3
- Update to cvmfs-config-egi-2.6

* Thu Mar 28 2022 Dave Dykstra <dwd@fnal.gov> 4-2
- Update to cvmfs-2.9.2

* Thu Mar 16 2022 Dave Dykstra <dwd@fnal.gov> 4-1
- Update to cvmfs-2.9.0

* Thu Sep 23 2021 Dave Dykstra <dwd@fnal.gov> 3-3
- Update to cvmfs-2.8.2 and cvmfs-x509-helper 2.2

* Thu Apr 22 2021 Dave Dykstra <dwd@fnal.gov> 3-2
- Update to cvmfs-2.8.1

* Thu Nov 5 2020 Dave Dykstra <dwd@fnal.gov> 3-1
- Update to cvmfs-2.8.0

* Thu Nov 5 2020 Dave Dykstra <dwd@fnal.gov> 2-7
- Update to cvmfs-2.7.5 and cvmfs-config-egi-2.5

* Tue Sep 15 2020 Dave Dykstra <dwd@fnal.gov> 2-6
- Update to cvmfs-2.7.4

* Wed Jul 01 2020 Dave Dykstra <dwd@fnal.gov> 2-5
- Update to cvmfs-2.7.3

* Mon Apr 27 2020 Dave Dykstra <dwd@fnal.gov> 2-4
- Update to cvmfs-2.7.2.

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
