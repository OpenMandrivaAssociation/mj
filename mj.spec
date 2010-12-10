%define	name	mj
%define	version	1.6.3
%define	release	%mkrel 6

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Chinese game of mah-jong
Url:		http://www.stevens-bradfield.com/MahJong/
Source0:	%{name}-%{version}-src.tar.bz2
Patch0:		mj-1.6.3-fix-str-fmt.patch
Group:		Games/Boards
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gtk+-devel

%description
mj is the Chinese game of mah-jong. mj supports network play, as well as 
simple human to computer play. A Windows (tm) version of this game is
also available.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p0

%build
make CDEBUGFLAGS="%{optflags}" CCLINK="gcc %{?ldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std install.man BINDIR="%{_bindir}" MANDIR="%{_mandir}/man1"

mkdir -p %buildroot%_datadir/applications
cat << EOF > %buildroot%_datadir/applications/mandriva-%name.desktop
[Desktop Entry]
Name=Mahjong
Comment=Chinese game of mah-jong
Exec=%_bindir/xmj
Icon=boards_section
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc  ChangeLog [A-Z][A-Z]*
%{_bindir}/*
%{_mandir}/man?/*
%{_datadir}/applications/*.desktop
