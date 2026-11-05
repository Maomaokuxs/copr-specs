Name:           sarasa-term-fonts
Version:        1.0.43
Release:        1%{?dist}
Summary:        Sarasa Term CJK programming font (terminal)

License:        OFL-1.1
URL:            https://github.com/be5invis/Sarasa-Gothic
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/SarasaTerm-TTF-%{version}.zip
Source1:        https://raw.githubusercontent.com/be5invis/Sarasa-Gothic/v%{version}/LICENSE#/sarasa-term-LICENSE

BuildArch:      noarch
BuildRequires:  unzip

%description
Sarasa Term SC (更纱黑体终端·简体中文) is the Simplified Chinese
terminal-emulator variant of the Sarasa Gothic CJK programming
font family, with half-width latin glyphs for clean terminal
rendering. Other locales ship as sarasa-term-{j,k,tc,hc,cl}
subpackages.

%package -n sarasa-term-j
Summary:        Sarasa Term Japanese programming font

%description -n sarasa-term-j
Sarasa Term J (Japanese) terminal variant.

%package -n sarasa-term-k
Summary:        Sarasa Term Korean programming font

%description -n sarasa-term-k
Sarasa Term K (Korean) terminal variant.

%package -n sarasa-term-tc
Summary:        Sarasa Term Traditional Chinese programming font

%description -n sarasa-term-tc
Sarasa Term TC (Traditional Chinese) terminal variant.

%package -n sarasa-term-hc
Summary:        Sarasa Term Hong Kong Cantonese programming font

%description -n sarasa-term-hc
Sarasa Term HC (Hong Kong Cantonese) terminal variant.

%package -n sarasa-term-cl
Summary:        Sarasa Term Classical orthography programming font

%description -n sarasa-term-cl
Sarasa Term CL (Classical orthography) terminal variant.

%prep
%setup -q -c -n %{name}-%{version} -T
unzip -q -o %{SOURCE0} 'SarasaTerm*.ttf'
cp %{SOURCE1} LICENSE

%build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/sarasa-term
install -m 644 SarasaTermSC-*.ttf %{buildroot}%{_datadir}/fonts/sarasa-term/
for loc in J K TC HC CL; do
    lower=$(echo $loc | tr 'A-Z' 'a-z')
    mkdir -p %{buildroot}%{_datadir}/fonts/sarasa-term-$lower
    install -m 644 SarasaTerm$loc-*.ttf %{buildroot}%{_datadir}/fonts/sarasa-term-$lower/
done

%files
%license LICENSE
%{_datadir}/fonts/sarasa-term/

%files -n sarasa-term-j
%license LICENSE
%{_datadir}/fonts/sarasa-term-j/

%files -n sarasa-term-k
%license LICENSE
%{_datadir}/fonts/sarasa-term-k/

%files -n sarasa-term-tc
%license LICENSE
%{_datadir}/fonts/sarasa-term-tc/

%files -n sarasa-term-hc
%license LICENSE
%{_datadir}/fonts/sarasa-term-hc/

%files -n sarasa-term-cl
%license LICENSE
%{_datadir}/fonts/sarasa-term-cl/

%changelog
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.43-1
- Update to 1.0.43

* Sat Oct 03 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.42-1
- Update to 1.0.42

* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.41-1
- Initial package
