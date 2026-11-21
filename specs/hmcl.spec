%global debug_package %{nil}

Name:           hmcl
Version:        3.17.2
Release:        1%{?dist}
Summary:        Hello Minecraft! Launcher - multifunctional Minecraft launcher

License:        GPL-3.0-only
URL:            https://github.com/HMCL-dev/HMCL
Source0:        https://github.com/HMCL-dev/HMCL/releases/download/v3.17.2/HMCL-3.17.2.jar
Source1:        https://raw.githubusercontent.com/Maomaokuxs/rpmbuild/main/assets/hmcl/hmcl-icon.png
Source2:        https://raw.githubusercontent.com/HMCL-dev/HMCL/main/LICENSE#/LICENSE
Requires:       java
BuildRequires:  desktop-file-utils
BuildRequires:  chrpath

%description
HMCL (Hello Minecraft! Launcher) is a multifunctional,
cross-platform and popular Minecraft launcher. It supports
Microsoft, Mojang, Yggdrasil and offline logins, mod management,
and game customization.

%prep
cp %{SOURCE2} LICENSE
mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_libdir}/%{name} %{buildroot}%{_bindir} %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE0} %{buildroot}%{_libdir}/%{name}/HMCL-%{version}.jar
cat > %{buildroot}%{_bindir}/%{name} <<WRAPEOF
#!/bin/sh
exec java -Dglass.gtk.uiScale=1.5 -jar %{_libdir}/%{name}/HMCL-%{version}.jar "$@"
WRAPEOF
chmod +x %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<DESKEOF
[Desktop Entry]
Name=Hmcl
Comment=Hello Minecraft! Launcher - multifunctional Minecraft launcher
Exec=java -Dglass.gtk.uiScale=1.5 -jar %{_libdir}/%{name}/HMCL-%{version}.jar
Icon=%{name}
Terminal=false
Type=Application
Categories=Utility;
StartupWMClass=Hmcl
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
* Sat Nov 21 2026 Maomaokuxs <biyuanh@qq.com> - 3.17.2-1
- Update to 3.17.2

* Wed Oct 07 2026 Maomaokuxs <biyuanh@qq.com> - 3.16.4-1
- Update to 3.16.4

* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 3.16.3-2
- Enrich package metadata (summary, description, license)

* Sun Jul 26 2026 Maomaokuxs <biyuanh@qq.com> - 3.16.3-1
- Update to 3.16.3
