Name:           gpu-screen-recorder
Version:        6.1.7
Release:        2%{?dist}
Summary:        ShadowPlay-like GPU screen recorder for Linux

License:        GPL-3.0-only
URL:            https://git.dec05eba.com/gpu-screen-recorder/about
Source0:        https://dec05eba.com/snapshot/gpu-screen-recorder.git.r1549.1d4946a.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  vulkan-headers
BuildRequires:  (ffmpeg-free-devel or ffmpeg-devel)
Requires(post): libcap

%description
ShadowPlay-like screen recorder for Linux, recording directly
from the GPU with near-zero performance impact. Supports
shadow-replay, streaming and hardware encoding (NVENC/AMF/VAAPI).

%prep
%setup -q -c -n %{name}-%{version} -T
tar xzf %{SOURCE0}

%build
%meson -Dcapabilities=false
%meson_build

%install
%meson_install

%post
setcap cap_sys_admin+ep %{_bindir}/gsr-kms-server || :

%files
%license LICENSE
%doc README.md
%{_datadir}/gpu-screen-recorder
%{_bindir}/gpu-screen-recorder
%{_bindir}/gsr-kms-server
%{_bindir}/gsr-cli
%{_includedir}/gsr/plugin.h
%{_userunitdir}/gpu-screen-recorder.service
%{_prefix}/lib/modprobe.d/gsr-nvidia.conf
%{_mandir}/man1/gsr-kms-server.1*
%{_mandir}/man1/gpu-screen-recorder.1*
%{_mandir}/man1/gsr-cli.1*

%changelog
* Tue Nov 10 2026 Maomaokuxs <biyuanh@qq.com> - 6.1.7-2
- Rebuild to match installed release (drop ackerman/nexus)
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 6.1.7-1
- Update to 6.1.7

* Thu Oct 22 2026 Maomaokuxs <biyuanh@qq.com> - 6.1.5-1
- Update to 6.1.5
* Thu Oct 15 2026 Maomaokuxs <biyuanh@qq.com> - 6.1.4-1
- Update to 6.1.4
* Mon Oct 12 2026 Maomaokuxs <biyuanh@qq.com> - 6.1.3-1
- Update snapshot to r1520.7f9405e (includes upstream 6.1.3)
* Wed Sep 30 2026 Maomaokuxs <biyuanh@qq.com> - 6.1.2-2
- Update snapshot to r1517.68dfeb9
* Wed Sep 23 2026 Maomaokuxs <biyuanh@qq.com> - 6.1.2-1
- Initial package (snapshot r1511.be3287d, system ffmpeg-free)
