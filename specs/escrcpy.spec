%global debug_package %{nil}
%global __os_install_post %{nil}
%global __arch_install_post %{nil}
%global __provides_exclude ^(%{_libdir}/%{name}/.*)

Name:           escrcpy
Version:        3.3.1
Release:        1%{?dist}
Summary:        Scrcpy GUI client powered by Electron

License:        Apache-2.0
URL:            https://github.com/viarotel-org/escrcpy
Source0:        https://github.com/viarotel-org/escrcpy/releases/download/v%{version}/Escrcpy-%{version}-linux-amd64.deb
Source1:        https://raw.githubusercontent.com/viarotel-org/escrcpy/main/LICENSE#/LICENSE

ExclusiveArch:  x86_64

BuildRequires:  binutils
BuildRequires:  desktop-file-utils

# adb/scrcpy 由运行时调用（上游不自带），xdg-utils 供 Electron 打开链接/文件；
# 其余库依赖由 rpm 自动从 Electron 二进制里检测
Requires:       xdg-utils
Requires:       scrcpy
Requires:       android-tools

%description
Escrcpy is a graphical user interface for scrcpy, powered by Electron:
mirror and control an Android device from the desktop, with multi-device
management and screen recording. Repackaged from the official upstream
deb without modification. Note that adb and scrcpy are not bundled and
are required at runtime.

%prep
cp %{SOURCE1} LICENSE
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
ar x %{SOURCE0}
tar -xJf data.tar.xz

%build

%install
mkdir -p %{buildroot}%{_libdir}/escrcpy %{buildroot}%{_bindir} %{buildroot}%{_datadir}
# 应用本体统一进 /usr/lib（官方 deb 放在 /opt）
cp -a %{name}-%{version}/opt/Escrcpy/. %{buildroot}%{_libdir}/escrcpy/
ln -s %{_libdir}/escrcpy/escrcpy %{buildroot}%{_bindir}/escrcpy
# desktop/图标照搬官方包，Exec 改成裸名（走 /usr/bin 软链）
cp -a %{name}-%{version}/usr/share/applications %{buildroot}%{_datadir}/
cp -a %{name}-%{version}/usr/share/icons %{buildroot}%{_datadir}/
sed -i 's|^Exec=/opt/Escrcpy/escrcpy|Exec=escrcpy|' %{buildroot}%{_datadir}/applications/escrcpy.desktop

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/escrcpy.desktop

%files
%license LICENSE
%{_bindir}/escrcpy
%{_libdir}/escrcpy/
%exclude %{_libdir}/escrcpy/chrome-sandbox
%attr(4755, root, root) %{_libdir}/escrcpy/chrome-sandbox
%{_datadir}/applications/escrcpy.desktop
%{_datadir}/icons/hicolor/*/apps/escrcpy.png

%changelog
* Sun Nov 08 2026 Maomaokuxs <biyuanh@qq.com> - 3.3.1-1
- Initial package (repack official upstream deb)
