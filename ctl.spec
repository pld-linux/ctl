Summary:	Color Transform Language libraries
Summary(pl.UTF-8):	Biblioteki CTL (języka przekształceń kolorów)
Name:		ctl
Version:	1.4.1
Release:	2
License:	BSD + IP clause
Group:		Libraries
Source0:	http://downloads.sourceforge.net/ampasctl/%{name}-%{version}.tar.gz
# Source0-md5:	11e215aea6c6380833ade3b576660638
Patch0:		%{name}-include.patch
URL:		http://www.oscars.org/science-technology/council/projects/ctl.html
BuildRequires:	ilmbase-devel >= 1.0.1
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CTL (Color Transform Language) interpreter contains the following C++
libraries:

IlmCtl - CTL interpreter frontend and the interpreter's public
programming interface.

IlmCtlSimd - interpreter's SIMD backend.

IlmCtlMath - math routines used by IlmCtlSimd: conversions between
standard color spaces, 1D and 3D lookup tables, 3D scattered data
interpolation.

%description -l pl.UTF-8
Interpreter CTL (Color Transform Language - języka przekształceń
kolorów) składa się z następujących bibliotek C++:

IlmCtl - frontend interpretera CTL i jego publiczny interfejs
programistyczny.

IlmCtlSimd - backend SIMD interpretera.

IlmCtlMath - funkcje matematyczne wykorzystywane przez IlmCtlSimd:
przekształcenia między standardowymi przestrzeniami kolorów, tablice
wyszukiwań 1D i 3D, interpolacja zgromadzonych danych 3D.

%package devel
Summary:	Header files for CTL library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CTL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ilmbase-devel >= 1.0.1
Requires:	libstdc++-devel

%description devel
Header files for CTL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CTL.

%package static
Summary:	Static CTL library
Summary(pl.UTF-8):	Statyczna biblioteka CTL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CTL library.

%description static -l pl.UTF-8
Statyczna biblioteka CTL.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libIlmCtl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmCtl.so.2
%attr(755,root,root) %{_libdir}/libIlmCtlMath.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmCtlMath.so.2
%attr(755,root,root) %{_libdir}/libIlmCtlSimd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libIlmCtlSimd.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/CtlManual.pdf
%attr(755,root,root) %{_libdir}/libIlmCtl.so
%attr(755,root,root) %{_libdir}/libIlmCtlMath.so
%attr(755,root,root) %{_libdir}/libIlmCtlSimd.so
%{_libdir}/libIlmCtl.la
%{_libdir}/libIlmCtlMath.la
%{_libdir}/libIlmCtlSimd.la
%{_includedir}/CTL
%{_pkgconfigdir}/CTL.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libIlmCtl.a
%{_libdir}/libIlmCtlMath.a
%{_libdir}/libIlmCtlSimd.a
