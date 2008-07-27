%define	snap	20080727
%define	orgname	kmilo
Summary:	K Desktop Environment - kmilo
Name:		kde4-kmilo
Version:	4.1.0
Release:	0.%{snap}.2
License:	GPL
Group:		X11/Applications
# svn export svn://anonsvn.kde.org/home/kde/tags/unmaintained/4/kmilo
Source0:	%{orgname}-%{snap}.tar.bz2
# Source0-md5:	423baeae545e02d61a8153e74b483408
Patch0:		%{name}-build.patch
URL:		http://www.kde.org/
BuildRequires:	automoc4 >= 0.9.83
BuildRequires:	kde4-kdebase-devel >= 4.1.0
BuildRequires:	kde4-kdepimlibs-devel >= 4.1.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMILO.

%prep
%setup -q -n %{orgname}
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/*.so
%attr(755,root,root) %{_libdir}/lib*.so.*
%{_datadir}/dbus-*/interfaces/*.xml
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/services/kded/*.desktop
%{_datadir}/kde4/services/kmilo
%{_datadir}/kde4/servicetypes/kmilo
