Summary: EGI metapackage for OASIS and CVMFS
Name: egi-cvmfs
Version: 1
# The release_prefix macro is used in the OBS prjconf, don't change its name
%define release_prefix 2
Release: %{release_prefix}%{?dist}
License: ASL 2.0
BuildArch: noarch
# Note: cannot require an exact release number (after a dash) unless 
#   including the dist as well, e.g. -2%{?dist}
Requires: cvmfs = 2.6.2
Requires: cvmfs-config-egi = 2.4
Requires: cvmfs-x509-helper >= 1.1

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
* Wed Aug 14 2019 Dave Dykstra <dwd@fnal.gov> 1-2
- Update to cvmfs-2.6.2

* Thu Aug 08 2019 Dave Dykstra <dwd@fnal.gov> 1-1
- Initial version, based on osg-oasis-15-1
