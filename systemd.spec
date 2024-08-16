#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v18
# autospec commit: 356da62
#
Name     : systemd
Version  : 256
Release  : 415
URL      : https://github.com/systemd/systemd-stable/archive/v256/systemd-stable-256.tar.gz
Source0  : https://github.com/systemd/systemd-stable/archive/v256/systemd-stable-256.tar.gz
Source1  : systemd-timesyncd-fix-localstatedir.service
Source2  : no-hibernate.conf
Summary  : systemd System and Service Manager
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 MIT OFL-1.1
Requires: libcap
BuildRequires : Linux-PAM-dev
BuildRequires : Linux-PAM-dev32
BuildRequires : acl-dev
BuildRequires : acl-dev32
BuildRequires : buildreq-meson
BuildRequires : cryptsetup-dev
BuildRequires : curl-dev
BuildRequires : dbus-dev
BuildRequires : dbus-dev32
BuildRequires : docbook-xml
BuildRequires : elfutils-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : gettext-dev
BuildRequires : glib-bin
BuildRequires : glib-dev
BuildRequires : glib-dev32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : gnu-efi-staticdev
BuildRequires : gperf
BuildRequires : intltool
BuildRequires : intltool-dev
BuildRequires : iptables-dev
BuildRequires : iptables-dev32
BuildRequires : kmod-dev
BuildRequires : kmod-dev32
BuildRequires : libcap-dev
BuildRequires : libcap-dev32
BuildRequires : libcgroup-dev
BuildRequires : libffi-dev
BuildRequires : libfido2
BuildRequires : libfido2-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgcrypt-dev32
BuildRequires : libgpg-error-dev
BuildRequires : libmicrohttpd-dev
BuildRequires : libseccomp-dev
BuildRequires : libseccomp-dev32
BuildRequires : libxcrypt-dev32
BuildRequires : libxslt-bin
BuildRequires : llvm
BuildRequires : openssl-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(32p11-kit-1)
BuildRequires : pkgconfig(zlib)
BuildRequires : pypi(jinja2)
BuildRequires : pypi-lxml
BuildRequires : pypi-pyelftools
BuildRequires : python3
BuildRequires : readline-dev
BuildRequires : shadow
BuildRequires : tpm2-tss-dev
BuildRequires : util-linux-dev
BuildRequires : util-linux-dev32
BuildRequires : util-linux-extras
BuildRequires : zlib-dev32
BuildRequires : zstd-dev
BuildRequires : zstd-dev32
Patch1: 0001-journal-raise-compression-threshold.patch
Patch2: 0002-journal-Add-option-to-skip-boot-kmsg-events.patch
Patch3: 0003-core-use-mmap-to-load-files.patch
Patch4: 0005-journal-flush-var-kmsg-after-starting-disable-kmsg-f.patch
Patch5: 0006-logind-pam-fix-systemd-user-to-include-common-sessio.patch
Patch6: 0007-sd-event-return-malloc-memory-reserves-when-main-loo.patch
Patch7: 0008-efi-boot-generator-Do-not-automount-boot-partition.patch
Patch8: 0009-core-do-not-apply-presets.patch
Patch9: 0011-Ship-default-services-in-system-unit-dir.patch
Patch10: 0012-bootctl-Add-force-option-to-enable-chroot-install-re.patch
Patch11: 0013-tmpfiles-Make-var-cache-ldconfig-world-readable.patch
Patch12: 0014-Set-a-default-unique-hostname-when-it-is-either-clr-.patch
Patch13: 0016-not-load-iptables.patch
Patch14: 0018-Enable-BBR-Bottleneck-Bandwidth-and-RTT.patch
Patch15: 0019-network-online-complete-once-one-link-is-online-not-.patch
Patch16: 0020-DHCP-retry-faster.patch
Patch17: 0021-Remove-libm-memory-overhead.patch
Patch18: 0022-skip-not-present-ACPI-devices.patch
Patch19: 0023-Ensure-var-run-is-never-a-directory.patch
Patch20: 0024-Make-timesyncd-a-simple-service.patch
Patch21: 0027-Don-t-do-transient-hostnames-we-set-ours-already.patch
Patch22: 0028-don-t-use-libm-just-for-integer-exp10.patch
Patch23: 0029-Notify-systemd-earlier-that-resolved-is-ready.patch
Patch24: 0030-Hand-off-coredumps-to-a-wrapper-that-will-optionally.patch
Patch25: 0032-Do-not-enable-audit-by-default-in-the-journal.patch
Patch26: 0034-Localize-1-symbol.patch
Patch27: 0036-Disable-LLDP-listening-by-default.patch
Patch28: 0037-units-use-var-swapfile-if-found.patch
Patch29: elfsection.patch

