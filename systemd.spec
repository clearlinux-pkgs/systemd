Name:           systemd
Version:        229
Release:        66
License:        GPL-2.0 LGPL-2.1 MIT
Summary:        System and service manager
Url:            http://www.freedesktop.org/wiki/Software/systemd
Group:          base/shell
Source0:        https://github.com/systemd/systemd/archive/v229.tar.gz
Source1:        20-pci-vendor-model.hwdb
BuildRequires:  filesystem-chroot
BuildRequires:  tzdata
BuildRequires:  autoconf
BuildRequires:  automake-dev automake m4 libtool libtool-dev
BuildRequires:  dbus-dev
BuildRequires:  gettext-dev
BuildRequires:  gettext-bin
BuildRequires:  gperf
BuildRequires:  intltool
BuildRequires:  intltool-dev
BuildRequires:  kmod-dev
BuildRequires:  acl-dev
BuildRequires:  libcap-dev
BuildRequires:  libcgroup-dev
BuildRequires:  libffi-dev
BuildRequires:  libgcrypt-dev
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  glib-bin
BuildRequires:  bzip2-dev
BuildRequires:  xz-dev
BuildRequires:  lz4-dev
BuildRequires:  Linux-PAM-dev
BuildRequires:  readline-dev
BuildRequires:  pkgconfig(zlib)
BuildRequires:  shadow
BuildRequires:  util-linux-dev
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

Requires(post): glibc-utils
Requires(post): shadow
Requires:       clr-systemd-config
Patch01: 0001-bootchart-use-ms-units-in-a-few-places.patch
Patch02: 0002-journal-raise-compression-threshold.patch
Patch03: 0003-journal-clearout-drop-kmsg.patch
Patch04: 0004-core-use-mmap-to-load-files.patch
Patch05: 0005-udev-add-debug-processing-marks.patch
Patch06: 0006-Makefile.am-drop-pam-nsswitch-ship-legacy-tmpfiles.patch
Patch07: 0007-bootchart-mount-proc-early.patch
Patch08: 0008-journal-flush-var-kmsg-after-starting.patch
Patch09: 0009-tmpfiles-fix-etc.conf-for-stateless.patch
Patch10: 0010-logind-pam-fix-systemd-user-to-include-common-sessio.patch
Patch11: 0011-analyze-increase-precision.patch
Patch12: 0012-configure.ac-disable-pie.patch
Patch13: 0013-sd-event-return-malloc-memory-reserves-when-main-loo.patch
Patch14: 0014-tmpfiles-create-locale-cache-dir.patch
Patch15: 0015-efi-boot-generator-Do-not-automount-boot-partition.patch
Patch16: 0016-core-do-not-apply-presets.patch
Patch17: 0017-locale-setup-set-default-locale-to-a-unicode-one.patch
Patch18: 0018-bootchart-fix-per-cpu-small-scales.patch
Patch19: 0019-autoconf-add-option-to-disable-journald-authenticati.patch
Patch20: 0020-bootchart-drop-log_info-spam-to-serial-console.patch
Patch21: 0021-mount-setup-mount-kernel-fs-by-default.patch
Patch22: 0022-telemetrics-invoke-crash-probes.patch
Patch23: 0023-Add-kernel-efi-stub-generator-script.patch
Patch24: 0024-Ship-default-services-in-system-unit-dir.patch
Patch25: 0025-bootctl-Add-force-option-to-enable-chroot-install-re.patch
Patch26: 0026-kernel-install-Support-alternate-root-usage-via-SUBD.patch
Patch27: 0027-bootctl-Handle-gummiboot-systemd-migration.patch
Patch28: 0028-tmpfiles-Make-var-cache-ldconfig-world-readable.patch
Patch29: 0029-Do-not-use-gold-to-link.patch
Patch30: 0030-Set-a-default-unique-hostname-when-it-is-either-clr-.patch
Patch31: systemd-rdrand.patch

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

%package doc
License:        GPL-2.0 and LGPL-2.1 and MIT
Summary:        System and service manager
Group:          doc

%description doc
System and service manager.

%package locale
Summary:        locate component for systemd package
Group:          doc

%description locale
locale component for systemd package

%package extras
Summary:        locate component for systemd package
Group:          doc

%description extras
extras component for systemd package

%package boot
Summary:         efi boot component for systemd package

%description boot
efi boot component for systemd package

%package coredump
Summary:         coredump component for systemd package

