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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.3-6mdv2011.0
+ Revision: 620368
- the mass rebuild of 2010.0 packages

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.6.3-5mdv2010.0
+ Revision: 439991
- rebuild

* Mon Apr 06 2009 Funda Wang <fwang@mandriva.org> 1.6.3-4mdv2009.1
+ Revision: 364334
- fix str fmt
- add menu item

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.6.3-3mdv2009.0
+ Revision: 252556
- rebuild
- fix summary-not-capitalized

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.6.3-1mdv2008.1
+ Revision: 130011
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import mj


* Thu Jan 13 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.6.3-1mdk
- 1.6.3

* Sat Dec 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.6-1mdk
- 1.6
- cosmetics
- don't rm -rf $RPM_BUILD_ROOT in %%prep
- use %%makeinstall_std macro
- add buildrequires

* Wed Aug 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.5.6-1mdk
- 1.5.6

* Mon May 12 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.5.5-1mdk
- 1.5.5

* Fri Apr 04 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.5.2-1mdk
- 1.5.2

* Mon Mar  3 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.2-5mdk
- fix W: mj non-standard-group Amusements/Games

* Sun Feb 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-4mdk
- rebuild

* Tue Aug 21 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-3mdk
- rebuild

* Mon Feb 12 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0.2-2mdk
- Fix defattr.

* Mon Feb 12 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.0.2-1mdk
- First RPM for Mandrake.

