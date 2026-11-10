Name:           hyprlock
Version:        0.9.7
Release:        2%{?dist}
Summary:        Hyprland screen locker

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprlock
Source0:        https://github.com/hyprwm/hyprlock/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hyprwayland-scanner
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(hyprgraphics) >= 0.1.6
BuildRequires:  pkgconfig(hyprland-protocols) >= 0.6.0
BuildRequires:  pkgconfig(hyprlang) >= 0.6.0
BuildRequires:  pkgconfig(hyprutils) >= 0.11.0
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(sdbus-c++) >= 2.0.0
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.35
BuildRequires:  pkgconfig(xkbcommon)

%description
hyprlock is Hyprland's GPU-accelerated screen locker with
blur, background images, and per-monitor input fields.

%prep
%autosetup -n hyprlock-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/hyprlock
%config(noreplace) %{_sysconfdir}/pam.d/hyprlock
%{_datadir}/hypr/hyprlock.conf

%changelog
* Tue Nov 10 2026 Maomaokuxs <biyuanh@qq.com> - 0.9.7-2
- Rebuild against hyprgraphics 0.6.0 (soname .so.4 -> .so.5)
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 0.9.7-1
- Update to 0.9.7

* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 0.9.6-1
- Initial package (clone for biyuan/software)