%description
systemd System and Service Manager
WEB SITE:
https://systemd.io
GIT:
git@github.com:systemd/systemd.git
https://github.com/systemd/systemd

%prep
%setup -q -n systemd-stable-256
cd %{_builddir}/systemd-stable-256
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1
%patch -P 19 -p1
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 22 -p1
%patch -P 23 -p1
%patch -P 24 -p1
%patch -P 25 -p1
%patch -P 26 -p1
%patch -P 27 -p1
%patch -P 28 -p1
%patch -P 29 -p1
pushd ..
cp -a systemd-stable-256 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1722382004
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_CXXFLAGS=$CLEAR_INTERMEDIATE_CFLAGS
CLEAR_INTERMEDIATE_FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_FCFLAGS=$CLEAR_INTERMEDIATE_FFLAGS
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault-hierarchy=hybrid \
-Dsmack=false \
-Dsysvinit-path= \
-Dsysvrcnd-path= \
-Dxz=false \
-Dgcrypt=true \
-Dlz4=false \
-Dqrencode=false \
-Dpcre2=false \
-Dlibidn=false \
-Dlibidn2=false \
-Dman=true \
-Ddefault-kill-user-processes=false \
-Dntp-servers="_gateway gateway 0.clearlinux.pool.ntp.org 1.clearlinux.pool.ntp.org 2.clearlinux.pool.ntp.org 3.clearlinux.pool.ntp.org time.intel.com" \
-Ddefault-dnssec=no \
-Dzstd=true \
-Dsbat-distro=clearlinux \
-Dsbat-distro-summary="Clear Linux OS for Intel (R) Architecture" \
-Dsbat-distro-url=https://clearlinux.org/ \
-Dlink-networkd-shared=true \
-Dlink-timesyncd-shared=true \
-Dbootloader=true \
-Ddefault-user-shell=/usr/bin/bash \
-Ddebug-shell=/usr/bin/bash  builddir
ninja -v -C builddir
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Ddefault-hierarchy=hybrid \
-Dsmack=false \
-Dsysvinit-path= \
-Dsysvrcnd-path= \
-Dxz=false \
-Dgcrypt=true \
-Dlz4=false \
-Dqrencode=false \
-Dpcre2=false \
-Dlibidn=false \
-Dlibidn2=false \
-Dman=true \
-Ddefault-kill-user-processes=false \
-Dntp-servers="_gateway gateway 0.clearlinux.pool.ntp.org 1.clearlinux.pool.ntp.org 2.clearlinux.pool.ntp.org 3.clearlinux.pool.ntp.org time.intel.com" \
-Ddefault-dnssec=no \
-Dzstd=true \
-Dsbat-distro=clearlinux \
-Dsbat-distro-summary="Clear Linux OS for Intel (R) Architecture" \
-Dsbat-distro-url=https://clearlinux.org/ \
-Dlink-networkd-shared=true \
-Dlink-timesyncd-shared=true \
-Dbootloader=true \
-Ddefault-user-shell=/usr/bin/bash \
-Ddebug-shell=/usr/bin/bash -Dlibcryptsetup=false \
-Dgnutls=false \
-Dlibcurl=false \
-Delfutils=false \
-Dmicrohttpd=false \
-Dremote=false \
-Dxz=false \
-Dgcrypt=false \
-Dopenssl=false \
-Daudit=false \
-Dpolkit=false \
-Dzstd=false builddir
ninja -v -C builddir
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
ninja -C builddir test ||:

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_CXXFLAGS=$CLEAR_INTERMEDIATE_CFLAGS
CLEAR_INTERMEDIATE_FFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wno-error -Wl,-z,max-page-size=0x4000 -march=westmere"
CLEAR_INTERMEDIATE_FCFLAGS=$CLEAR_INTERMEDIATE_FFLAGS
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fno-lto "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fno-lto "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/systemd
cp %{_builddir}/systemd-stable-%{version}/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/systemd/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
cp %{_builddir}/systemd-stable-%{version}/LICENSE.LGPL2.1 %{buildroot}/usr/share/package-licenses/systemd/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/systemd-stable-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/systemd/ea97eb88ae53ec41e26f8542176ab986d7bc943a || :
cp %{_builddir}/systemd-stable-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/systemd/5aebbff6ecbe1754fc59dc9b27e1ea8692384d64 || :
cp %{_builddir}/systemd-stable-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/systemd/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/systemd-stable-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/systemd/5c6c38fa1b6ac7c66252c83d1203e997ae3d1c98 || :
cp %{_builddir}/systemd-stable-%{version}/LICENSES/MIT-0.txt %{buildroot}/usr/share/package-licenses/systemd/99942a5202ca4ca2f2025bbf35266bc225876236 || :
cp %{_builddir}/systemd-stable-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/systemd/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
cp %{_builddir}/systemd-stable-%{version}/LICENSES/OFL-1.1.txt %{buildroot}/usr/share/package-licenses/systemd/d9fe5ac0193fdebda45d1fe971d470beafdb2f8b || :
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/systemd-timesyncd-fix-localstatedir.service
mkdir -p %{buildroot}/usr/lib/systemd/sleep.conf.d
install -m644 %{_sourcedir}/no-hibernate.conf %{buildroot}/usr/lib/systemd/sleep.conf.d/
## Remove excluded files
rm -f %{buildroot}*/usr/bin/kernel-install
rm -f %{buildroot}*/usr/bin/systemd-firstboot
rm -f %{buildroot}*/usr/lib/rpm/macros.d/macros.systemd
rm -f %{buildroot}*/usr/lib/systemd/import-pubring.gpg
rm -f %{buildroot}*/usr/lib/systemd/system-generators/systemd-hibernate-resume-generator
rm -f %{buildroot}*/usr/lib/systemd/system-generators/systemd-system-update-generator
rm -f %{buildroot}*/usr/lib/systemd/system-generators/systemd-veritysetup-generator
rm -f %{buildroot}*/usr/lib/systemd/system/ldconfig.service
rm -f %{buildroot}*/usr/lib/systemd/system/systemd-firstboot.service
rm -f %{buildroot}*/usr/lib/systemd/system/systemd-hwdb-update.service
rm -f %{buildroot}*/usr/lib/systemd/system/systemd-journal-catalog-update.service
rm -f %{buildroot}*/usr/lib/systemd/system/systemd-sysusers.service
rm -f %{buildroot}*/usr/lib/systemd/system/systemd-tmpfiles-setup-dev.service
rm -f %{buildroot}*/usr/lib/systemd/system/systemd-update-done.service
rm -f %{buildroot}*/usr/lib/systemd/system/system-update-cleanup.service
rm -f %{buildroot}*/usr/lib/systemd/system/system-update.target
rm -f %{buildroot}*/usr/lib/systemd/systemd-update-done
rm -f %{buildroot}*/usr/lib/udev/hwdb.d/20-pci-vendor-model.hwdb
rm -f %{buildroot}*/usr/share/bash-completion/completions/kernel-install
rm -f %{buildroot}*/usr/share/zsh/site-functions/_kernel-install
rm -f %{buildroot}*/var/lib/systemd/catalog/database
rm -f %{buildroot}*/var/log/README
## install_append content

