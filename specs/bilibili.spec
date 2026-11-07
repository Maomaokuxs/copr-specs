%global debug_package %{nil}
%global __provides_exclude ^(%{_libdir}/%{name}/.*\.so)
%global __requires_exclude ^(libmpv|libflutter|libdart|libapp).*

Name:           bilibili
Version:        1.20.0
Release:        2%{?dist}
Summary:        Bilibili desktop client for Linux

# 上游声明：MIT 仅覆盖项目脚本，客户端二进制版权归上海宽娱所有，
# 故本包标记为 Proprietary（见上游 README 免责声明）。
License:        MIT
URL:            https://github.com/msojocs/bilibili-linux
Source0:        https://github.com/msojocs/bilibili-linux/releases/download/v1.20.0-2/bilibili-v1.20.0-2-x64.tar.gz
Source1:        https://raw.githubusercontent.com/Maomaokuxs/rpmbuild/main/assets/bilibili/bilibili-icon.png
Source2:        https://raw.githubusercontent.com/msojocs/bilibili-linux/master/license#/LICENSE

BuildRequires:  desktop-file-utils
BuildRequires:  chrpath
BuildRequires:  rpm-build

%description
Bilibili Linux client ported from the official Bilibili desktop
client, with region roaming support. Watch videos, live streams
and messages on Linux.

%prep
cp %{SOURCE2} LICENSE
mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libdir}/%{name} %{buildroot}%{_bindir} %{buildroot}%{_datadir}/applications
tar xzf %{SOURCE0} -C %{buildroot}%{_libdir}/%{name} 
for f in %{buildroot}%{_libdir}/%{name}/bin/bilibili %{buildroot}%{_libdir}/%{name}/lib/*.so; do
    chrpath -r '$ORIGIN/lib' "$f" 2>/dev/null || true
done
chmod +x %{buildroot}%{_libdir}/%{name}/bin/bilibili
ln -s %{_libdir}/%{name}/bin/bilibili %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<DESKEOF
[Desktop Entry]
Name=Bilibili
Comment=Bilibili desktop client for Linux
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;
StartupWMClass=Bilibili
DESKEOF
%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
* Sat Nov 07 2026 Maomaokuxs <biyuanh@qq.com> - 1.20.0-2
- Update to upstream v1.20.0-2

* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 1.20.0-1
- Update to upstream v1.20.0-1

* Mon Oct 05 2026 Maomaokuxs <biyuanh@qq.com> - 1.19.0-3
- Update to upstream v1.19.0-3

* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 1.19.0-2
- Enrich package metadata (summary, description, license)

* Sat Sep 19 2026 Maomaokuxs <biyuanh@qq.com> - 1.19.0-1
- Update to 1.19.0-1

* Sun Jul 26 2026 Maomaokuxs <biyuanh@qq.com> - 1.18.0-1
- Update to 1.18.0-1
