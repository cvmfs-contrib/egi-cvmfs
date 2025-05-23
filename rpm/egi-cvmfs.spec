Summary: EGI metapackage for CVMFS
Name: egi-cvmfs
Version: 7
# The release_prefix macro is used in the OBS prjconf, don't change its name
%define release_prefix 4
Release: %{release_prefix}%{?dist}
License: ASL 2.0
BuildArch: noarch
# The required cvmfs version has to be an "=", not ">=", so if someone
#   does `dnf upgrade cvmfs` they will also get an upgraded egi-cvmfs
#   and most importantly any other updated dependencies.
# Note: cannot require an exact release number (after a dash) unless 
#   including the dist as well, e.g. -2%{?dist}
Requires: cvmfs = 2.13.0
Requires: cvmfs-config-egi >= 2.7
Requires: cvmfs-x509-helper >= 2.4

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
* Fri May 23 2025 Carl Vuosalo <cvuosalo@cern.ch> 7-4
- Update to cvmfs-2.13.0

* Wed Feb 26 2025 Carl Vuosalo <cvuosalo@cern.ch> 7-3
- Update to cvmfs-2.12.7

* Tue Feb 11 2025 Carl Vuosalo <cvuosalo@cern.ch> 7-2
- Update to cvmfs-2.12.6

* Tue Jan 14 2025 Dave Dykstra <dwd@fnal.gov> 7-1
- Update to cvmfs-2.12.4 and change the cvmfs-config-egi requires to >=.

* Tue Sep 24 2024 Dave Dykstra <dwd@fnal.gov> 6-8
- Update to cvmfs-config-egi-2.7

* Wed Sep  4 2024 Carl Vuosalo <cvuosalo@cern.ch> 6-7
- Update to cvmfs-2.11.5

* Wed Aug 14 2024 Carl Vuosalo <cvuosalo@cern.ch> 6-6
- Update to cvmfs-2.11.4

* Fri Jun 28 2024 Dave Dykstra <dwd@fnal.gov> 6-5
- Update to cvmfs-2.11.3

* Wed Nov  2 2023 Dave Dykstra <dwd@fnal.gov> 6-4
- Update to cvmfs-2.11.2

* Fri Oct 27 2023 Dave Dykstra <dwd@fnal.gov> 6-3
- Update to cvmfs-2.11.1

* Fri Oct 27 2023 Dave Dykstra <dwd@fnal.gov> 6-2
- Update to at least cvmfs-x509-helper-2.4

* Tue Sep  5 2023 Dave Dykstra <dwd@fnal.gov> 6-1
- Update to cvmfs-2.11.0 and at least cvmfs-x509-helper-2.3

* Thu Aug 11 2022 Dave Dykstra <dwd@fnal.gov> 5-1
- Update to cvmfs-2.10.0

* Thu Aug 11 2022 Dave Dykstra <dwd@fnal.gov> 4-4
- Update to cvmfs-2.9.4

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
