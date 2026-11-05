%global debug_package %{nil}
%global __os_install_post %{nil}
%global __arch_install_post %{nil}
%global __provides_exclude ^(%{_datadir}/%{name}/.*\\.so)

Name:           flclash
Version:        0.9.3
Release:        1%{?dist}
Summary:        Cross-platform proxy client built with Flutter

License:        GPL-3.0-only
URL:            https://github.com/chen08209/FlClash
Source0:        https://github.com/chen08209/FlClash/releases/download/v%{version}/FlClash-%{version}-linux-amd64.rpm
Source2:        https://raw.githubusercontent.com/chen08209/FlClash/main/LICENSE#/LICENSE

BuildRequires:  desktop-file-utils

%description
FlClash is a cross-platform proxy client (Clash/Mihomo front-end)
built with Flutter, supporting rule-based routing, TUN mode,
system tray integration and subscription management.
Repackaged from the official upstream RPM without modification.

%prep
cp %{SOURCE2} LICENSE
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
rpm2cpio %{SOURCE0} | cpio -idm

%build

%install
mkdir -p %{buildroot}%{_libdir}/flclash %{buildroot}%{_bindir} %{buildroot}%{_datadir}
# 应用本体统一进 /usr/lib（官方包放在 /usr/share，无他因）
cp -a %{name}-%{version}/usr/share/FlClash/. %{buildroot}%{_libdir}/flclash/
ln -s %{_libdir}/flclash/FlClash %{buildroot}%{_bindir}/FlClash
# desktop/图标/元数据照搬官方包（Exec/Icon 均为裸名，无需改路径）
cp -a %{name}-%{version}/usr/share/applications %{buildroot}%{_datadir}/
cp -a %{name}-%{version}/usr/share/pixmaps %{buildroot}%{_datadir}/
cp -a %{name}-%{version}/usr/share/metainfo %{buildroot}%{_datadir}/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/FlClash.desktop

%files
%license LICENSE
%{_bindir}/FlClash
%{_libdir}/flclash/
%{_datadir}/applications/FlClash.desktop
%{_datadir}/pixmaps/FlClash.png
%{_datadir}/metainfo/

%changelog
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 0.9.3-1
- Update to 0.9.3

* Sat Oct 17 2026 Maomaokuxs <biyuanh@qq.com> - 0.9.1-1
- Update to 0.9.1
* Thu Oct 15 2026 Maomaokuxs <biyuanh@qq.com> - 0.9.0-1
- Update to 0.9.0
- Update to 0.8.99

* Thu Sep 24 2026 Maomaokuxs <biyuanh@qq.com> - 0.8.98-3
- Fix dangling /usr/bin symlink (absolute libdir path)

* Thu Sep 24 2026 Maomaokuxs <biyuanh@qq.com> - 0.8.98-2
- Move app dir to /usr/lib (repo path standard)
- Initial package (repack official upstream RPM)
