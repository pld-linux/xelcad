Summary:	xelcad - electricat circuit layouts.
Summary(pl):	xelcad - projektowanie obwodów elektrycznych.
Name:		xelcad
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications/Engeeniering/CAD
Group(pl):	X11/Aplikacje/CAD
Source0:	http://www.neuss.netsurf.de/~skrodzki/xelcad/%{name}-src.tgz
Source1:	xelcad-start 
Patch0:		xelcad-Makefile.patch
Patch1:		xelcad-config-fix.patch
Buildroot:	/tmp/%{name}-%{version}-root-%(id -u -n)


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

%patch -p1
%patch1 -p1

%build
cd %{name}-%{version}/put_me_anywhere
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
cd %name-%version
install -d $RPM_BUILD_ROOT%{_prefix}/doc/%{name}-%{version}
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/{bin,share/xelcad/{examples,xelcad}}

install -s put_me_anywhere/xelcad $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

install %SOURCE1 $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

install examples/* $RPM_BUILD_ROOT%{_prefix}/X11R6/share/xelcad/examples

cp -Rpd .xelcad/* $RPM_BUILD_ROOT%{_prefix}/X11R6/share/xelcad/xelcad
cp -Rpd .xelcad/.x* $RPM_BUILD_ROOT%{_prefix}/X11R6/share/xelcad/xelcad

gzip -9nf README
install README.gz $RPM_BUILD_ROOT%{_prefix}/doc/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(644,root,root) %{_prefix}/doc/%{name}-%{version}/README.gz
%attr(755,root,root) %{_prefix}/X11R6/bin/xelcad
%attr(755,root,root) %{_prefix}/X11R6/bin/xelcad-start
%{_prefix}/X11R6/share/xelcad
