Summary:	Chinese game of mah-jong
Name:		mj
Version:	1.16
Release:	1
License:	GPLv2+
Group:		Games/Boards
Url:		http://www.stevens-bradfield.com/MahJong/
Source0:	http://mahjong.julianbradfield.org/Source/%{name}-%{version}-src.tar.gz
BuildRequires:	pkgconfig(gtk+-2.0)

%description
mj is the Chinese game of mah-jong. mj supports network play, as well as 
simple human to computer play. A Windows (tm) version of this game is
also available.

%files
%doc ChangeLog README CHANGES LICENCE
%{_bindir}/xmj
%{_bindir}/mj-*
%{_mandir}/man1/*.1*
%{_datadir}/applications/*.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-src

%build
make CDEBUGFLAGS="%{optflags}" CCLINK="gcc %{?ldflags}"

%install
%makeinstall_std \
	install.man \
	BINDIR="%{_bindir}" \
	MANDIR="%{_mandir}/man1" \
	INSTPGMFLAGS=""

mkdir -p %{buildroot}%{_datadir}/applications
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Mahjong
Comment=Chinese game of mah-jong
Exec=%{_bindir}/xmj
Icon=boards_section
Terminal=false
Type=Application
Categories=Game;BoardGame;
EOF

