%define oname I-Nex

Summary:	System information tool
Name:		i-nex
Version:	7.6.1
Release:	5
Group:		System/Configuration/Hardware
License:	LGPLv3+
Url:		https://launchpad.net/i-nex
Source0:	https://github.com/%{name}/I-Nex/archive/%{version}/%{oname}-%{version}.tar.gz
Patch1:		i-nex-makefile-p0.patch
# Arch
Patch2:		Fix-error-if-proc-mtrr-doesn-t-exist.patch
Patch3:		Fix-libcpuid-SOVERSION.patch
Patch4:		Adapt-for-new-libcpuid-structure.patch
# Just to make sure we have all these in repositories
BuildRequires:	gambas3-devel
BuildRequires:	gambas3-gb-desktop
BuildRequires:	gambas3-gb-form-dialog
BuildRequires:	gambas3-gb-form
BuildRequires:	gambas3-gb-gui
BuildRequires:	gambas3-gb-gtk3
BuildRequires:	gambas3-gb-image
BuildRequires:	gambas3-gb-qt5
BuildRequires:	gambas3-gb-settings
BuildRequires:  gambas3-gb-jit
BuildRequires:	imagemagick
BuildRequires:  pastebinit
BuildRequires:	pkgconfig(libcpuid) >= 0.5.0
Requires:	gambas3-gb-desktop
Requires:	gambas3-gb-form-dialog
Requires:	gambas3-gb-form
Requires:	gambas3-gb-gui
Requires:	gambas3-gb-gtk3
Requires:	gambas3-gb-image
Requires:	gambas3-gb-qt5
Requires:	gambas3-gb-settings
Requires:	gambas3-runtime
Requires:	gambas3-gb-jit
Requires:	libcpuid-tools >= 0.5.0

%description
An application that gathers information for hardware components available
on your system and displays it using an user interface similar to the popular
Windows tool CPU-Z.

%prep
%setup -q -n %{oname}-%{version}
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

# fix png rgb 
pushd %{oname}/%{name}/logo
find . -type f -name "*.png" -exec convert {} -strip {} \;
popd

%build
pushd %{oname}
autoreconf -fi
%configure
popd
%make_build \
	STATIC=false \
	CFLAGS="%{optflags}"

%install
%make_install

# install menu entries
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

cat > %{buildroot}%{_datadir}/applications/%{name}-library.desktop << EOF
[Desktop Entry]
Version=1.0
Name=I-Nex Library
Comment=I-Nex System Library Information
Exec=%{name} --library
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Utility;
EOF

# install menu icons
#for N in 16 32 48 64 128;
#do
#convert %{oname}/%{name}/logo/i-nex.0.4.x.png -resize ${N}x${N} $N.png;
#install -D -m 0644 16.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
#done

# not needed
rm -rf %{buildroot}%{_defaultdocdir}/%{name}



%files
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
#{_datadir}/%{name}
#{_iconsdir}/hicolor/*/apps/%{name}.png
%{_udevrulesdir}/i2c_smbus.rules
%{_datadir}/applications/i-nex-library.desktop
%{_mandir}/man1/i-nex.1.*
%{_mandir}/man1/i-nex.gambas.1.*
%{_mandir}/man1/i-nex-edid.1.*
%{_datadir}/pixmaps/i-nex-16.png
%{_datadir}/pixmaps/i-nex-32.png
%{_datadir}/pixmaps/i-nex-128.png
%{_datadir}/pixmaps/i-nex.png
