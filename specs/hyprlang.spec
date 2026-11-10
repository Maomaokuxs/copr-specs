Name:           hyprlang
Version:        0.6.8
Release:        2%{?dist}
Summary:        Hyprland config language library

License:        LGPL-3.0-only
URL:            https://github.com/hyprwm/hyprlang
Source0:        https://github.com/hyprwm/hyprlang/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(hyprutils) >= 0.7.1

%description
hyprlang is the configuration language library used by Hyprland
ecosystem projects for parsing their config files.

%package devel
Summary:        Development files for hyprlang
Requires:       %{name} = %{version}-%{release}

%description devel
Headers and pkg-config file for developing against hyprlang.

%prep
%autosetup -n hyprlang-%{version}

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libhyprlang.so.*

%files devel
%{_includedir}/hyprlang.hpp
%{_libdir}/libhyprlang.so
%{_libdir}/pkgconfig/hyprlang.pc

%changelog
* Tue Nov 10 2026 Maomaokuxs <biyuanh@qq.com> - 0.6.8-2
- Rebuild to match installed release (drop eddievs/hyprland)
* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 0.6.8-1
- Initial package (clone for biyuan/software)