%description coredump
coredump component for systemd package

%prep

%setup -q -n %{name}-%{version}
%patch01 -p1
%patch02 -p1
%patch03 -p1
%patch04 -p1
%patch05 -p1
%patch06 -p1
%patch07 -p1
%patch08 -p1
%patch09 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1

%build
./autogen.sh
%configure CFLAGS="$CFLAGS -fno-semantic-interposition -Os -fno-tree-vectorize" \
    --enable-pam \
    --disable-smack \
    --disable-silent-rules \
    --enable-xz \
    --enable-lz4 \
    --enable-coredump \
    --disable-kdbus \
    --disable-split-usr \
    --without-python \
    --enable-rdrand \
    --sysconfdir=%{_sysconfdir} \
    --with-sysvinit-path="" \
    --with-sysvrcnd-path="" \
    ac_cv_path_KILL=/usr/bin/kill \
    --enable-gcrypt \
    --disable-journald-authenticate \
    --disable-microhttpd \
    --localstatedir=%{_localstatedir} \
    --enable-elfutils \
    --with-ntp-servers='gateway. 0.clearlinux.pool.ntp.org 1.clearlinux.pool.ntp.org 2.clearlinux.pool.ntp.org 3.clearlinux.pool.ntp.org' \
    --with-efi-ldsdir=/usr/lib --with-efi-libdir=/usr/lib \
    --with-pamlibdir=%{_libdir}/security

# Disable unified cgroups, as a guess that that's why we are seeing pid 1 aborts
# This regresses bootspeed.
#    --enable-unified


make %{?_smp_mflags}

%check
make V=1 VERBOSE=1 %{?_smp_mflags} check || :

%install
%make_install

# need to provide %{_sbindir}/init
mkdir -p %{buildroot}%{_sbindir}
ln -s /usr/lib/systemd/systemd %{buildroot}%{_sbindir}/init

# compat symlinks
ln -s %{_bindir}/systemctl %{buildroot}%{_sbindir}/halt
ln -s %{_bindir}/systemctl %{buildroot}%{_sbindir}/poweroff
ln -s %{_bindir}/systemctl %{buildroot}%{_sbindir}/reboot
ln -s %{_bindir}/systemctl %{buildroot}%{_sbindir}/runlevel
ln -s %{_bindir}/systemctl %{buildroot}%{_sbindir}/shutdown

# All users should be defined in the systemd-config package
rm -f %{buildroot}/usr/lib/sysusers.d/basic.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd.conf
rm -f %{buildroot}/usr/lib/sysusers.d/systemd-remote.conf
rmdir %{buildroot}/usr/lib/sysusers.d

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

# remove bootchart man pages
rm -f %{buildroot}/usr/share/man/man1/systemd-bootchart.1
rm -f %{buildroot}/usr/share/man/man5/bootchart.conf.5
rm -f %{buildroot}/usr/share/man/man5/bootchart.conf.d.5

# Do not ship broken symlink
rm -f %{buildroot}/etc/xdg/systemd/user

# Move config file into system PAM location
mv %{buildroot}%{_sysconfdir}/pam.d %{buildroot}%{_datadir}/.

cp %{SOURCE1} %{buildroot}/usr/lib/udev/hwdb.d/
rm -f %{buildroot}/usr/lib/udev/hwdb.d/20-usb-vendor-model.hwdb

