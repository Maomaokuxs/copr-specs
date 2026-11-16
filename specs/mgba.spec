Name:           mgba
Version:        0.10.5
Release:        1%{?dist}
Summary:        Game Boy Advance emulator
License:        MPL-2.0
URL:            https://mgba.io
Source0:        https://github.com/mgba-emu/mgba/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconf-pkg-config
BuildRequires:  SDL2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  libpng-devel
BuildRequires:  zlib-devel
BuildRequires:  libzip-devel
BuildRequires:  sqlite-devel
BuildRequires:  libedit-devel
BuildRequires:  lua-devel
BuildRequires:  libelf-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libepoxy-devel
BuildRequires:  xz-devel

%description
mGBA is a Game Boy Advance emulator focusing on speed and accuracy.
It also emulates the original Game Boy and Game Boy Color.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DBUILD_TEST=OFF
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.mgba.mGBA.desktop

%files
%{_bindir}/mgba
%{_bindir}/mgba-qt
%{_libdir}/libmgba.so
%{_libdir}/libmgba.so.*
%{_includedir}/mgba/
%{_includedir}/mgba-util/
%{_datadir}/mgba/
%{_datadir}/applications/io.mgba.mGBA.desktop
%{_datadir}/icons/hicolor/*/apps/io.mgba.mGBA.png
%{_mandir}/man6/mgba*.6*
%{_docdir}/%{name}/

%changelog
* Mon Nov 16 2026 Maomaokuxs <biyuanh@qq.com> - 0.10.5-1
- Initial package
