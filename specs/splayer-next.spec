%global debug_package %{nil}
%global __provides_exclude ^(%{_libdir}/%{name}/.*\.so)
%global __requires_exclude ^(libEGL|libGLESv2|libffmpeg|libvk_swiftshader|libvulkan|libnode).*

Name:           splayer-next
Version:        1.2.0
Release:        1%{?dist}
Summary:        Cross-platform desktop music player with rich lyric support

License:        AGPL-3.0-only
URL:            https://github.com/SPlayer-Dev/SPlayer-Next
Source0:        https://github.com/SPlayer-Dev/SPlayer-Next/releases/download/v%{version}/splayer-next-%{version}-x64.tar.gz
Source1:        https://raw.githubusercontent.com/Maomaokuxs/rpmbuild/main/assets/splayer-next/splayer-next-icon.png
Source2:        https://raw.githubusercontent.com/Maomaokuxs/rpmbuild/main/assets/splayer-next/splayer-next-LICENSE

BuildRequires:  desktop-file-utils

Requires:       alsa-lib
Requires:       mesa-libGL
Requires:       mesa-libEGL
Requires:       libxkbcommon
Requires:       dbus
Requires:       ffmpeg-libs
Requires:       pulseaudio-libs

%description
SPlayer-Next is a cross-platform desktop music player with rich lyric support,
broad audio format compatibility (MP3, FLAC, WAV, AAC, OGG, APE, etc.),
streaming server support (Subsonic/Navidrome/Jellyfin/Emby), and a
high-performance FFmpeg + Rust audio engine.

%prep
%setup -q -c -n %{name}-%{version}
cp %{SOURCE2} LICENSE

%build

%install
mkdir -p %{buildroot}%{_libdir}/%{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps

tar xzf %{SOURCE0} -C %{buildroot}%{_libdir}/%{name} --strip-components=1

ln -sf %{_libdir}/%{name}/SPlayer-Next %{buildroot}%{_bindir}/%{name}

install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<DESKTOP
[Desktop Entry]
Name=SPlayer-Next
Comment=Cross-platform desktop music player
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Music;Player;
MimeType=audio/aac;audio/flac;audio/mpeg;audio/ogg;audio/wav;audio/x-ape;
DESKTOP

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
if [ -f %{_libdir}/%{name}/chrome-sandbox ]; then
    chmod 4755 %{_libdir}/%{name}/chrome-sandbox 2>/dev/null || true
fi

%files
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 1.2.0-1
- Update to 1.2.0

* Fri Aug 28 2026 Maomaokuxs <biyuanh@qq.com> - 1.1.0-1
- Update to 1.1.0

* Wed Aug 12 2026 Maomaokuxs <biyuanh@qq.com> - 1.0.0-2
- Repackage official upstream v1.0.0 x64 tar.gz
