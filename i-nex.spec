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
BuildRequires:	gambas3-gb-gtk3
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
pushd %{oname}
autoreconf -fi
%configure2_5x
popd
%make \
	STATIC=false \
	CFLAGS="%{optflags}"

%install
%makeinstall_std

%files
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png

