#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-config
Name:		lxqt-config
Version:	0.11.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	e50bf87b509ec57281cda154b272392c
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	kp5-libkscreen-devel
BuildRequires:	liblxqt-devel >= 0.11.0
BuildRequires:	libqtxdg-devel >= 2.0.0
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-config

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/menus/lxqt-config.menu
%attr(755,root,root) %{_bindir}/lxqt-config
%attr(755,root,root) %{_bindir}/lxqt-config-appearance
%attr(755,root,root) %{_bindir}/lxqt-config-file-associations
%attr(755,root,root) %{_bindir}/lxqt-config-input
%attr(755,root,root) %{_bindir}/lxqt-config-locale
%attr(755,root,root) %{_bindir}/lxqt-config-monitor
%dir %{_libdir}/lxqt-config
%attr(755,root,root) %{_libdir}/lxqt-config/liblxqt-config-cursor.so
%{_desktopdir}/lxqt-config-appearance.desktop
%{_desktopdir}/lxqt-config-file-associations.desktop
%{_desktopdir}/lxqt-config-input.desktop
%{_desktopdir}/lxqt-config-locale.desktop
%{_desktopdir}/lxqt-config.desktop
%{_desktopdir}/lxqt-config-monitor.desktop

#%dir %{_datadir}/lxqt/translations/lxqt-config
#%dir %{_datadir}/lxqt/translations/lxqt-config-appearance
#%dir %{_datadir}/lxqt/translations/lxqt-config-cursor
#%dir %{_datadir}/lxqt/translations/lxqt-config-file-associations
#%dir %{_datadir}/lxqt/translations/lxqt-config-input
#%dir %{_datadir}/lxqt/translations/lxqt-config-monitor

%attr(755,root,root) %{_bindir}/lxqt-config-brightness
%{_desktopdir}/lxqt-config-brightness.desktop
%{_iconsdir}/hicolor/48x48/apps/brightnesssettings.svg
%{_datadir}/lxqt/icons/monitor.svg
