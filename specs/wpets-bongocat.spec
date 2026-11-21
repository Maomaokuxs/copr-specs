Name:           wpets-bongocat
Version:        6.2.0
Release:        1%{?dist}
Summary:        Classic Bongo Cat Wayland overlay (keyboard reactive pet)
License:        MIT
URL:            https://github.com/furudbat/wayland-vpets
Source0:        https://github.com/furudbat/wayland-vpets/archive/refs/tags/v6.2.0.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  wayland-devel
BuildRequires:  systemd-devel
BuildRequires:  python3
BuildRequires:  git-core
Requires:       systemd-udev
# 只装经典猫：上游 install 规则里 TARGETS bongocat 即经典版，
# dm/clippy/pkmn 等其他二进制默认不安装

%description
Classic Bongo Cat as a passive Wayland overlay: a cat at the screen
edge whose paws follow your real keyboard input. Layer-shell based,
so it is visible on all workspaces. Config lives at
~/.config/bongocat/bongocat.conf (see
%{_datadir}/bongocat/bongocat.conf.example). Keyboard capture needs
membership in the 'input' group: sudo usermod -a -G input $USER
(log out and back in), then list keyboards with bongocat-find-devices
and set keyboard_device= lines.

%prep
%autosetup -n wayland-vpets-6.2.0
# 上游写死 -march=native 会导致 COPR 构建机指令集超出用户 CPU(SIGILL)，
# 统一改成通用 x86-64
grep -rl -- '-march=native' . | xargs sed -i 's/-march=native/-march=x86-64 -mtune=generic/g'

%build
%cmake -DCMAKE_BUILD_TYPE=Release
# 必须全量编译：install 脚本引用了全部 target，只编 bongocat 会缺文件；
# 猫之外的二进制在 %install 里删掉，只发经典猫
%cmake_build

%install
%cmake_install
# 只留经典猫：删版本化副本、cmake 导出文件、其他宠物二进制
rm -rf %{buildroot}%{_bindir}/bongocat-6.2.0 %{buildroot}%{_libdir}/cmake
find %{buildroot}%{_bindir} -type f ! -name 'bongocat' ! -name 'bongocat-find-devices' -delete 2>/dev/null || true

%files
%license LICENSE
%{_bindir}/bongocat
%{_bindir}/bongocat-find-devices
%{_datadir}/bongocat/

%changelog
* Sat Nov 21 2026 Maomaokuxs <biyuanh@qq.com> - 6.2.0-1
- Update to 6.2.0

* Thu Sep 24 2026 Maomaokuxs <biyuanh@qq.com> - 5.0.2-2
- Replace -march=native with generic x86-64 (avoid SIGILL on user CPUs)

* Thu Sep 24 2026 Maomaokuxs <biyuanh@qq.com> - 5.0.2-1
- Initial package, classic bongocat only
