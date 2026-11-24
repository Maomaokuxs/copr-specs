Name:           python3-materialyoucolor
Version:        3.1.0
Release:        1%{?dist}
Summary:        Material You color generation in pure Python

License:        MIT
URL:            https://pypi.org/project/materialyoucolor/
Source0:        https://files.pythonhosted.org/packages/59/8e/9f4cba4a77c7ffb50c6af8b618fcf1a7a300e3b3c7500d9b74025ebdee48/materialyoucolor-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  gcc-c++
BuildRequires:  pybind11-devel
BuildRequires:  python3-pybind11

%description
Material You color generation algorithms in pure Python,
used by kde-material-you-colors to derive color schemes
from wallpapers.

%prep
%autosetup -n materialyoucolor-%{version} -p1

%build
# kde-material-you-colors 2.x requires the C++ QuantizeCelebi extension,
# so build it via pybind11 instead of the pure-Python flavor.
%pyproject_wheel

%install
%pyproject_install

%files
%license LICENSE
%{python3_sitearch}/materialyoucolor/
%{python3_sitearch}/materialyoucolor-%{version}*.dist-info/

%changelog
* Tue Nov 24 2026 Maomaokuxs <biyuanh@qq.com> - 3.1.0-1
- Update to 3.1.0

* Sat Oct 10 2026 Maomaokuxs <biyuanh@qq.com> - 3.0.4-5
- Build the C++ QuantizeCelebi extension (kde-material-you-colors 2.x requires it)
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 3.0.4-1
- Initial package (self-containment for kde-material-you-colors)
