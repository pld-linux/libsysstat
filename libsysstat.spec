%define		qtver		5.3.1

Summary:	libsysstat
Name:		libsysstat
Version:	0.3.1
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://downloads.lxqt.org/libsysstat/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8513824b127fd1bdcd0ec32f4ba790d6
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
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
Requires:	Qt5Core-devel >= %{qtver}
Requires:	Qt5Gui-devel >= %{qtver}
Requires:	Qt5Xml-devel >= %{qtver}
Obsoletes:	razor-qt-devel

%description devel
This package contains header files and development documentation for
libsysstat.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących libsysstat.

%prep
%setup -q

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
%ghost %{_libdir}/libsysstat-qt5.so.0
%attr(755,root,root) %{_libdir}/libsysstat-qt5.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/sysstat-qt5
%{_libdir}/libsysstat-qt5.so
%{_pkgconfigdir}/sysstat-qt5.pc
%{_datadir}/cmake/sysstat-qt5
