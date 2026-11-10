Name:           starship
Version:        1.27.0
Release:        2%{?dist}
Summary:        Minimal, fast, customizable shell prompt

License:        ISC
URL:            https://github.com/starship/starship
Source0:        https://github.com/starship/starship/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  rust

%description
Starship is a minimal, blazing-fast and customizable prompt for
any shell (bash, fish, zsh, PowerShell, ...), showing git status,
language versions and more at a glance.

%prep
%autosetup -n starship-%{version} -p1

%build
cargo build --release --locked

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 target/release/starship %{buildroot}%{_bindir}/starship
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
./target/release/starship completions bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
./target/release/starship completions zsh > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
./target/release/starship completions fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files
%license LICENSE
%doc README.md
%{_bindir}/starship
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%changelog
* Tue Nov 10 2026 Maomaokuxs <biyuanh@qq.com> - 1.27.0-2
- Rebuild to match installed release (drop ackerman/nexus)
* Sun Oct 18 2026 Wed Sep 23 2026 Maomaokuxs - 1.27.0-1
- Update to 1.27.0
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 1.26.0-1
- Initial package (clone terra's package into biyuan/software)
