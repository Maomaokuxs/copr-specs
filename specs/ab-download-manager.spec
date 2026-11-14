%global debug_package %{nil}
%global jbr_dir jbrsdk_jcef-25.0.3-linux-x64-b508.4

Name:           ab-download-manager
Version:        1.11.4
Release:        1%{?dist}
Summary:        A Download Manager that speeds up your downloads

License:        Apache-2.0
URL:            https://abdownloadmanager.com
Source0:        https://github.com/amir1376/ab-download-manager/archive/refs/tags/v%{version}.tar.gz
Source1:        https://services.gradle.org/distributions/gradle-9.2.1-bin.zip
Source2:        abdownloadmanager.desktop
Source3:        https://cache-redirector.jetbrains.com/intellij-jbr/%{jbr_dir}.tar.gz

ExclusiveArch:  x86_64

Requires:       libXrender
Requires:       libXtst
Requires:       harfbuzz
Requires:       fontconfig
Requires:       gtk3

BuildRequires:  git
BuildRequires:  unzip
BuildRequires:  desktop-file-utils

%description
AB Download Manager is a desktop app that helps you manage and organize
your downloads more efficiently than ever before.

%prep
%autosetup -n ab-download-manager-%{version}

# Init dummy git repo (gradle needs git tags for versioning)
git init -q
git config user.email "builder@localhost"
git config user.name "RPM Builder"
git add .
git commit -qm "RPM build"
git tag v%{version}

# Extract Gradle and JBR
unzip -q %{SOURCE1} -d %{_builddir}
tar -xf %{SOURCE3} -C %{_builddir}

%build
export JAVA_HOME=%{_builddir}/%{jbr_dir}
export PATH=$JAVA_HOME/bin:$PATH
export SKIP_ANDROID_BUILD=true
./gradlew --no-daemon createReleaseFolderForCi

%install
tar -xf build/ci-release/binaries/ABDownloadManager_*_linux_x64.tar.gz
mkdir -p %{buildroot}/opt/abdownloadmanager
cp -r ABDownloadManager/* %{buildroot}/opt/abdownloadmanager/

# dbus-java forbids two transport providers for the same protocol on the
# classpath (upstream bundles both junixsocket and native-unixsocket, which
# crashes D-Bus init with TransportRegistrationException when opening the
# directory picker). Drop the native one; junixsocket supports FD passing.
rm -f %{buildroot}/opt/abdownloadmanager/lib/app/dbus-java-transport-native-unixsocket-*.jar

# Install icon
install -Dm644 desktop/app/icons/icon.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/abdownloadmanager.png

# Install desktop file
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/abdownloadmanager.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/abdownloadmanager.desktop

# Symlink to /usr/bin
mkdir -p %{buildroot}%{_bindir}
ln -s ../../opt/abdownloadmanager/bin/ABDownloadManager %{buildroot}%{_bindir}/abdownloadmanager

%files
/opt/abdownloadmanager/
/usr/share/icons/hicolor/512x512/apps/abdownloadmanager.png
/usr/share/applications/abdownloadmanager.desktop
/usr/bin/abdownloadmanager

%changelog
* Sat Nov 14 2026 Maomaokuxs <biyuanh@qq.com> - 1.11.4-1
- Update to 1.11.4
* Thu Oct 15 2026 Maomaokuxs <biyuanh@qq.com> - 1.11.1-1
- Update to 1.11.1
* Mon Oct 12 2026 Maomaokuxs <biyuanh@qq.com> - 1.11.0-2
- Drop dbus-java-transport-native-unixsocket jar: two UNIX socket transport
  providers on the classpath crash D-Bus init (TransportRegistrationException)
  when opening the directory picker; keep junixsocket which supports FD passing
* Mon Oct 12 2026 Maomaokuxs <biyuanh@qq.com> - 1.11.0-1
- Initial package
