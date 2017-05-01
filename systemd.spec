Name:           systemd
Version:        233
Release:        122
License:        GPL-2.0 LGPL-2.1 MIT
Summary:        System and service manager
Url:            http://www.freedesktop.org/wiki/Software/systemd
Group:          base/shell
Source0:        https://github.com/systemd/systemd/archive/v233.tar.gz
Source1:        20-pci-vendor-model.hwdb
BuildRequires:  filesystem-chroot
BuildRequires:  tzdata
BuildRequires:  autoconf
BuildRequires:  automake-dev automake m4 libtool libtool-dev
BuildRequires:  dbus-dev
BuildRequires:  dbus-dev32
BuildRequires:  gettext-dev
BuildRequires:  gettext-bin
BuildRequires:  gperf
BuildRequires:  intltool
BuildRequires:  intltool-dev
BuildRequires:  kmod-dev
BuildRequires:  kmod-dev32
BuildRequires:  acl-dev
BuildRequires:  acl-dev32
BuildRequires:  libcap-dev
BuildRequires:  libcap-dev32
BuildRequires:  libcgroup-dev
BuildRequires:  libffi-dev
BuildRequires:  libgcrypt-dev
BuildRequires:  libgcrypt-dev32
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  glib-bin
BuildRequires:  bzip2-dev
BuildRequires:  xz-dev
BuildRequires:  lz4-dev
BuildRequires:  Linux-PAM-dev
BuildRequires:  Linux-PAM-dev32
BuildRequires:  readline-dev
BuildRequires:  pkgconfig(zlib)
BuildRequires:  zlib-dev32
BuildRequires:  shadow
BuildRequires:  util-linux-dev
BuildRequires:  util-linux-dev32
BuildRequires:  pkg-config-dev
BuildRequires:  libxslt-bin docbook-xml
BuildRequires:  perl(XML::Parser)
BuildRequires:  util-linux-extras
BuildRequires:  cryptsetup-dev
BuildRequires:  curl-dev
BuildRequires:  libgpg-error-dev
BuildRequires:  gnu-efi
BuildRequires:  gnu-efi-dev
BuildRequires:  elfutils-dev
BuildRequires:  iptables-dev
BuildRequires:  iptables-dev32
BuildRequires:  gcc-dev32
BuildRequires:  gcc-libgcc32
BuildRequires:  gcc-libstdc++32
BuildRequires:  glibc-dev32
BuildRequires:  glibc-libc32

Requires(post): glibc-utils
Requires(post): shadow
Requires:       clr-systemd-config

Patch0001: 0001-journal-raise-compression-threshold.patch
Patch0002: 0002-journal-clearout-drop-kmsg.patch
Patch0003: 0003-core-use-mmap-to-load-files.patch
Patch0004: 0004-Makefile.am-drop-pam-nsswitch-ship-legacy-tmpfiles.patch
Patch0005: 0005-journal-flush-var-kmsg-after-starting.patch
Patch0006: 0006-tmpfiles-fix-etc.conf-for-stateless.patch
Patch0007: 0007-logind-pam-fix-systemd-user-to-include-common-sessio.patch
Patch0008: 0008-analyze-increase-precision.patch
Patch0009: 0009-configure.ac-disable-pie.patch
Patch0010: 0010-sd-event-return-malloc-memory-reserves-when-main-loo.patch
Patch0011: 0011-tmpfiles-create-locale-cache-dir.patch
Patch0012: 0012-efi-boot-generator-Do-not-automount-boot-partition.patch
Patch0013: 0013-core-do-not-apply-presets.patch
Patch0014: 0014-locale-setup-set-default-locale-to-a-unicode-one.patch
Patch0015: 0015-autoconf-add-option-to-disable-journald-authenticati.patch
Patch0016: 0016-mount-setup-mount-kernel-fs-by-default.patch
Patch0017: 0017-Ship-default-services-in-system-unit-dir.patch
Patch0018: 0018-bootctl-Add-force-option-to-enable-chroot-install-re.patch
Patch0019: 0019-kernel-install-Support-alternate-root-usage-via-SUBD.patch
Patch0020: 0020-bootctl-Handle-gummiboot-systemd-migration.patch
Patch0021: 0021-tmpfiles-Make-var-cache-ldconfig-world-readable.patch
Patch0022: 0022-Do-not-use-gold-to-link.patch
Patch0023: 0023-Set-a-default-unique-hostname-when-it-is-either-clr-.patch
Patch0024: 0024-Add-RDRAND-support-as-an-alternative-to-dev-urandom.patch
Patch0025: 0025-more-udev-children-workers.patch
Patch0026: 0026-not-load-iptables.patch
Patch0027: 0027-force-write-resovl.conf-at-boot.patch
Patch0028: 0028-Add-journal-flush-service-for-Microsoft-Azure-VMs.patch
Patch0029: 0029-Disable-systemd-resolved-as-default-resolver.patch
Patch0030: 0030-Enable-BBR-Bottleneck-Bandwidth-and-RTT.patch
Patch0031: 0031-network-online-complete-once-one-link-is-online-not-.patch
Patch0032: 0032-DHCP-retry-faster.patch
Patch0033: timesync-no-libm.patch

