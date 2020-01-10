# header-only library
%global debug_package %{nil}

Name: mdds
Version: 0.10.3
Release: 1%{?dist}
Summary: A collection of multi-dimensional data structures and indexing algorithms

Group: Development/Libraries
License: MIT
URL: http://code.google.com/p/multidimalgorithm/
Source0: http://kohei.us/files/%{name}/src/%{name}_%{version}.tar.bz2

BuildRequires: boost-devel

%description
A collection of multi-dimensional data structures and indexing algorithms.
 
It implements the following data structures:
* segment tree
* flat segment tree 
* rectangle set
* point quad tree
* multi type matrix
* multi type vector

See README for a brief description of the structures.

%package devel
Group: Development/Libraries
Summary: Headers for %{name}
BuildArch: noarch
Requires: boost-devel
Provides: %{name}-static = %{version}-%{release}

%description devel
Headers for %{name}.

%prep
%setup -q -n %{name}_%{version}
# this is only used in tests
sed -i -e '/^CPPFLAGS_NODEBUG=/s/=.*/="%{optflags}"/' configure

%build
%configure

%install
install -d -m 0755 %{buildroot}/%{_includedir}/mdds
cp -pr include/mdds/* %{buildroot}/%{_includedir}/mdds
install -d -m 0755 %{buildroot}/%{_datadir}/pkgconfig
install -p -m 0644 misc/%{name}.pc %{buildroot}/%{_datadir}/pkgconfig

%check
make check %{?_smp_mflags}

%files devel
%{_includedir}/%{name}
%{_datadir}/pkgconfig/%{name}.pc
%doc AUTHORS COPYING NEWS README

%changelog
* Fri Aug 22 2014 David Tardon <dtardon@redhat.com> - 0.10.3-1
- Resolves: rhbz#1132069 rebase to 0.10.3

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.8.1-3
- Mass rebuild 2013-12-27

* Mon Jun 10 2013 David Tardon <dtardon@redhat.com> - 0.8.1-2
- trivial changes

* Tue May 21 2013 David Tardon <dtardon@redhat.com> - 0.8.1-1
- new release

* Tue May 14 2013 David Tardon <dtardon@redhat.com> - 0.8.0-1
- new release

* Mon Mar 18 2013 David Tardon <dtardon@redhat.com> - 0.7.1-1
- new release

* Thu Feb 28 2013 David Tardon <dtardon@redhat.com> - 0.7.0-1
- new release

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.6.1-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.6.1-2
- Rebuild for Boost-1.53.0

* Tue Sep 18 2012 David Tardon <dtardon@redhat.com> - 0.6.1-1
- new version

* Sat Jul 28 2012 David Tardon <dtardon@redhat.com> - 0.6.0-2
- rebuilt for boost 1.50

* Mon Jul 23 2012 David Tardon <dtardon@redhat.com> - 0.6.0-1
- new version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 David Tardon <dtardon@redhat.com> - 0.5.4-1
- new version

* Thu Jul 14 2011 David Tardon <dtardon@redhat.com> - 0.5.3-1
- new version

* Wed Mar 30 2011 David Tardon <dtardon@redhat.com> - 0.5.2-2
- install license

* Tue Mar 29 2011 David Tardon <dtardon@redhat.com> - 0.5.2-1
- new version

* Thu Mar 24 2011 David Tardon <dtardon@redhat.com> - 0.5.1-3
- Resolves: rhbz#680766 fix a crash and two other bugs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 08 2011 David Tardon <dtardon@redhat.com> - 0.5.1-1
- new version

* Tue Dec 21 2010 David Tardon <dtardon@redhat.com> - 0.4.0-1
- new version

* Tue Nov 16 2010 David Tardon <dtardon@redhat.com> - 0.3.1-1
- new version

* Wed Jul 07 2010 Caolán McNamara <caolanm@redhat.com> - 0.3.0-2
- rpmlint warnings

* Wed Jun 30 2010 David Tardon <dtardon@redhat.com> - 0.3.0-1
- initial import
