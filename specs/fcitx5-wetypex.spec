Name:           fcitx5-wetypex
Version:        3.0.1.684
Release:        5%{?dist}
Summary:        WeTypeX native Linux input method for Fcitx5 (WeChat input method compatibility)

License:        MIT AND curl AND ISC AND BSD-2-Clause AND Apache-2.0
URL:            https://github.com/panxuc/fcitx5-wetypex
Source0:        https://github.com/panxuc/fcitx5-wetypex/releases/download/v3.0.1.684-5/fcitx5-wetypex-3.0.1.684.tar.gz
Source1:        https://github.com/mheily/libkqueue/archive/46a3e130f88b0b0742575dcb01d77e336538024b.tar.gz#/libkqueue-46a3e130f88b0b0742575dcb01d77e336538024b.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  pkgconf-pkg-config
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  libime-devel
BuildRequires:  json-c-devel
BuildRequires:  openssl-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libcxx-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  layer-shell-qt-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(libcurl)

Requires:       glibc
Requires:       libcxx
Requires:       openssl-libs
Requires:       ca-certificates
Requires:       json-c
Requires:       fcitx5
Requires:       fcitx5-qt-libfcitx5qt6widgets
Requires:       libime
Requires:       qt6-qtbase
Requires:       qt6-qtsvg
Requires:       qt6-qtwebengine
Requires:       layer-shell-qt
Requires:       bubblewrap
Requires:       util-linux
Requires:       python3
Requires:       python3-fonttools
Requires:       python3-pillow
Requires:       fontconfig
Requires:       libwayland-client
Requires:       pipewire-utils
Requires:       /usr/bin/ffmpeg
Requires:       wl-clipboard
Requires:       libnotify
Requires:       polkit

%description
WeTypeX is a community (non-official, not endorsed by Tencent)
compatibility layer that runs the WeChat input method engine on
Linux through Fcitx5. This package contains only the open-source
adapter code (MIT); it does not ship any Tencent engine, dictionary
or resource files. After installation, run
`fcitx5-wetypex-setup --download --accept-upstream-license` to
download the official macOS package from Tencent and prepare the
runtime in the user's home directory, then add WeTypeX in the
Fcitx5 configuration.

%prep
%setup -q -n %{name}-%{version}
# Vendor libkqueue: upstream fetches it from Git at build time,
# which is not available in the COPR buildroot. Pin the exact
# commit used by upstream (see CMakeLists.txt).
mkdir -p vendor
tar -xzf %{SOURCE1} -C vendor

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=lib64 \
    -DWETYPE_LAYER_SHELL=ON \
    -DWETYPE_BUNDLED_CURL=OFF \
    -DFETCHCONTENT_SOURCE_DIR_KQUEUE=%{_builddir}/%{name}-%{version}/vendor/libkqueue-46a3e130f88b0b0742575dcb01d77e336538024b
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/fcitx5-wetypex-settings.desktop

%files
%license LICENSE NOTICE
%doc README.md
%{_bindir}/fcitx5-wetypex-*
%{_libdir}/fcitx5/wetypex.so
%{_libdir}/fcitx5/qt6/libwetypexconfig.so
%{_libdir}/fcitx5-wetypex/
%{_datadir}/fcitx5/addon/wetypex.conf
%{_datadir}/fcitx5/inputmethod/wetypex.conf
%{_datadir}/fcitx5/themes/wetypex-light/
%{_datadir}/fcitx5/themes/wetypex-dark/
%{_datadir}/fcitx5-wetypex/
%{_datadir}/applications/fcitx5-wetypex-settings.desktop
%{_datadir}/icons/hicolor/*/apps/fcitx5-wetypex.png
%{_datadir}/icons/hicolor/scalable/apps/fcitx5-wetypex*.svg
%{_datadir}/doc/fcitx5-wetypex/
%{_datadir}/licenses/fcitx5-wetypex/

%changelog
* Fri Nov 13 2026 Maomaokuxs <biyuanh@qq.com> - 3.0.1.684-5
- Update to upstream 3.0.1.684-5
* Thu Nov 12 2026 Maomaokuxs <biyuanh@qq.com> - 3.0.1.684-4
- Update to upstream 3.0.1.684-4
* Sun Nov 08 2026 Maomaokuxs <biyuanh@qq.com> - 2.2.3.657-17
- Update to upstream 2.2.3.657-17

* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 2.2.3.657-16
- Initial package (upstream 2.2.3.657, release 16; system libcurl, vendored libkqueue)