%description
System and service manager.

%package libs
License:        GPL-2.0 and LGPL-2.1 and MIT
Summary:        System and service manager
Group:          base/shell

%description libs
System and service manager.

%package dev
License:        GPL-2.0 and LGPL-2.1 and MIT
Summary:        System and service manager
Group:          devel
Requires:       %{name} = %{version}-%{release}
Requires:       systemd-libs = %{version}-%{release}

%description dev
System and service manager.

%package lib32
License:        GPL-2.0 and LGPL-2.1 and MIT
Summary:        System and service manager
Group:          base/shell

%description lib32
System and service manager.

%package dev32
License:        GPL-2.0 and LGPL-2.1 and MIT
Summary:        System and service manager
Group:          devel
Requires:       %{name} = %{version}-%{release}
Requires:       systemd-lib32 = %{version}-%{release}

%description dev32
System and service manager.

%package doc
License:        GPL-2.0 and LGPL-2.1 and MIT
Summary:        System and service manager
Group:          doc

%description doc
System and service manager.

%package locale
Summary:        locale component for systemd package
Group:          doc

%description locale
locale component for systemd package

%package extras
Summary:        extras component for systemd package
Group:          doc

%description extras
extras component for systemd package

%package hwdb
Summary:        hwdb component for systemd package
Group:          base/shell

%description hwdb
hwdb component for systemd package

%package boot
Summary:         efi boot component for systemd package

%description boot
efi boot component for systemd package

%package coredump
Summary:         coredump component for systemd package

%description coredump
coredump component for systemd package

%package polkit
Summary:        polkit component for systemd package
Group:          doc

%description polkit
polkit component for systemd package

%prep

%setup -q -n %{name}-%{version}

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
%patch0006 -p1
%patch0007 -p1
%patch0008 -p1
%patch0009 -p1
%patch0010 -p1
%patch0011 -p1
%patch0012 -p1
%patch0013 -p1
%patch0014 -p1
%patch0015 -p1
%patch0016 -p1
%patch0017 -p1
%patch0018 -p1
%patch0019 -p1
%patch0020 -p1
%patch0021 -p1
%patch0022 -p1
%patch0023 -p1
%patch0024 -p1
%patch0025 -p1
%patch0026 -p1
%patch0027 -p1
%patch0028 -p1
%patch0029 -p1
%patch0030 -p1
%patch0031 -p1
%patch0032 -p1
%patch0033 -p1

pushd ..
cp -a  %{name}-%{version}  build32
popd

%build


./autogen.sh
%configure CFLAGS="$CFLAGS -fno-semantic-interposition -Os -fno-tree-vectorize" \
    --enable-pam \
    --disable-smack \
    --disable-silent-rules \
    --disable-xz \
    --disable-lz4 \
    --enable-coredump \
    --disable-split-usr \
    --without-python \
    --enable-rdrand \
    --sysconfdir=/etc \
    --with-sysvinit-path="" \
    --with-sysvrcnd-path="" \
    ac_cv_path_KILL=/usr/bin/kill \
    --disable-gcrypt \
    --disable-libcryptsetup \
    --disable-microhttpd \
    --disable-quotacheck \
    --with-dbuspolicydir=/usr/share/dbus-1/system.d \
    --localstatedir=%{_localstatedir} \
    --enable-elfutils \
    --with-ntp-servers='gateway. 0.clearlinux.pool.ntp.org 1.clearlinux.pool.ntp.org 2.clearlinux.pool.ntp.org 3.clearlinux.pool.ntp.org' \
    --with-efi-ldsdir=/usr/lib --with-efi-libdir=/usr/lib \
    --with-pamlibdir=/usr/lib64/security \
    --without-kill-user-processes \
    --enable-polkit \
    --with-default-hierarchy=legacy

