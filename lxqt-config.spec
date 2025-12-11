#
# Conditional build:
#
%define		qtver		6.6.0

Summary:	Config tools for LXQt desktop suite
Summary(pl.UTF-8):	Narzędzia konfiguracyjne dla środowiska graficznego LXQt
Name:		lxqt-config
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	https://github.com/lxqt/lxqt-config/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	1e5a3ab6a0b85f1339b7b02bc35b5dd5
URL:		http://www.lxqt.org/
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	kp6-libkscreen-devel >= 6.0.0
BuildRequires:	liblxqt-devel >= 2.3.0
BuildRequires:	lxqt-menu-data >= 2.0.0
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xorg-driver-input-libinput-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config tools for LXQt desktop suite.

%description -l pl.UTF-8
Narzędzia konfiguracyjne dla środowiska graficznego LXQt.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config
%attr(755,root,root) %{_bindir}/lxqt-config-appearance
%attr(755,root,root) %{_bindir}/lxqt-config-file-associations
%attr(755,root,root) %{_bindir}/lxqt-config-input
%attr(755,root,root) %{_bindir}/lxqt-config-locale
%attr(755,root,root) %{_bindir}/lxqt-config-monitor
%dir %{_libdir}/lxqt-config
%{_libdir}/lxqt-config/liblxqt-config-cursor.so
%{_desktopdir}/lxqt-config-monitor-autostart.desktop
%{_desktopdir}/lxqt-config-touchpad-autostart.desktop
%{_desktopdir}/lxqt-config-appearance.desktop
%{_desktopdir}/lxqt-config-file-associations.desktop
%{_desktopdir}/lxqt-config-input.desktop
%{_desktopdir}/lxqt-config-locale.desktop
%{_desktopdir}/lxqt-config.desktop
%{_desktopdir}/lxqt-config-monitor.desktop
%{_desktopdir}/lxqt-config-brightness.desktop
# needed for the lang files
%dir %{_datadir}/lxqt/translations/lxqt-config
%dir %{_datadir}/lxqt/translations/lxqt-config-appearance
%dir %{_datadir}/lxqt/translations/lxqt-config-brightness
%dir %{_datadir}/lxqt/translations/lxqt-config-cursor
%dir %{_datadir}/lxqt/translations/lxqt-config-file-associations
%dir %{_datadir}/lxqt/translations/lxqt-config-input
%dir %{_datadir}/lxqt/translations/lxqt-config-locale
%dir %{_datadir}/lxqt/translations/lxqt-config-monitor
%attr(755,root,root) %{_bindir}/lxqt-config-brightness
%{_iconsdir}/hicolor/48x48/apps/brightnesssettings.svg
%dir %{_datadir}/lxqt/icons
%{_datadir}/lxqt/icons/monitor.svg
%{_mandir}/man1/lxqt-config-appearance.1*
%{_mandir}/man1/lxqt-config-input.1*
%{_mandir}/man1/lxqt-config.1*
