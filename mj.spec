%define	name	mj
%define	version	1.6.3
%define	release	1mdk

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	mj is the Chinese game of mah-jong
Url:		http://www.stevens-bradfield.com/MahJong/
Source0:	%{name}-%{version}-src.tar.bz2
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

%build
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std install.man BINDIR="%{_bindir}" MANDIR="%{_mandir}/man1"
#make install DESTDIR="$RPM_BUILD_ROOT" BINDIR="%_bindir"
#make install.man MANDIR="%_mandir/man1" DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc  ChangeLog [A-Z][A-Z]*
%{_bindir}/*
%{_mandir}/man?/*

