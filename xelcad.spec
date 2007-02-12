#
# TODO:
# - prepare desktop file and png icon.
#
Summary:	xelcad - electricat circuit layouts
Summary(pl.UTF-8):   xelcad - projektowanie obwodów elektrycznych
Name:		xelcad
Version:	0.3
Release:	5
License:	GPL
Group:		X11/Applications/Science
#Source0:	http://www.neuss.netsurf.de/~skrodzki/xelcad/%{name}-src.tgz
Source0:	%{name}-src.tgz
# Source0-md5:	b6b41464bc0035c92006da8e61cd2acf
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-config-fix.patch
Patch2:		%{name}-math.patch
#URL:		http://www.neuss.netsurf.de/~skrodzki/
BuildRequires:	xforms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XelCAD is a X-based application, designed to create electrical circuit
layouts. As author say: "It's, of course, not a profesional CAD
application, but it's absolutely sufficient for private-home usage"

%description -l pl.UTF-8
XelCAD to aplikacja pod X służąca do projektowania obwodów
elektrycznych. Według autora, nie jest to profesjonalna aplikacja CAD,
ale całkowicie wystarcza do domowego użytku.

%prep
%setup -q -c
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
%{__make} -C put_me_anywhere \
	RPM_OPT_FLAGS="%{rpmcflags}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xelcad/{examples,elements}}

install put_me_anywhere/xelcad $RPM_BUILD_ROOT%{_bindir}

install examples/*	$RPM_BUILD_ROOT%{_datadir}/xelcad/examples
cp -Rpd .xelcad/*	$RPM_BUILD_ROOT%{_datadir}/xelcad
cp -Rpd .xelcad/.x*	$RPM_BUILD_ROOT%{_datadir}/xelcad

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/xelcad
%{_datadir}/xelcad
