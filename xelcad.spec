Summary:	xelcad - electricat circuit layouts.
Summary(pl):	xelcad - projektowanie obwodów elektrycznych.
Name:		xelcad
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications/Engeeniering/CAD
######		Unknown group!
Group(pl):	X11/Aplikacje/CAD
Source0:	http://www.neuss.netsurf.de/~skrodzki/xelcad/%{name}-src.tgz
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-config-fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XelCAD is a X-based application, designed to create electrical circuit
layouts. As author say: "It's, of course, not a profesional CAD
application, but it's absolutely sufficient for private-homr usage"

%description -l pl

%prep
%setup -q -c

%patch -p0
%patch1 -p0

%build
cd put_me_anywhere
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xelcad/{examples,elements}}

install put_me_anywhere/xelcad $RPM_BUILD_ROOT%{_bindir}

install examples/* $RPM_BUILD_ROOT%{_datadir}/xelcad/examples

cp -Rpd .xelcad/* $RPM_BUILD_ROOT%{_datadir}/xelcad
cp -Rpd .xelcad/.x* $RPM_BUILD_ROOT%{_datadir}/xelcad

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/xelcad
%{_datadir}/xelcad
