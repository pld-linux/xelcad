#
# TODO:
# - prepare desktop file and png icon.
#
Summary:	xelcad - electricat circuit layouts
Summary(pl):	xelcad - projektowanie obwodów elektrycznych
Name:		xelcad
Version:	0.3
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://www.neuss.netsurf.de/~skrodzki/xelcad/%{name}-src.tgz
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-config-fix.patch
# URL from sources, but seems to be dead
URL:		http://www.neuss.netsurf.de/~skrodzki/
BuildRequires:	xforms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XelCAD is a X-based application, designed to create electrical circuit
layouts. As author say: "It's, of course, not a profesional CAD
application, but it's absolutely sufficient for private-home usage"

%description -l pl
XelCAD to aplikacja pod X s³u¿±ca do projektowania obwodów
elektrycznych. Wed³ug autora, nie jest to profesjonalna aplikacja CAD,
ale ca³kowicie wystarcza do domowego u¿ytku.

%prep
%setup -q -c

%patch0 -p0
%patch1 -p0

%build
cd put_me_anywhere
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir}/xelcad/{examples,elements}}

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
