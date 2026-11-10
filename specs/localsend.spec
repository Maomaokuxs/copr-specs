%global debug_package %{nil}
%global __os_install_post %{nil}
%global __arch_install_post %{nil}
%global __provides_exclude ^(%{_libdir}/%{name}/.*\\.so)

Name:           localsend
Version:        1.18.2
Release:        5%{?dist}
Summary:        Open source cross-platform alternative to AirDrop

License:        Apache-2.0
URL:            https://github.com/localsend/localsend
Source0:        https://github.com/localsend/localsend/releases/download/v%{version}/LocalSend-%{version}-linux-x86-64.deb
Source1:        https://raw.githubusercontent.com/localsend/localsend/main/LICENSE#/LICENSE

ExclusiveArch:  x86_64

BuildRequires:  binutils
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
LocalSend is a free, open-source app that lets you securely share files
and messages with nearby devices over your local network without needing
an internet connection. Think AirDrop for all platforms.
Repackaged from the official upstream DEB without modification.

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
ar x %{SOURCE0}
tar --no-same-owner -xf data.tar.zst
cp %{SOURCE1} LICENSE

%build

%install
cd %{name}-%{version}
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/localsend %{buildroot}%{_bindir}
# 应用本体统一进 /usr/lib（官方 deb 放在 /opt，无他因）
cp -a opt/localsend_app/. %{buildroot}%{_libdir}/localsend/
ln -s %{_libdir}/localsend/localsend_app %{buildroot}%{_bindir}/localsend_app
mkdir -p %{buildroot}%{_datadir}
cp -a usr/share/. %{buildroot}%{_datadir}/
# LICENSE 装到标准位置
mkdir -p %{buildroot}%{_licensedir}/%{name}
cp -a LICENSE %{buildroot}%{_licensedir}/%{name}/

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/localsend_app.desktop

%files
%license %{_licensedir}/%{name}/LICENSE
%{_bindir}/localsend_app
%{_libdir}/localsend/
%{_datadir}/applications/localsend_app.desktop
%{_datadir}/icons/hicolor/

%changelog
* Tue Nov 10 2026 Maomaokuxs <biyuanh@qq.com> - 1.18.2-5
- Rebuild to match installed release (drop ackerman/nexus)
* Sat Oct 17 2026 Maomaokuxs <biyuanh@qq.com> - 1.18.2-1
- Initial package (repack official upstream DEB)
