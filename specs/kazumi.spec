%global debug_package %{nil}
%global __provides_exclude ^(%{_libdir}/%{name}/.*\.so)
%global __requires_exclude ^(libmpv|libflutter|libdart|libapp).*

Name:           kazumi
Version:        2.4.4
Release:        1%{?dist}
Summary:        Rule-based anime streaming app with danmaku

License:        GPL-3.0-only
URL:            https://github.com/Predidit/Kazumi
Source0:        https://github.com/Predidit/Kazumi/releases/download/2.4.4/Kazumi_linux_2.4.4_amd64.tar.gz
Source1:        https://raw.githubusercontent.com/Maomaokuxs/rpmbuild/main/assets/kazumi/kazumi-icon.png
Source2:        https://raw.githubusercontent.com/Predidit/Kazumi/main/LICENSE#/LICENSE

BuildRequires:  desktop-file-utils
BuildRequires:  chrpath
BuildRequires:  rpm-build

%description
Kazumi is an anime streaming app based on custom rules,
supporting online streaming, danmaku comments and
real-time super-resolution.

%prep
cp %{SOURCE2} LICENSE
mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libdir}/%{name} %{buildroot}%{_bindir} %{buildroot}%{_datadir}/applications
tar xzf %{SOURCE0} -C %{buildroot}%{_libdir}/%{name} --strip-components=1
for f in %{buildroot}%{_libdir}/%{name}/kazumi %{buildroot}%{_libdir}/%{name}/lib/*.so; do
    chrpath -r '$ORIGIN/lib' "$f" 2>/dev/null || true
done
chmod +x %{buildroot}%{_libdir}/%{name}/kazumi
ln -s %{_libdir}/%{name}/kazumi %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<DESKEOF
[Desktop Entry]
Name=Kazumi
Comment=Rule-based anime streaming app with danmaku
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;
StartupWMClass=Kazumi
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
* Fri Nov 13 2026 Maomaokuxs <biyuanh@qq.com> - 2.4.4-1
- Update to 2.4.4
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 2.4.3-1
- Update to 2.4.3

* Thu Oct 15 2026 Maomaokuxs <biyuanh@qq.com> - 2.3.9-1
- Update to 2.3.9
- Update to 2.3.8

* Sat Oct 03 2026 Maomaokuxs <biyuanh@qq.com> - 2.3.7-1
- Update to 2.3.7

* Thu Sep 24 2026 Maomaokuxs <biyuanh@qq.com> - 2.3.6-1
- Update to 2.3.6
- Enrich package metadata (summary, description, license)

* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 2.3.4-1
- Update to 2.3.4

* Sat Sep 19 2026 Maomaokuxs <biyuanh@qq.com> - 2.3.3-1
- Update to 2.3.3

* Fri Aug 28 2026 Maomaokuxs <biyuanh@qq.com> - 2.3.0-1
- Update to 2.3.0

* Wed Aug 12 2026 Maomaokuxs <biyuanh@qq.com> - 2.2.7-1
- Test webhook auto-rebuild

* Sun Jul 26 2026 Maomaokuxs <biyuanh@qq.com> - 2.2.7-1
- Update to 2.2.7
