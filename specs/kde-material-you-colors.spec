%global debug_package %{nil}
%global __requires_exclude ^python3.*dist\\(python-magic\\)

Name:           kde-material-you-colors
Version:        2.3.0
Release:        5%{?dist}
Summary:        Automatic Material You color scheme generator for KDE Plasma

License:        GPL-3.0-or-later
URL:            https://github.com/luisbocanegra/kde-material-you-colors
Source0:        https://github.com/luisbocanegra/kde-material-you-colors/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

Requires:       python3-dbus
Requires:       python3-numpy
Requires:       python3-pillow
Requires:       python3-file-magic
Requires:       python3-gobject
Requires:       python3-materialyoucolor
Obsoletes:      python3-kde-material-you-colors < 2.3.0-4

%description
Automatic color scheme generator from your wallpaper for KDE Plasma,
powered by Google's Material You color utilities. Generates light and
dark themes for Plasma, Konsole, and pywal.

%prep
%setup -q -n kde-material-you-colors-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%{_bindir}/kde-material-you-colors
%{python3_sitelib}/kde_material_you_colors/
%{python3_sitelib}/kde_material_you_colors-%{version}*.dist-info/

%changelog
* Sun Nov 15 2026 Maomaokuxs <biyuanh@qq.com> - 2.3.0-5
- Revert python-magic requires exclude to double backslashes
* Sun Nov 15 2026 Maomaokuxs <biyuanh@qq.com> - 2.3.0-4
- Fix python-magic requires exclude (single backslashes)
- Obsolete terra python3 subpackage
* Sun Nov 15 2026 Maomaokuxs <biyuanh@qq.com> - 2.3.0-3
- Fix python-magic requires exclude for Python 3.15
* Sun Nov 15 2026 Maomaokuxs <biyuanh@qq.com> - 2.3.0-2
- Update to 2.3.0
* Fri Aug 28 2026 Maomaokuxs <biyuanh@qq.com> - 2.2.0-1
- Initial package