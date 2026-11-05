%global debug_package %{nil}

Name:           rime-ice
Version:        2026.10.31
Release:        2%{?dist}
Summary:        Simplified Chinese input schema for Rime (Wusong Pinyin)

License:        GPL-3.0-only
URL:            https://github.com/iDvel/rime-ice
Source0:        https://github.com/iDvel/rime-ice/releases/download/nightly/full.zip

BuildArch:      noarch
Requires:       librime
Requires:       librime-lua

%description
Rime Ice (雾凇拼音) is a long-maintained simplified Chinese input
schema and dictionary for Rime, offering pinyin, double-pinyin
and auxiliary-code input modes.

%prep
mkdir -p %{name}-%{version}
cd %{name}-%{version}
unzip -q %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{_datadir}/rime-data/rime-ice
mkdir -p %{buildroot}%{_bindir}
cd %{name}-%{version}
for d in */; do [ "$d" != "BUILDROOT/" ] && [ "$d" != "SPECPARTS/" ] && cp -a "$d" %{buildroot}%{_datadir}/rime-data/rime-ice/; done
cp -a ./*.yaml ./*.txt ./*.lua 2>/dev/null %{buildroot}%{_datadir}/rime-data/rime-ice/ || true

# 激活脚本
cat > %{buildroot}%{_bindir}/rime-ice-enable <<'EOF'
#!/bin/bash
DST="$HOME/.local/share/fcitx5/rime"
SRC="/usr/share/rime-data/rime-ice"
mkdir -p "$DST"
for f in "$SRC"/*; do
    ln -sf "$f" "$DST/$(basename "$f")"
done
echo "rime-ice 已启用，请执行 fcitx5-remote -r"
EOF
chmod +x %{buildroot}%{_bindir}/rime-ice-enable

%post
if [ -n "$SUDO_USER" ]; then
    DST=$(eval echo ~$SUDO_USER)/.local/share/fcitx5/rime
    mkdir -p "$DST"
    for f in %{_datadir}/rime-data/rime-ice/*; do
        ln -sf "$f" "$DST/$(basename "$f")" 2>/dev/null
    done
    echo "rime-ice 已自动部署到 $DST"
fi

%files
%dir %{_datadir}/rime-data/rime-ice
%{_datadir}/rime-data/rime-ice/
%{_bindir}/rime-ice-enable

%changelog
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 2026.10.31-2
- Require librime-lua (rime-ice schemas use lua_processor/translator/filter)
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 2026.10.31-1
- Update to 2026.10.31

* Wed Oct 07 2026 Maomaokuxs <biyuanh@qq.com> - 2026.10.05-1
- Update nightly snapshot to 2026.10.05

* Sat Oct 03 2026 Maomaokuxs <biyuanh@qq.com> - 2026.09.25-1
- Update nightly snapshot to 2026.09.25

* Fri Aug 28 2026 Maomaokuxs <biyuanh@qq.com> - 2026.06.30-1
- Update nightly snapshot to 2026.06.30

* Wed Jul 09 2025 Maomaokuxs <biyuanh@qq.com> - 2025.05.21-1
- Initial packaging
