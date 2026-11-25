%global debug_package %{nil}
%global assetdir %{name}-%{version}-x86_64-unknown-linux-musl-with-assets

Name:           wallust
Version:        3.5.2
Release:        1%{?dist}
Summary:        Generate colors from an image

License:        MIT
URL:            https://codeberg.org/explosion-mental/wallust
Source0:        https://codeberg.org/explosion-mental/wallust/releases/download/3.5.2/wallust-3.5.2-x86_64-unknown-linux-musl-with-assets.tar.gz
Source1:        https://codeberg.org/explosion-mental/wallust/raw/branch/master/LICENSE#/LICENSE

%description
wallust generates a color palette from an image and applies it to
applications through templates. It is a pywal replacement with
multiple backends and color spaces, a `wallust run` command and a
built-in pywal-compatible CLI.

%prep
%setup -q -c -T
cp %{SOURCE1} LICENSE
tar xzf %{SOURCE0}

%build

%install
install -D -m 755 %{assetdir}/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{assetdir}/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -D -m 644 %{assetdir}/man/%{name}-cs.1 %{buildroot}%{_mandir}/man1/%{name}-cs.1
install -D -m 644 %{assetdir}/man/%{name}-theme.1 %{buildroot}%{_mandir}/man1/%{name}-theme.1
install -D -m 644 %{assetdir}/man/%{name}-run.1 %{buildroot}%{_mandir}/man1/%{name}-run.1
install -D -m 644 %{assetdir}/man/%{name}.5 %{buildroot}%{_mandir}/man5/%{name}.5
install -D -m 644 %{assetdir}/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -m 644 %{assetdir}/completions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -D -m 644 %{assetdir}/completions/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%check
%{buildroot}%{_bindir}/%{name} --version

%files
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/%{name}-cs.1.gz
%{_mandir}/man1/%{name}-theme.1.gz
%{_mandir}/man1/%{name}-run.1.gz
%{_mandir}/man5/%{name}.5.gz
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
* Wed Nov 25 2026 Maomaokuxs <biyuanh@qq.com> - 3.5.2-1
- Initial package