# Disable unified cgroups, as a guess that that's why we are seeing pid 1 aborts
# This regresses bootspeed.
#    --enable-unified


make %{?_smp_mflags}

# then do the 32 bit build
pushd ../build32/
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"

./autogen.sh
%configure CFLAGS="$CFLAGS -fno-semantic-interposition -Os -fno-tree-vectorize" \
    --libdir=/usr/lib32 \
    --disable-pam \
    --disable-smack \
    --disable-silent-rules \
    --disable-xz \
    --disable-lz4 \
    --disable-coredump \
    --disable-split-usr \
    --without-python \
    --disable-rdrand \
    --sysconfdir=/etc \
    --with-sysvinit-path="" \
    --with-sysvrcnd-path="" \
    ac_cv_path_KILL=/usr/bin/kill \
    --disable-gcrypt \
    --disable-libcryptsetup \
    --disable-microhttpd \
    --disable-quotacheck \
    --with-dbuspolicydir=/usr/share/dbus-1/system.d \
    --disable-libcurl \
    --disable-libiptc \
    --localstatedir=%{_localstatedir} \
    --disable-elfutils \
    --with-ntp-servers='gateway. 0.clearlinux.pool.ntp.org 1.clearlinux.pool.ntp.org 2.clearlinux.pool.ntp.org 3.clearlinux.pool.ntp.org' \
    --with-efi-ldsdir=/usr/lib --with-efi-libdir=/usr/lib \
    --with-pamlibdir=/usr/lib64/security \
    --without-kill-user-processes \
    --disable-polkit \
    --with-default-hierarchy=legacy

make %{?_smp_mflags}
popd


%check
make V=1 VERBOSE=1 %{?_smp_mflags} check || :

%install
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd

%make_install

# need to provide /usr/bin/init
mkdir -p %{buildroot}/usr/bin
ln -s /usr/lib/systemd/systemd %{buildroot}/usr/bin/init

# compat symlinks
ln -s /usr/bin/systemctl %{buildroot}/usr/bin/halt
ln -s /usr/bin/systemctl %{buildroot}/usr/bin/poweroff
ln -s /usr/bin/systemctl %{buildroot}/usr/bin/reboot
ln -s /usr/bin/systemctl %{buildroot}/usr/bin/runlevel
ln -s /usr/bin/systemctl %{buildroot}/usr/bin/shutdown

# All users should be defined in the systemd-config package
rm -f %{buildroot}/usr/lib/sysusers.d/basic.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd-remote.conf
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
rmdir %{buildroot}/etc/udev/hwdb.d
rmdir %{buildroot}/etc/udev/rules.d
rmdir %{buildroot}/etc/udev

# Do not ship broken symlink
rm -f %{buildroot}/etc/xdg/systemd/user

# Move config file into system PAM location
mv %{buildroot}/etc/pam.d %{buildroot}%{_datadir}/.

cp %{SOURCE1} %{buildroot}/usr/lib/udev/hwdb.d/
rm -f %{buildroot}/usr/lib/udev/hwdb.d/20-usb-vendor-model.hwdb

# exclude hwdb for pci device id vendors - we don't want this in containers
# or VMs. An update trigger will remake the full hwdb for non-vm cases.
mkdir -p %{buildroot}/usr/lib/udev/hwdb.d/20
mv %{buildroot}/usr/lib/udev/hwdb.d/20-* %{buildroot}/usr/lib/udev/hwdb.d/20

# Pre-generate and pre-ship hwdb, to speed up first boot
./systemd-hwdb --root %{buildroot} --usr || ./udevadm hwdb --root %{buildroot} --update --usr

