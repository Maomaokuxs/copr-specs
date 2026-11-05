Name:           hyprutils
Version:        0.14.3
Release:        1%{?dist}
Summary:        Hyprland C++ utility library

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprutils
Source0:        https://github.com/hyprwm/hyprutils/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(pixman-1)

%description
hyprutils is the core C++ utility library shared by Hyprland
ecosystem projects (hyprlang, hyprgraphics, hyprlock, hypridle).

%package devel
Summary:        Development files for hyprutils
Requires:       %{name} = %{version}-%{release}

%description devel
Headers, CMake config and pkg-config file for developing
against hyprutils.

%prep
%autosetup -n hyprutils-%{version}

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libhyprutils.so.*

%files devel
%{_includedir}/hyprutils/
%{_libdir}/libhyprutils.so
%{_libdir}/pkgconfig/hyprutils.pc

%changelog
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 0.14.3-1
- Update to 0.14.3

* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 0.14.2-1
- Initial package (clone for biyuan/software)
