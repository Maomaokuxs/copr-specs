Name:           sarasa-mono-fonts
Version:        1.0.43
Release:        1%{?dist}
Summary:        Sarasa Mono CJK programming font (monospaced)

License:        OFL-1.1
URL:            https://github.com/be5invis/Sarasa-Gothic
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/SarasaMono-TTF-%{version}.zip
Source1:        https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/v%{version}/LICENSE#/sarasa-mono-LICENSE

BuildArch:      noarch
BuildRequires:  unzip

%description
Sarasa Mono SC (更纱黑体等宽·简体中文) is the Simplified Chinese
monospaced variant of the Sarasa Gothic CJK programming font
family, based on Source Han Sans and Iosevka. Other locales ship
as sarasa-mono-{j,k,tc,hc,cl} subpackages.

%package -n sarasa-mono-j
Summary:        Sarasa Mono Japanese programming font
%description -n sarasa-mono-j
Sarasa Mono J (Japanese) monospaced variant.

%package -n sarasa-mono-k
Summary:        Sarasa Mono Korean programming font
%description -n sarasa-mono-k
Sarasa Mono K (Korean) monospaced variant.

%package -n sarasa-mono-tc
Summary:        Sarasa Mono Traditional Chinese programming font
%description -n sarasa-mono-tc
Sarasa Mono TC (Traditional Chinese) monospaced variant.

%package -n sarasa-mono-hc
Summary:        Sarasa Mono Hong Kong Cantonese programming font
%description -n sarasa-mono-hc
Sarasa Mono HC (Hong Kong Cantonese) monospaced variant.

%package -n sarasa-mono-cl
Summary:        Sarasa Mono Classical orthography programming font
%description -n sarasa-mono-cl
Sarasa Mono CL (Classical orthography) monospaced variant.

%prep
%setup -q -c -n %{name}-%{version} -T
unzip -q -o %{SOURCE0} 'SarasaMono*.ttf'
cp %{SOURCE1} LICENSE

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/sarasa-mono
install -m 644 SarasaMonoSC-*.ttf %{buildroot}%{_datadir}/fonts/sarasa-mono/
for loc in J K TC HC CL; do
    lower=$(echo $loc | tr 'A-Z' 'a-z')
    mkdir -p %{buildroot}%{_datadir}/fonts/sarasa-mono-$lower
    install -m 644 SarasaMono$loc-*.ttf %{buildroot}%{_datadir}/fonts/sarasa-mono-$lower/
done

%files
%license LICENSE
%{_datadir}/fonts/sarasa-mono/

%files -n sarasa-mono-j
%license LICENSE
%{_datadir}/fonts/sarasa-mono-j/

%files -n sarasa-mono-k
%license LICENSE
%{_datadir}/fonts/sarasa-mono-k/

%files -n sarasa-mono-tc
%license LICENSE
%{_datadir}/fonts/sarasa-mono-tc/

%files -n sarasa-mono-hc
%license LICENSE
%{_datadir}/fonts/sarasa-mono-hc/

%files -n sarasa-mono-cl
%license LICENSE
%{_datadir}/fonts/sarasa-mono-cl/

%changelog
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.43-1
- Update to 1.0.43

* Sat Oct 03 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.42-1
- Update to 1.0.42

* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.41-1
- Initial package