# restore 20-* hwdb files
mv %{buildroot}/usr/lib/udev/hwdb.d/20/* %{buildroot}/usr/lib/udev/hwdb.d/
rmdir %{buildroot}/usr/lib/udev/hwdb.d/20

# Compute catalog
./journalctl --root %{buildroot} --update-catalog

# Add a hook to integrate telemetrics crashprobe with systemd-coredump
mkdir -p %{buildroot}/usr/lib/systemd/system-coredump
ln -s ../../../bin/crashprobe %{buildroot}/usr/lib/systemd/system-coredump/crashprobe

# only supported plugin is "clear.install"
rm -rvf %{buildroot}/usr/lib/kernel

# Remove unused systemd plka
rm -rvf %{buildroot}/var/lib/polkit-1

%find_lang systemd

%files
%exclude /usr/lib/systemd/system/sysinit.target.wants/ldconfig.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-firstboot.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-sysusers.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-hwdb-update.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-update-done.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-journal-catalog-update.service
%exclude /usr/lib/systemd/system/system-update-cleanup.service
%exclude /usr/lib/systemd/system/systemd-journal-catalog-update.service
%exclude /usr/lib/systemd/system/systemd-firstboot.service
%exclude /usr/lib/systemd/system/systemd-sysusers.service
%exclude /usr/lib/systemd/system/systemd-hwdb-update.service
%exclude /usr/lib/systemd/system/systemd-update-done.service
%exclude /usr/lib/systemd/systemd-update-done
%exclude /usr/lib/systemd/systemd-coredump

%{_datadir}/bash-completion/completions/*
/usr/share/zsh/site-functions/*

%{_datadir}/pam.d/systemd-user

/usr/bin/halt
/usr/bin/init
/usr/bin/poweroff
/usr/bin/reboot
/usr/bin/runlevel
/usr/bin/shutdown
/usr/bin/busctl
/usr/bin/hostnamectl
/usr/bin/journalctl
/usr/bin/kernel-install
/usr/bin/localectl
/usr/bin/loginctl
/usr/bin/machinectl
/usr/bin/networkctl
/usr/bin/systemctl
/usr/bin/systemd-analyze
/usr/bin/systemd-ask-password
/usr/bin/systemd-cat
/usr/bin/systemd-cgls
/usr/bin/systemd-cgtop
/usr/bin/systemd-delta
/usr/bin/systemd-detect-virt
/usr/bin/systemd-escape
/usr/bin/systemd-inhibit
/usr/bin/systemd-machine-id-setup
/usr/bin/systemd-mount
/usr/bin/systemd-notify
/usr/bin/systemd-nspawn
/usr/bin/systemd-path
/usr/bin/systemd-resolve
/usr/bin/systemd-run
/usr/bin/systemd-socket-activate
/usr/bin/systemd-stdio-bridge
/usr/bin/systemd-tmpfiles
/usr/bin/systemd-tty-ask-password-agent
/usr/bin/systemd-umount
/usr/bin/timedatectl
/usr/bin/udevadm

/usr/lib/sysctl.d/50-default.conf
/usr/lib/systemd/catalog/systemd.catalog
/usr/lib/systemd/catalog/systemd.bg.catalog
/usr/lib/systemd/network/80-container-host0.network
/usr/lib/systemd/network/80-container-ve.network
/usr/lib/systemd/network/80-container-vz.network
/usr/lib/systemd/network/99-default.link
/usr/lib/systemd/system-generators/systemd-debug-generator
/usr/lib/systemd/system-generators/systemd-fstab-generator
/usr/lib/systemd/system-generators/systemd-getty-generator
/usr/lib/systemd/system-generators/systemd-gpt-auto-generator
%exclude /usr/lib/systemd/system-generators/systemd-hibernate-resume-generator
/usr/lib/systemd/system-preset/90-systemd.preset
/usr/lib/systemd/system/autovt@.service
/usr/lib/systemd/system/basic.target
/usr/lib/systemd/system/bluetooth.target
/usr/lib/systemd/system/console-getty.service
/usr/lib/systemd/system/container-getty@.service
/usr/lib/systemd/system/ctrl-alt-del.target
/usr/lib/systemd/system/dbus-org.freedesktop.hostname1.service
/usr/lib/systemd/system/dbus-org.freedesktop.locale1.service
/usr/lib/systemd/system/dbus-org.freedesktop.login1.service
/usr/lib/systemd/system/dbus-org.freedesktop.machine1.service
/usr/lib/systemd/system/dbus-org.freedesktop.network1.service
/usr/lib/systemd/system/dbus-org.freedesktop.resolve1.service
/usr/lib/systemd/system/dbus-org.freedesktop.timedate1.service
/usr/lib/systemd/system/debug-shell.service
/usr/lib/systemd/system/default.target
/usr/lib/systemd/system/emergency.service
/usr/lib/systemd/system/emergency.target
/usr/lib/systemd/system/exit.target
/usr/lib/systemd/system/final.target
/usr/lib/systemd/system/getty.target
/usr/lib/systemd/system/getty@.service
/usr/lib/systemd/system/graphical.target
/usr/lib/systemd/system/halt.target
/usr/lib/systemd/system/hibernate.target
/usr/lib/systemd/system/hybrid-sleep.target
/usr/lib/systemd/system/machines.target

/usr/lib/systemd/system/initrd-cleanup.service
/usr/lib/systemd/system/initrd-fs.target
/usr/lib/systemd/system/initrd-parse-etc.service
/usr/lib/systemd/system/initrd-root-fs.target
/usr/lib/systemd/system/initrd-switch-root.service
/usr/lib/systemd/system/initrd-switch-root.target
/usr/lib/systemd/system/initrd-udevadm-cleanup-db.service
/usr/lib/systemd/system/initrd.target
/usr/lib/systemd/system/initrd-root-device.target

/usr/lib/systemd/system/getty.target.wants/getty@tty1.service

/usr/lib/systemd/system/kexec.target
/usr/lib/systemd/system/kmod-static-nodes.service
/usr/lib/systemd/system/local-fs-pre.target
/usr/lib/systemd/system/local-fs.target
/usr/lib/systemd/system/local-fs.target.wants/systemd-remount-fs.service
/usr/lib/systemd/system/local-fs.target.wants/tmp.mount
/usr/lib/systemd/system/machine.slice

/usr/lib/systemd/system/busnames.target
/usr/lib/systemd/system/busnames.target.wants/org.freedesktop.hostname1.busname
/usr/lib/systemd/system/busnames.target.wants/org.freedesktop.locale1.busname
/usr/lib/systemd/system/busnames.target.wants/org.freedesktop.login1.busname
/usr/lib/systemd/system/busnames.target.wants/org.freedesktop.machine1.busname
/usr/lib/systemd/system/busnames.target.wants/org.freedesktop.network1.busname
/usr/lib/systemd/system/busnames.target.wants/org.freedesktop.resolve1.busname
/usr/lib/systemd/system/busnames.target.wants/org.freedesktop.systemd1.busname
/usr/lib/systemd/system/busnames.target.wants/org.freedesktop.timedate1.busname
/usr/lib/systemd/system/org.freedesktop.hostname1.busname
/usr/lib/systemd/system/org.freedesktop.locale1.busname
/usr/lib/systemd/system/org.freedesktop.login1.busname
/usr/lib/systemd/system/org.freedesktop.machine1.busname
/usr/lib/systemd/system/org.freedesktop.network1.busname
/usr/lib/systemd/system/org.freedesktop.resolve1.busname
/usr/lib/systemd/system/org.freedesktop.systemd1.busname
/usr/lib/systemd/system/org.freedesktop.timedate1.busname

/usr/lib/systemd/system/multi-user.target
/usr/lib/systemd/system/multi-user.target.wants/getty.target
/usr/lib/systemd/system/multi-user.target.wants/remote-fs.target
/usr/lib/systemd/system/multi-user.target.wants/systemd-ask-password-wall.path
/usr/lib/systemd/system/multi-user.target.wants/systemd-logind.service
/usr/lib/systemd/system/multi-user.target.wants/systemd-user-sessions.service
/usr/lib/systemd/system/multi-user.target.wants/systemd-networkd.service
/usr/lib/systemd/system/multi-user.target.wants/systemd-resolved.service

/usr/lib/systemd/system/network-online.target
/usr/lib/systemd/system/network-online.target.wants/systemd-networkd-wait-online.service
/usr/lib/systemd/system/network-pre.target
/usr/lib/systemd/system/network.target
/usr/lib/systemd/system/nss-lookup.target
/usr/lib/systemd/system/nss-user-lookup.target

/usr/lib/systemd/system/paths.target
/usr/lib/systemd/system/poweroff.target
/usr/lib/systemd/system/printer.target
/usr/lib/systemd/system/proc-sys-fs-binfmt_misc.automount
/usr/lib/systemd/system/proc-sys-fs-binfmt_misc.mount
/usr/lib/systemd/system/quotaon.service
/usr/lib/systemd/system/reboot.target
/usr/lib/systemd/system/remote-fs-pre.target
/usr/lib/systemd/system/remote-fs.target
/usr/lib/systemd/system/rescue.service
/usr/lib/systemd/system/rescue.target
/usr/lib/systemd/system/rpcbind.target

/usr/lib/systemd/system/serial-getty@.service
/usr/lib/systemd/system/shutdown.target
/usr/lib/systemd/system/sigpwr.target
/usr/lib/systemd/system/sleep.target
/usr/lib/systemd/system/slices.target
/usr/lib/systemd/system/smartcard.target

/usr/lib/systemd/system/sockets.target
/usr/lib/systemd/system/sockets.target.wants/*.socket

/usr/lib/systemd/system/sound.target
/usr/lib/systemd/system/suspend.target
/usr/lib/systemd/system/swap.target

/usr/lib/systemd/system/sysinit.target
/usr/lib/systemd/system/sysinit.target.wants/*

/usr/lib/systemd/system/syslog.socket
/usr/lib/systemd/system/system.slice
/usr/lib/systemd/system/systemd-*
/usr/lib/systemd/system/time-sync.target
/usr/lib/systemd/system/timers.target
/usr/lib/systemd/system/timers.target.wants/systemd-tmpfiles-clean.timer
/usr/lib/systemd/system/tmp.mount
/usr/lib/systemd/system/umount.target
/usr/lib/systemd/system/user.slice
/usr/lib/systemd/system/user@.service
/usr/lib/systemd/systemd
/usr/lib/systemd/systemd-*
/usr/lib/systemd/resolv.conf
%exclude /usr/lib/systemd/systemd-journal-upload
/usr/lib/systemd/user/*.service
/usr/lib/systemd/user/*.target

/usr/lib/systemd/user-environment-generators/*

/usr/lib/systemd/libsystemd-shared-%{version}.so

/usr/lib/tmpfiles.d/*.conf

/usr/lib/udev/ata_id
/usr/lib/udev/scsi_id
/usr/lib/udev/hwdb.bin
/usr/lib/udev/rules.d/50-udev-default.rules
/usr/lib/udev/rules.d/60-drm.rules
/usr/lib/udev/rules.d/60-persistent-input.rules
/usr/lib/udev/rules.d/60-persistent-storage.rules
/usr/lib/udev/rules.d/64-btrfs.rules
/usr/lib/udev/rules.d/70-mouse.rules
/usr/lib/udev/rules.d/70-power-switch.rules
/usr/lib/udev/rules.d/70-touchpad.rules
/usr/lib/udev/rules.d/70-uaccess.rules
/usr/lib/udev/rules.d/71-seat.rules
/usr/lib/udev/rules.d/73-seat-late.rules
/usr/lib/udev/rules.d/75-net-description.rules
/usr/lib/udev/rules.d/80-drivers.rules
/usr/lib/udev/rules.d/80-net-setup-link.rules
/usr/lib/udev/rules.d/90-vconsole.rules
/usr/lib/udev/rules.d/99-systemd.rules

/usr/lib/udev/rules.d/60-block.rules
/usr/lib/udev/rules.d/60-evdev.rules
/usr/lib/udev/rules.d/60-serial.rules
/usr/lib/udev/rules.d/60-sensor.rules


%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/dbus-1/system-services/*
%{_datadir}/dbus-1/services/*

/usr/lib/environment.d/99-environment.conf

%{_datadir}/systemd/*

%exclude /var/lib/systemd/catalog/database

%files libs
/usr/lib64/libnss_myhostname.so.2
/usr/lib64/libnss_mymachines.so.2
/usr/lib64/libnss_resolve.so.2
/usr/lib64/libnss_systemd.so.2

/usr/lib64/libudev.so.*
/usr/lib64/libsystemd.so.*

/usr/lib64/security/pam_systemd.so

%files dev
/usr/include/*.h
/usr/include/systemd/*.h
/usr/lib64/*.so
/usr/lib/rpm/macros.d/macros.systemd
/usr/lib64/pkgconfig/*.pc

%files lib32
/usr/lib32/libnss_myhostname.so.2
/usr/lib32/libnss_mymachines.so.2
/usr/lib32/libnss_resolve.so.2
/usr/lib32/libnss_systemd.so.2

/usr/lib32/libudev.so.*
/usr/lib32/libsystemd.so.*


%files dev32
/usr/lib32/*.so
/usr/lib32/pkgconfig/*.pc

%files doc
%{_datadir}/doc/systemd/*
%{_mandir}/*/*

