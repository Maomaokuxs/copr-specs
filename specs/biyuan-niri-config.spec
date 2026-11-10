%global commit 6b4bb2b8b75bf2b5890ad83f0e1bd2948378a7fe

Name:           biyuan-niri-config
Version:        20260922
Release:        2%{?dist}
Summary:        Biyuan niri desktop environment configs

License:        MIT
URL:            https://github.com/Maomaokuxs/Biyuan-niri-desktop
# Pinned commit of Biyuan-niri-desktop (no tags yet).
# Bump Version (date) + %%commit together on updates.
Source0:        https://github.com/Maomaokuxs/Biyuan-niri-desktop/archive/%{commit}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       stow

%description
Config templates and wallpapers for the Biyuan niri desktop
(niri + quickshell bar, waybar fallback, mako, rofi, kitty,
fastfetch, starship, waypaper, hypridle/hyprlock, xdg-desktop-portal).
Files live under %{_datadir}/biyuan-niri-desktop/; run
biyuan-niri-deploy as your user to link them into $HOME
(existing files are backed up first).

%prep
%setup -q -n Biyuan-niri-desktop-%{commit}

%build

%install
mkdir -p %{buildroot}%{_datadir}/biyuan-niri-desktop
cp -a dotfiles wallpapers %{buildroot}%{_datadir}/biyuan-niri-desktop/
mkdir -p %{buildroot}%{_bindir}
install -m 755 packaging/biyuan-niri-deploy %{buildroot}%{_bindir}/biyuan-niri-deploy

%files
%license LICENSE
%{_datadir}/biyuan-niri-desktop/
%{_bindir}/biyuan-niri-deploy

%package -n biyuan-niri-desktop
Summary:        Biyuan niri desktop environment (meta package)
Requires:       %{name} = %{version}-%{release}
Requires:       niri
Requires:       quickshell
Requires:       waybar
Requires:       rofi
Requires:       kitty
Requires:       mako
Requires:       fastfetch
Requires:       stow
Requires:       wl-clipboard
Requires:       grim
Requires:       slurp
Requires:       xdg-desktop-portal-wlr
Recommends:     starship
Recommends:     hyprlock
Recommends:     hypridle
Recommends:     awww
Recommends:     waypaper
Recommends:     hellwal
Recommends:     jetbrainsmono-nerd-fonts
Recommends:     fcitx5

%description -n biyuan-niri-desktop
Meta package pulling in everything for the Biyuan niri desktop.
Hard requirements come from Fedora official repos; Recommends
cover third-party repos (terra, eddievs/hyprland, biyuan/software)
and are skipped silently when unavailable. After install, run
biyuan-niri-deploy as your user, then log into a niri session.

%files -n biyuan-niri-desktop

%post -n biyuan-niri-desktop
echo "Biyuan niri desktop installed. Run 'biyuan-niri-deploy' as your user,"
echo "then log into a niri session (first login initializes wallpaper/theme)."

%changelog
* Tue Nov 10 2026 Maomaokuxs <biyuanh@qq.com> - 20260922-2
- Update pinned commit after history rewrite
* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 20260922-1
- Initial package (niri desktop configs, quickshell default bar)
