Name:           babry
Version:        0.1.9
Release:        1%{?dist}
Summary:        Smart boundary-aware screenshot tool for Linux Wayland

License:        Apache-2.0
URL:            https://github.com/kregonia/babry
Source0:        https://raw.githubusercontent.com/kregonia/babry/v%{version}/LICENSE

ExclusiveArch:  x86_64

Requires:       fontconfig
Requires:       libxkbcommon
Requires:       libwayland-client

BuildRequires:  curl

%description
Babry is a smart boundary-aware screenshot tool for Linux Wayland.

%prep
curl -sL -o babry-amd64-linux https://github.com/kregonia/babry/releases/download/v%{version}/babry-amd64-linux-v%{version}
chmod +x babry-amd64-linux

%build

%install
install -Dm755 babry-amd64-linux %{buildroot}%{_bindir}/babry
install -Dm644 %{SOURCE0} %{buildroot}%{_licensedir}/%{name}/LICENSE

%files
%{_bindir}/babry
%{_licensedir}/%{name}/LICENSE

%changelog
* Sun Nov 08 2026 Maomaokuxs <biyuanh@qq.com> - 0.1.9-1
- Update to 0.1.9

* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 0.1.7-1
- Update to 0.1.7

* Sat Oct 17 2026 Biyuan <biyuan@example.com> - 0.1.4-1
- Update to 0.1.4
* Thu Oct 15 2026 Biyuan <biyuan@example.com> - 0.1.1-1
- Update to 0.1.1
- Initial package