%files extras
/usr/bin/systemd-firstboot
/usr/lib/systemd/systemd-journal-upload
/usr/bin/systemd-sysusers
/usr/lib/systemd/system-generators/systemd-system-update-generator
/usr/lib/systemd/system/ldconfig.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/ldconfig.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-firstboot.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-sysusers.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-update-done.service
/usr/lib/systemd/system/system-update.target
/usr/lib/systemd/system/systemd-firstboot.service
/usr/lib/systemd/system/systemd-sysusers.service
/usr/lib/systemd/system/systemd-update-done.service
/usr/lib/systemd/systemd-update-done
/usr/lib/systemd/system/local-fs.target.wants/var-lib-machines.mount
/usr/lib/systemd/system/var-lib-machines.mount

%files hwdb
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-hwdb-update.service
%exclude /usr/lib/systemd/system/systemd-hwdb-update.service
/usr/bin/systemd-hwdb
/usr/lib/udev/hwdb.d/*.hwdb
/usr/lib/udev/rules.d/60-cdrom_id.rules
/usr/lib/udev/rules.d/60-persistent-alsa.rules
/usr/lib/udev/rules.d/60-persistent-storage-tape.rules
/usr/lib/udev/rules.d/60-persistent-v4l.rules
/usr/lib/udev/rules.d/75-probe_mtd.rules
/usr/lib/udev/rules.d/78-sound-card.rules
/usr/lib/udev/cdrom_id
/usr/lib/udev/collect
/usr/lib/udev/mtd_probe
/usr/lib/udev/v4l_id


%files locale -f systemd.lang
/usr/lib/systemd/catalog/systemd.fr.catalog
/usr/lib/systemd/catalog/systemd.it.catalog
/usr/lib/systemd/catalog/systemd.pl.catalog
/usr/lib/systemd/catalog/systemd.pt_BR.catalog
/usr/lib/systemd/catalog/systemd.ru.catalog
/usr/lib/systemd/catalog/systemd.be.catalog
/usr/lib/systemd/catalog/systemd.be@latin.catalog
/usr/lib/systemd/catalog/systemd.zh_TW.catalog
/usr/lib/systemd/catalog/systemd.zh_CN.catalog

%files boot
/usr/bin/bootctl
/usr/lib/systemd/boot/efi/

%files coredump
/usr/bin/coredumpctl
/usr/lib/sysctl.d/50-coredump.conf
/usr/lib/systemd/systemd-coredump
/usr/lib/systemd/system-coredump/crashprobe

%files polkit
/usr/share/polkit-1/actions/org.freedesktop.hostname1.policy
/usr/share/polkit-1/actions/org.freedesktop.locale1.policy
/usr/share/polkit-1/actions/org.freedesktop.login1.policy
/usr/share/polkit-1/actions/org.freedesktop.machine1.policy
/usr/share/polkit-1/actions/org.freedesktop.systemd1.policy
/usr/share/polkit-1/actions/org.freedesktop.timedate1.policy
/usr/share/polkit-1/rules.d/systemd-networkd.rules
