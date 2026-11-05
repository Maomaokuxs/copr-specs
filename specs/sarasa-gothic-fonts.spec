Name:           sarasa-gothic-fonts
Version:        1.0.43
Release:        1%{?dist}
Summary:        Sarasa Gothic CJK programming font

License:        OFL-1.1
URL:            https://github.com/be5invis/Sarasa-Gothic
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/Sarasa-TTC-%{version}.zip
Source1:        https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/v%{version}/LICENSE#/sarasa-gothic-LICENSE

BuildArch:      noarch
BuildRequires:  unzip

%description
Sarasa Gothic (更纱黑体) is a CJK programming font based on
Source Han Sans and Iosevka, shipping TrueType Collections
covering Latin, kana and CJK glyphs.

%prep
%setup -q -c -n %{name}-%{version} -T
unzip -q %{SOURCE0} 'Sarasa-*.ttc'
cp %{SOURCE1} LICENSE

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/sarasa-gothic
install -m 644 Sarasa-*.ttc %{buildroot}%{_datadir}/fonts/sarasa-gothic/

%files
%license LICENSE
%{_datadir}/fonts/sarasa-gothic/

%changelog
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.43-1
- Update to 1.0.43

* Sat Oct 03 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.42-1
- Update to 1.0.42

* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.41-1
- Initial package (clone terra's fonts into biyuan/software)
