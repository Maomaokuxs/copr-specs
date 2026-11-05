Name:           miyu
Version:        0.7.4
Release:        1%{?dist}

# Upstream Arch pkgrel embedded in the release asset name
%global pkgrel 1
Summary:        2D anime-style AI assistant in your terminal

License:        MIT
URL:            https://github.com/SHORiN-KiWATA/Miyu

Source0:        https://github.com/SHORiN-KiWATA/Miyu/releases/download/v%{version}/miyu-%{version}-%{pkgrel}-x86_64.pkg.tar.zst

%description
Miyu is a 2D anime-style AI assistant living in your terminal,
powered by large language models.

%prep
mkdir -p %{name}-%{version}
cd %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/miyu

# 解压 Arch 包，提取二进制和数据文件
tar xf %{SOURCE0} --zstd
install -m 755 usr/bin/miyu %{buildroot}%{_bindir}/miyu
cp -a usr/share/miyu/* %{buildroot}%{_datadir}/miyu/ 2>/dev/null || true

%files
%{_bindir}/miyu
%{_datadir}/miyu/

%changelog
* Thu Nov 05 2026 Maomaokuxs <biyuanh@qq.com> - 0.7.4-1
- Update to 0.7.4

* Thu Oct 22 2026 Maomaokuxs <biyuanh@qq.com> - 0.7.1-1
- Update to 0.7.1

* Sat Oct 03 2026 Maomaokuxs <biyuanh@qq.com> - 0.7.0-1
- Update to 0.7.0

* Tue Sep 22 2026 Maomaokuxs <biyuanh@qq.com> - 0.6.2-1
- Update to 0.6.2 (upstream pkgrel is now 1)

* Sat Sep 19 2026 Maomaokuxs <biyuanh@qq.com> - 0.6.0-1
- Update to 0.6.0 (upstream pkgrel is now 2)

* Fri Aug 28 2026 Maomaokuxs <biyuanh@qq.com> - 0.4.6-1
- Update to 0.4.6

* Fri Aug 28 2026 Maomaokuxs <biyuanh@qq.com> - 0.4.5-1
- Update to 0.4.5

* Sun Jul 26 2026 Maomaokuxs <biyuanh@qq.com> - 0.3.0-1
- Update to 0.3.0
