%define oname I-Nex

Summary:	System information tool
Name:		i-nex
Version:	7.6.0
Release:	1
Group:		System/Configuration/Hardware
License:	LGPLv3+
Url:		https://launchpad.net/i-nex
Source0:	https://github.com/%{name}/I-Nex/archive/%{version}/%{oname}-%{version}.tar.gz
# Just to make sure we have all these in repositories
BuildRequires:	gambas3-devel
BuildRequires:	gambas3-gb-desktop
BuildRequires:	gambas3-gb-form-dialog
BuildRequires:	gambas3-gb-form
BuildRequires:	gambas3-gb-gui
BuildRequires:	gambas3-gb-gtk
BuildRequires:	gambas3-gb-image
BuildRequires:	gambas3-gb-qt5
BuildRequires:	gambas3-gb-settings
BuildRequires:	imagemagick
BuildRequires:  pastebinit
BuildRequires:	pkgconfig(libcpuid)
Requires:	gambas3-gb-desktop
Requires:	gambas3-gb-form-dialog
Requires:	gambas3-gb-form
Requires:	gambas3-gb-gui
Requires:	gambas3-gb-gtk
Requires:	gambas3-gb-image
Requires:	gambas3-gb-qt4
Requires:	gambas3-gb-settings
Requires:	gambas3-runtime
BuildArch:	noarch

%description
An application that gathers information for hardware components available
on your system and displays it using an user interface similar to the popular
Windows tool CPU-Z.

%prep
%setup -q -n %{oname}-%{version}

%build
cd src/%{name}
gbc3 -eagtpmv
gba3

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 src/i-nex/i-nex.gambas %{buildroot}%{_bindir}

# Launcher script
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
env LIBOVERLAY_SCROLLBAR=0 %{_bindir}/i-nex.gambas
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

# install menu entry
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Version=1.0
Name=I-Nex
Comment=I-Nex, a system information tool
Exec=i-nex
Icon=i-nex
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Utility;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert src/i-nex/logo/i-nex.0.4.x.png -resize ${N}x${N} $N.png;
install -D -m 0644 16.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

# pastebinit
mkdir -p %{buildroot}%{_datadir}/%{name}/pastebinit
cp -rf pastebin.d utils pastebinit{,.xml} release.conf test.sh %{buildroot}%{_datadir}/%{name}/pastebinit
chmod 0755 %{buildroot}%{_datadir}/%{name}/pastebinit/test.sh
chmod 0755 %{buildroot}%{_datadir}/%{name}/pastebinit/utils/pbput

%files
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png

