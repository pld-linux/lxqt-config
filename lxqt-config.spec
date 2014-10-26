#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-config
Name:		lxqt-config
Version:	0.8.0
Release:	0.2
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	72f0641977b7f46fa4de5c5cfc30f39d
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Concurrent-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.8.0
BuildRequires:	libqtxdg-devel >= 1.0.0
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
    -DUSE_QT5=ON \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/xdg/menus/lxqt-config.menu
%attr(755,root,root) %{_bindir}/lxqt-config
%attr(755,root,root) %{_bindir}/lxqt-config-appearance
%attr(755,root,root) %{_bindir}/lxqt-config-file-associations
%attr(755,root,root) %{_bindir}/lxqt-config-input
%attr(755,root,root) %{_bindir}/lxqt-config-monitor
%attr(755,root,root) %{_libdir}/liblxqt-config-cursor.so
%{_desktopdir}/lxqt-config-appearance.desktop
%{_desktopdir}/lxqt-config-file-associations.desktop
%{_desktopdir}/lxqt-config-input.desktop
%{_desktopdir}/lxqt-config.desktop
%{_desktopdir}/lxqt-config-monitor.desktop

%dir %{_datadir}/lxqt-qt5/translations/lxqt-config
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_el_GR.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_fi.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_it_IT.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_pl.qm
%lang(pl_PL) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_ru_RU.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_th_TH.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-config/lxqt-config_zh_TW.qm

%dir %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_da.qm
%lang(da_DK) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_de.qm
%lang(de_DE) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_hu.qm
%lang(hu_HU) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_hu_HU.qm
%lang(ia) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_ia.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_id_ID.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_it.qm
%lang(it_IT) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_ja.qm
%lang(ko) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_ko.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_pl.qm
%lang(pl_PL) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_ru_RU.qm
%lang(sk) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_sk_SK.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_sl.qm
%lang(sr) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_sr@latin.qm
%lang(sr_RS) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_sr_RS.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-config-appearance/lxqt-config-appearance_zh_TW.qm

%dir %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_ar.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_cs_CZ.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_da_DK.qm
%lang(de) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_de_DE.qm
%lang(el) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_el_GR.qm
%lang(eo) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_eo.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_es.qm
%lang(es_VE) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_es_VE.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_fr_FR.qm
%lang(hu) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_hu_HU.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_it_IT.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_ja.qm
%lang(lt) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_lt.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_nl.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_pl_PL.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_pt.qm
%lang(pt_BR) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_pt_BR.qm
%lang(ro) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_ro_RO.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_ru.qm
%lang(ru_RU) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_ru_RU.qm
%lang(sl) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_sl.qm
%lang(th) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_th_TH.qm
%lang(tr) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_tr.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-config-cursor/lxqt-config-cursor_zh_TW.qm

%dir %{_datadir}/lxqt-qt5/translations/lxqt-config-input
%lang(af) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_af.qm
%lang(ar) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_ar.qm
%lang(bg) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_bg.qm
%lang(bn) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_bn.qm
%lang(bn_IN) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_bn_IN.qm
%lang(ca) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_ca.qm
%lang(cs) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_cs.qm
%lang(da) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_da.qm
%lang(es) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_es.qm
%lang(eu) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_eu.qm
%lang(fi) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_fi.qm
%lang(fr) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_fr.qm
%lang(gl) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_gl.qm
%lang(hr) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_hr.qm
%lang(id) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_id.qm
%lang(is) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_is.qm
%lang(it) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_it.qm
%lang(ja) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_ja.qm
%lang(nl) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_nl.qm
%lang(pa) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_pa.qm
%lang(pl) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_pl.qm
%lang(pt) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_pt.qm
%lang(ru) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_ru.qm
%lang(sv) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_sv.qm
%{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_template.qm
%lang(uk) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_uk.qm
%lang(zh_CN) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_zh_CN.qm
%lang(zh_HK) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_zh_HK.qm
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-config-input/lxqt-config-input_zh_TW.qm

%dir %{_datadir}/lxqt-qt5/translations/lxqt-config-monitor
%lang(zh_TW) %{_datadir}/lxqt-qt5/translations/lxqt-config-monitor/lxqt-config-monitor_zh_TW.qm
%{_datadir}/lxqt-qt5/translations/lxqt-config-monitor/lxqt-config-monitor_template.qm
