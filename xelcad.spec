Summary:	xelcad - electricat circuit layouts.
Summary(pl):	xelcad - projektowanie obwodów elektrycznych.
Name:		xelcad
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications/Engeeniering/CAD
Group(pl):	X11/Aplikacje/CAD
Source0:	http://www.neuss.netsurf.de/~skrodzki/xelcad/%{name}-src.tgz
Patch0:		xelcad-Makefile.patch
Patch1:		xelcad-config-fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6
%define _docdir	/usr/share/doc

%description
XelCAD is a X-based application, designed to create electrical circuit layouts.
As author say:
"It's, of course, not a profesional CAD application, but it's absolutely 
sufficient for private-homr usage"

%description -l pl

%prep
install -d $RPM_BUILD_DIR/%{name}-%{version}
cd $RPM_BUILD_DIR/%{name}-%{version}
tar xfz %SOURCE0

%patch -p0
%patch1 -p0

%build
cd %{name}-%{version}/put_me_anywhere
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
cd %name-%version
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xelcad/{examples,elements}}

install -s put_me_anywhere/xelcad $RPM_BUILD_ROOT%{_bindir}

install examples/* $RPM_BUILD_ROOT%{_datadir}/xelcad/examples

cp -Rpd .xelcad/* $RPM_BUILD_ROOT%{_datadir}/xelcad
cp -Rpd .xelcad/.x* $RPM_BUILD_ROOT%{_datadir}/xelcad

gzip -9nf README
install README.gz $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(644,root,root) %{_docdir}/%{name}-%{version}/README.gz
%attr(755,root,root) %{_bindir}/xelcad
%{_datadir}/xelcad
