%define		qtver		4.8.5

Summary:	libsysstat
Name:		libsysstat
Version:	0.1.0
Release:	0.1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://lxqt.org/downloads/libsysstat/0.1.0/%{name}-%{version}.tar.xz
# Source0-md5:	6034052ab9c228aeb5e48d863fa78f41
URL:		http://www.lxqt.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsysstat.

%package devel
Summary:	libsysstat - header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libsysstat
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qtver}
Requires:	QtGui-devel >= %{qtver}
Requires:	QtXml-devel >= %{qtver}
Obsoletes:	razor-qt-devel

%description devel
This package contains header files and development documentation for
libsysstat.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących libsysstat.

%prep
%setup -q -c %{name}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost %{_libdir}/libsysstat.so.0
%attr(755,root,root) %{_libdir}/libsysstat.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/sysstat
%{_libdir}/libsysstat.so
%{_pkgconfigdir}/sysstat.pc
%{_datadir}/cmake/sysstat