# All users should be defined in the systemd-config package
rm -f %{buildroot}/usr/lib/sysusers.d/basic.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd-remote.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd-coredump.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd-journal.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd-network.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd-oom.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd-resolve.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd-timesync.conf
rm -f %{buildroot}/usr/lib/sysusers.d/README
rmdir %{buildroot}/usr/lib/sysusers.d

# No external linking of this shared object should happen
rm -f %{buildroot}/usr/lib/systemd/libsystemd-shared.so

# These configuration files, are actually documentation only
# We have manpages for that
rm -f %{buildroot}/etc/systemd/journald.conf
rm -f %{buildroot}/etc/systemd/logind.conf
rm -f %{buildroot}/etc/systemd/resolved.conf
rm -f %{buildroot}/etc/systemd/system.conf
rm -f %{buildroot}/etc/systemd/timesyncd.conf
rm -f %{buildroot}/etc/systemd/user.conf
rm -f %{buildroot}/etc/udev/udev.conf
rm -f %{buildroot}/etc/udev/iocost.conf
rmdir %{buildroot}/etc/udev/hwdb.d
rmdir %{buildroot}/etc/udev/rules.d
rmdir %{buildroot}/etc/udev

# These are unwanted and would end up in -autostart, because %exclude isn't
# honored by -autostart auto subrpm
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/ldconfig.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-firstboot.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-hwdb-update.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-journal-catalog-update.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-sysusers.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-update-done.service
rm -f %{buildroot}/usr/lib/systemd/system/sysinit.target.wants/systemd-tmpfiles-setup-dev.service
rm -f %{buildroot}/usr/lib/systemd/system/sockets.target.wants/systemd-journald-audit.socket