# Move dbus config
mkdir -p %{buildroot}%{_datadir}/dbus-1/system.d
mv %{buildroot}%{_sysconfdir}/dbus-1/system.d/* %{buildroot}%{_datadir}/dbus-1/system.d

# Pre-generate and pre-ship hwdb, to speed up first boot
./systemd-hwdb --root %{buildroot} --usr || ./udevadm hwdb --root %{buildroot} --update --usr

# Compute catalog
./journalctl --root %{buildroot} --update-catalog

# Add a hook to integrate telemetrics crashprobe with systemd-coredump
mkdir -p %{buildroot}/usr/lib/systemd/system-coredump
ln -s ../../../bin/crashprobe %{buildroot}/usr/lib/systemd/system-coredump/crashprobe

# only supported plugin is "clear.install"
rm -rvf %{buildroot}/usr/lib/kernel

%find_lang systemd

%files
%exclude /usr/lib/systemd/system/sysinit.target.wants/ldconfig.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-firstboot.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-sysusers.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-hwdb-update.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-update-done.service
%exclude /usr/lib/systemd/system/sysinit.target.wants/systemd-journal-catalog-update.service
%exclude /usr/lib/systemd/system/systemd-journal-catalog-update.service
%exclude /usr/lib/systemd/system/systemd-firstboot.service
%exclude /usr/lib/systemd/system/systemd-sysusers.service
%exclude /usr/lib/systemd/system/systemd-hwdb-update.service
%exclude /usr/lib/systemd/system/systemd-update-done.service
%exclude /usr/lib/systemd/systemd-update-done
%exclude /usr/lib/systemd/system/systemd-importd.service
%exclude /usr/lib/systemd/systemd-importd
%exclude /usr/lib/systemd/systemd-import
%exclude /usr/share/dbus-1/system-services/org.freedesktop.import1.service
%exclude /usr/share/dbus-1/system.d/org.freedesktop.import1.conf
%exclude /usr/lib/systemd/systemd-coredump
%exclude /usr/lib/systemd/systemd-bootchart
%exclude /usr/lib/systemd/system/systemd-bootchart.service

%{_datadir}/pam.d/systemd-user

%{_sbindir}/halt
%{_sbindir}/init
%{_sbindir}/poweroff
%{_sbindir}/reboot
%{_sbindir}/runlevel
%{_sbindir}/shutdown
%{_bindir}/busctl
%{_bindir}/hostnamectl
%{_bindir}/journalctl
%{_bindir}/kernel-install
%{_bindir}/localectl
%{_bindir}/loginctl
%{_bindir}/machinectl
%{_bindir}/networkctl
%{_bindir}/systemctl
%{_bindir}/systemd-analyze
%{_bindir}/systemd-ask-password
%{_bindir}/systemd-cat
%{_bindir}/systemd-cgls
%{_bindir}/systemd-cgtop
%{_bindir}/systemd-delta
%{_bindir}/systemd-detect-virt
%{_bindir}/systemd-escape
%{_bindir}/systemd-inhibit
%{_bindir}/systemd-machine-id-setup
%{_bindir}/systemd-notify
%{_bindir}/systemd-nspawn
%{_bindir}/systemd-path
%{_bindir}/systemd-resolve
%{_bindir}/systemd-run
%{_bindir}/systemd-stdio-bridge
%{_bindir}/systemd-tmpfiles
%{_bindir}/systemd-tty-ask-password-agent
%{_bindir}/timedatectl
%{_bindir}/udevadm

/usr/lib/sysctl.d/50-default.conf
/usr/lib/systemd/catalog/systemd.catalog
/usr/lib/systemd/network/80-container-host0.network
/usr/lib/systemd/network/80-container-ve.network
/usr/lib/systemd/network/99-default.link
/usr/lib/systemd/system-generators/systemd-dbus1-generator
/usr/lib/systemd/system-generators/systemd-debug-generator
/usr/lib/systemd/system-generators/systemd-fstab-generator
/usr/lib/systemd/system-generators/systemd-getty-generator
%exclude /usr/lib/systemd/system-generators/systemd-gpt-auto-generator
%exclude /usr/lib/systemd/system-generators/systemd-cryptsetup-generator
%exclude /usr/lib/systemd/system-generators/systemd-hibernate-resume-generator
/usr/lib/systemd/system-preset/90-systemd.preset
/usr/lib/systemd/system/-.slice
/usr/lib/systemd/system/autovt@.service
/usr/lib/systemd/system/basic.target
/usr/lib/systemd/system/bluetooth.target
/usr/lib/systemd/system/console-getty.service
/usr/lib/systemd/system/console-shell.service
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
%exclude /usr/lib/systemd/systemd-journal-upload
%exclude /usr/lib/systemd/systemd-pull
/usr/lib/systemd/user/*.service
/usr/lib/systemd/user/*.socket
/usr/lib/systemd/user/*.target
/usr/lib/systemd/user-generators/systemd-dbus1-generator

/usr/lib/tmpfiles.d/*.conf

/usr/lib/udev/ata_id
/usr/lib/udev/cdrom_id
/usr/lib/udev/collect
/usr/lib/udev/hwdb.bin
/usr/lib/udev/mtd_probe
/usr/lib/udev/rules.d/50-udev-default.rules
/usr/lib/udev/rules.d/60-drm.rules
/usr/lib/udev/rules.d/60-persistent-input.rules
/usr/lib/udev/rules.d/60-persistent-storage.rules
/usr/lib/udev/rules.d/64-btrfs.rules
/usr/lib/udev/rules.d/70-mouse.rules
/usr/lib/udev/rules.d/70-power-switch.rules
/usr/lib/udev/rules.d/70-uaccess.rules
/usr/lib/udev/rules.d/71-seat.rules
/usr/lib/udev/rules.d/73-seat-late.rules
/usr/lib/udev/rules.d/75-net-description.rules
/usr/lib/udev/rules.d/80-drivers.rules
/usr/lib/udev/rules.d/80-net-setup-link.rules
/usr/lib/udev/rules.d/90-vconsole.rules
/usr/lib/udev/rules.d/99-systemd.rules

/usr/lib/systemd/system/cryptsetup-pre.target
/usr/lib/systemd/system/cryptsetup.target
/usr/lib/udev/rules.d/60-block.rules
/usr/lib/udev/rules.d/60-evdev.rules
/usr/lib/udev/rules.d/60-serial.rules

/usr/lib/udev/scsi_id
/usr/lib/udev/v4l_id

%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/dbus-1/system-services/*
%{_datadir}/dbus-1/services/*

%{_datadir}/systemd/*

%exclude /var/lib/systemd/catalog/database

%files libs
%{_libdir}/libnss_myhostname.so.2
%{_libdir}/libnss_mymachines.so.2
%{_libdir}/libnss_resolve.so.2

%{_libdir}/libudev.*
%{_libdir}/libsystemd.so.*
%{_libdir}/security/pam_systemd.so

%files dev
%{_includedir}/*.h
%{_includedir}/systemd/*.h
%{_libdir}/*.so
/usr/lib/rpm/macros.d/macros.systemd
/usr/lib64/pkgconfig/*.pc

%files doc
%{_datadir}/doc/systemd/*
%{_mandir}/*/*

