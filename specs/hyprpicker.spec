Name:           hyprpicker
Version:        0.4.8
Release:        1%{?dist}
Summary:        Hyprland screen color picker

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprpicker
Source0:        https://github.com/hyprwm/hyprpicker/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hyprwayland-scanner >= 0.4.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(hyprutils) >= 0.2.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.37
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%description
hyprpicker is Hyprland's screen color picker: click anywhere to
copy the color in hex, rgb, hsl or cmyk format to the clipboard.

%prep
%autosetup -n hyprpicker-%{version} -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/hyprpicker
%{_mandir}/man1/hyprpicker.1*

%changelog
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 0.4.8-1
- Update to 0.4.8

* Thu Sep 24 2026 Maomaokuxs <biyuanh@qq.com> - 0.4.7-1
- Initial package
