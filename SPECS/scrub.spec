%bcond_without check

Name:		scrub
Version:	2.5.2
Release:	16%{?dist}
Summary:	Disk scrubbing program
License:	GPLv2+
Group:		System Environment/Base
URL:		http://code.google.com/p/diskscrub/
Source0:	http://diskscrub.googlecode.com/files/%{name}-%{version}.tar.bz2

BuildRequires: autoconf automake libtool
BuildRequires: libgcrypt-devel

Patch0: scrub-2.5.2-extentonly.patch
Patch1: scrub-2.5.2-remove-aes-implementation.patch
Patch2: scrub-2.5.2-test-use-power-2-filesizes.patch
Patch3: scrub-2.5.2-symlinkresolve.patch

%description
Scrub writes patterns on files or disk devices to make
retrieving the data more difficult.  It operates in one of three
modes: 1) the special file corresponding to an entire disk is scrubbed
and all data on it is destroyed;  2) a regular file is scrubbed and
only the data in the file (and optionally its name in the directory
entry) is destroyed; or 3) a regular file is created, expanded until
the file system is full, then scrubbed as in 2).

%prep
%setup -q

%patch0 -p1 -b .extent-only
%patch1 -p1 -b .remove-aes
%patch2 -p1 -b .test-use-power-2-filesizes
%patch3 -p1 -b .symlinkresolve

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%if %{with check}
%check
make check
%endif

%install
make DESTDIR=%{buildroot} install

%files
%doc DISCLAIMER COPYING
%doc README ChangeLog
%{_bindir}/scrub
%{_mandir}/man1/scrub.1*

%changelog
* Mon Aug 16 2021 Sergio Arroutbi <sarroutb@redhat.com> - 2.5.2-16
- Fix covscan issues introduced in previous version
  Resolves: rhbz#1920252

* Thu Aug 12 2021 Sergio Arroutbi <sarroutb@redhat.com> - 2.5.2-15
- Fix for symbolic link resolution
  Resolves: rhbz#1920252

* Tue Jul 16 2019 Daniel Kopecek <dkopecek@redhat.com> - 2.5.2-14
Resolves: rhbz#1689897 - Missing '--extent-only' patch
Resolves: rhbz#1630298 - Removal of component scrub or its crypto from RHEL

* Tue May 14 2019 Daniel Kopecek <dkopecek@redhat.com> - 2.5.2-13
- spec: added check phase (conditional, enabled by default)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Tom Callaway <spot@fedoraproject.org> - 2.5.2-1
- update to 2.5.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 30 2011 Tom Callaway <spot@fedoraproject.org> - 2.4.1-1
- update to 2.4.1

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov  4 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4-1
- update to 2.4

* Tue Jun 29 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2-1
- update to 2.2, new url, source location

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.1-1
- update to 2.1

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9-3
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.9-2
- license tag fix
- ppc32 rebuild

* Mon Jul  9 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.9-1
- bump to 1.9

* Mon Sep  4 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.8-1
- bump to 1.8

* Mon Feb 20 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.7-1
- bump to 1.7, update URL, Source0
- use Ben Woodard's description

* Sat May 21 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.6-2
- cleanups

* Thu May 19 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.6-1
- initial package for Fedora Extras
