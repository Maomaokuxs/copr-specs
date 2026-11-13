%global debug_package %{nil}
%global __os_install_post %{nil}
%global __arch_install_post %{nil}

Name:           obsidian
Version:        1.15.1
Release:        1%{?dist}
Summary:        Obsidian - a powerful knowledge base on top of a local folder of plain text Markdown files

License:        Proprietary
URL:            https://obsidian.md
Source0:        https://github.com/obsidianmd/obsidian-releases/releases/download/v%{version}/obsidian_%{version}_amd64.deb

ExclusiveArch:  x86_64

BuildRequires:  binutils
BuildRequires:  desktop-file-utils
BuildRequires:  xz
Requires:       alsa-lib, at-spi2-core, gtk3, libXScrnSaver, libnotify, mesa-libgbm, nss, xdg-utils
Requires:       libXtst, libuuid
Requires:       hicolor-icon-theme
AutoReqProv:    no

%description
Obsidian 官方 Linux 客户端。内容来自官方发布的 deb 安装包，
仅重新打包，不修改任何程序文件。

安装位置：/opt/Obsidian

%prep
rm -rf %{name}-%{version}
mkdir %{name}-%{version}
cd %{name}-%{version}
ar x %{SOURCE0}
tar xf data.tar.xz

%build

%install
cd %{name}-%{version}
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -a opt %{buildroot}/
mkdir -p %{buildroot}%{_datadir}
cp -a usr/share/applications %{buildroot}%{_datadir}/
cp -a usr/share/icons %{buildroot}%{_datadir}/
cp -a usr/share/mime %{buildroot}%{_datadir}/
# 终端里也能直接敲 obsidian 启动
mkdir -p %{buildroot}%{_bindir}
ln -s /opt/Obsidian/obsidian %{buildroot}%{_bindir}/obsidian

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/md.obsidian.Obsidian.desktop

%post
update-desktop-database -q %{_datadir}/applications || :
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :

%postun
update-desktop-database -q %{_datadir}/applications || :
touch --no-create %{_datadir}/icons/hicolor || :
gtk-update-icon-cache -q %{_datadir}/icons/hicolor 2>/dev/null || :

%files
%attr(4755,root,root) /opt/Obsidian/chrome-sandbox
/opt/Obsidian/
/usr/bin/obsidian
%{_datadir}/applications/md.obsidian.Obsidian.desktop
%{_datadir}/icons/hicolor/*/apps/obsidian.png
%{_datadir}/mime/packages/obsidian.xml

%changelog
* Fri Nov 13 2026 Maomaokuxs <biyuanh@qq.com> - 1.15.1-1
- Update to 1.15.1
* Tue Nov 10 2026 Maomaokuxs <biyuanh@qq.com> - 1.15.0-1
- Update to 1.15.0
* Thu Oct 22 2026 Maomaokuxs <biyuanh@qq.com> - 1.14.4-1
- Initial package: repackage official Linux deb, no program changes