# Do not ship broken symlinks
rm -f %{buildroot}/etc/xdg/systemd/user
rm -f %{buildroot}/usr/lib/environment.d/99-environment.conf

# Move config file into system PAM location
mv %{buildroot}/usr/lib/pam.d %{buildroot}/usr/share/.

# Move pc files to default pkgconfig dir
mv %{buildroot}/usr/share/pkgconfig/* %{buildroot}/usr/lib64/pkgconfig/
rmdir %{buildroot}/usr/share/pkgconfig/

# exclude hwdb for pci device id vendors - we don't want this in containers
# or VMs. An update trigger will remake the full hwdb for non-vm cases.
mkdir -p %{buildroot}/usr/lib/udev/hwdb.d/20
mv %{buildroot}/usr/lib/udev/hwdb.d/20-* %{buildroot}/usr/lib/udev/hwdb.d/20

# Pre-generate and pre-ship hwdb, to speed up first boot
builddir/udevadm hwdb --root %{buildroot} --update --usr

# restore 20-* hwdb files
mv %{buildroot}/usr/lib/udev/hwdb.d/20/* %{buildroot}/usr/lib/udev/hwdb.d/
rmdir %{buildroot}/usr/lib/udev/hwdb.d/20

# Compute catalog
builddir/journalctl --root %{buildroot} --update-catalog

# Add a hook to integrate telemetrics crashprobe with systemd-coredump
cp src/coredump/coredump-wrapper %{buildroot}/usr/lib/systemd/

# only supported plugin is "clear.install"
rm -rvf %{buildroot}/usr/lib/kernel

# Remove unused systemd plka
rm -rvf %{buildroot}/var/lib/polkit-1

# Services that are OK to restart after software update
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/systemd-timesyncd.service %{buildroot}/usr/share/clr-service-restart/systemd-timesyncd.service
ln -sf /usr/lib/systemd/system/systemd-resolved.service %{buildroot}/usr/share/clr-service-restart/systemd-resolved.service
ln -sf /usr/lib/systemd/system/systemd-udevd.service %{buildroot}/usr/share/clr-service-restart/systemd-udevd.service
ln -sf /usr/lib/systemd/system/systemd-journald.service %{buildroot}/usr/share/clr-service-restart/systemd-journald.service

# fix systemd-timesyncd v242 - dir expected, was symlink before in /var/state/timesync
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants
ln -s ../systemd-timesyncd-fix-localstatedir.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/systemd-timesyncd-fix-localstatedir.service

# remove catalog
rm -rvf %{buildroot}/var/lib/systemd
chmod a-x %{buildroot}/usr/share/man/man*/*
## install_append end

%files
%defattr(-,root,root,-)
