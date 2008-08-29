%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: Python serial port access library
Name: pyserial
Version: 2.2
Release: 6%{?dist}
Source0: http://easynews.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.zip
License: Python
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: http://pyserial.sourceforge.net/
BuildRequires: python-devel
BuildArch: noarch

%description
This module encapsulates the access for the serial port. It provides backends
for standard Python running on Windows, Linux, BSD (possibly any POSIX
compilant system) and Jython. The module named "serial" automaticaly selects
the appropriate backend.

%prep
export UNZIP="-aa"
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE.txt CHANGES.txt README.txt examples
%{python_sitelib}/*

%changelog
* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2-6
- fix license tag

* Tue Dec 12 2006 Paul P. Komkoff Jr <i@stingr.net>
- rebuilt

* Mon Nov  6 2006 Paul P Komkoff Jr <i@stingr.net> - 2.2-4
- remove "export libdirname"

* Tue Oct 24 2006 Paul P Komkoff Jr <i@stingr.net> - 2.2-3
- Minor specfile fixes

* Sat Oct 14 2006 Paul P Komkoff Jr <i@stingr.net> - 2.2-2
- Minor specfile fixes

* Tue May  9 2006 Paul P Komkoff Jr <i@stingr.net> - 2.2-1
- Fedora Extras submission