%files extras
/usr/share/zsh/site-functions/*
%{_datadir}/bash-completion/completions/*
/usr/share/polkit-1/actions/*
/usr/bin/systemd-firstboot
/usr/lib/systemd/systemd-journal-upload
/usr/lib/systemd/systemd-pull
%{_bindir}/systemd-sysusers
/usr/lib/systemd/system-generators/systemd-system-update-generator
/usr/lib/systemd/system/ldconfig.service
/usr/lib/systemd/system/sysinit.target.wants/ldconfig.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-firstboot.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-sysusers.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-hwdb-update.service
/usr/lib/systemd/system/sysinit.target.wants/systemd-update-done.service
/usr/lib/systemd/system/system-update.target
/usr/lib/systemd/system/systemd-firstboot.service
/usr/lib/systemd/system/systemd-sysusers.service
/usr/lib/systemd/system/systemd-hwdb-update.service
%{_bindir}/systemd-hwdb
/usr/lib/udev/hwdb.d/*.hwdb
/usr/lib/systemd/system/systemd-update-done.service
/usr/lib/systemd/systemd-update-done
/usr/lib/udev/rules.d/60-cdrom_id.rules
/usr/lib/udev/rules.d/60-persistent-alsa.rules
/usr/lib/udev/rules.d/60-persistent-storage-tape.rules
/usr/lib/udev/rules.d/60-persistent-v4l.rules
/usr/lib/udev/rules.d/75-probe_mtd.rules
/usr/lib/udev/rules.d/78-sound-card.rules
/usr/lib/systemd/system/dbus-org.freedesktop.import1.service
/usr/lib/systemd/system/org.freedesktop.import1.busname
/usr/lib/systemd/system/busnames.target.wants/org.freedesktop.import1.busname
/usr/lib/systemd/system/local-fs.target.wants/var-lib-machines.mount
/usr/lib/systemd/system/var-lib-machines.mount
/usr/lib/systemd/system/systemd-importd.service
/usr/lib/systemd/systemd-importd
/usr/lib/systemd/systemd-import
/usr/share/dbus-1/system-services/org.freedesktop.import1.service
/usr/share/dbus-1/system.d/org.freedesktop.import1.conf
/usr/lib/systemd/import-pubring.gpg


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
%{_bindir}/bootctl
%{_bindir}/kernel-efi-stub
/usr/lib/systemd/boot/efi/

%files coredump
/usr/bin/coredumpctl
/usr/lib/sysctl.d/50-coredump.conf
/usr/lib/systemd/systemd-coredump
/usr/lib/systemd/system-coredump/crashprobe
