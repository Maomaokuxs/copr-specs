Name:           hyprgraphics
Version:        0.6.0
Release:        1%{?dist}
Summary:        Hyprland graphics / image loading library

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprgraphics
Source0:        https://github.com/hyprwm/hyprgraphics/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)

%description
hyprgraphics is the image loading and rendering helper library
of the Hyprland ecosystem (JPEG, PNG, WebP, SVG, JXL, AVIF/HEIF),
used by hyprlock and others.

%package devel
Summary:        Development files for hyprgraphics
Requires:       %{name} = %{version}-%{release}

%description devel
Headers and pkg-config file for developing against hyprgraphics.

%prep
%autosetup -n hyprgraphics-%{version}

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/libhyprgraphics.so.*

%files devel
%{_includedir}/hyprgraphics/
%{_libdir}/libhyprgraphics.so
%{_libdir}/pkgconfig/hyprgraphics.pc

%changelog
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 0.6.0-1
- Update to 0.6.0

* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 0.5.1-1
- Initial package (clone for biyuan/software)
