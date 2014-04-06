Summary:	Color Transform Language libraries
Summary(pl.UTF-8):	Biblioteki CTL (języka przekształceń kolorów)
Name:		ctl
Version:	1.5
Release:	1
License:	BSD + IP clause
Group:		Libraries
Source0:	https://github.com/ampas/CTL/archive/%{name}-%{version}.tar.gz
# Source0-md5:	020aa09422c13b2f62c1c40f18d9d093
Patch0:		%{name}-libdir.patch
Patch1:		%{name}-ctlrender.patch
Patch2:		%{name}-pc.patch
URL:		http://www.oscars.org/science-technology/council/projects/ctl.html
BuildRequires:	OpenEXR-devel
BuildRequires:	aces_container-devel
BuildRequires:	cmake >= 2.8
BuildRequires:	ilmbase-devel >= 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
Requires:	ilmbase >= 2.0.0
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
Requires:	ilmbase-devel >= 2.0.0
Requires:	libstdc++-devel
Obsoletes:	ctl-static

%description devel
Header files for CTL library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CTL.

%package -n openexr_ctl
Summary:	OpenEXR interface to CTL (Color Transform Language)
Summary(pl.UTF-8):	Interfejs OpenEXR do CTL (języka przekształceń kolorów)
Group:		Libraries
Requires:	ctl = %{version}-%{release}

%description -n openexr_ctl
IlmImfCtl provides a simplified OpenEXR interface to CTL (Color
Transform Language).

%description -n openexr_ctl -l pl.UTF-8
IlmImfCtl udostępnia uproszczony interfejs OpenEXR do CTL (języka
przekształceń kolorów).

%package -n openexr_ctl-devel
Summary:	Header files for IlmInfCtl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki IlmInfCtl
Group:		Development/Libraries
Requires:	OpenEXR-devel
Requires:	ctl-devel = %{version}-%{release}
Requires:	openexr_ctl = %{version}-%{release}
Obsoletes:	openexr_ctl-static

%description -n openexr_ctl-devel
Header files for IlmInfCtl library.

%description -n openexr_ctl-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki IlmInfCtl.

%package -n openexr_ctl-progs
Summary:	Programs utilizing OpenEXR/CTL interface
Summary(pl.UTF-8):	Programy wykorzystujące interfejs OpenEXR/CTL
Group:		Applications/Graphics
Requires:	openexr_ctl = %{version}-%{release}

%description -n openexr_ctl-progs
Programs utilizing OpenEXR/CTL interface:

exrdpx is an initial version of a CTL-driven file converter that
translates DPX files into OpenEXR files and vice versa. The conversion
between the DPX and OpenEXR color spaces is handled by CTL transforms.

exr_ctl_exr is an initial version of a program that can bake the
effect of a series of CTL transforms into the pixels of an OpenEXR
file.

%description -n openexr_ctl-progs -l pl.UTF-8
Programy wykorzystujące interfejs OpenEXR/CTL:

exrdpx to wstępna wersja konwertera plików sterowanego CTL-em,
tłumaczącego pliki DPX na OpenEXR i na odwrót. Przekształcenia między
przestrzeniami kolorów DPX i OpenEXR są obsługiwane przez
przekształcenia CTL.

exr_ctl_exr to wstępna wersja programu potrafiącego zamienić efekt
serii przekształceń CTL na piksele w pliku OpenEXR.

%package -n ctlrender
Summary:	CLI application to apply CTL transforms to an image
Summary(pl.UTF-8):	Uruchamiany z linii poleceń program do nakładania przekształceń CTL na obraz
Group:		Applications/Graphics
Requires:	ctl = %{version}-%{release}

%description -n ctlrender
ctlrender is a command line application for applying CTL transforms to
an image using one or more CTL scripts, potentially converting the
file format in the process.

ctlrender supports OpenEXR, TIFF, DPX, and ACES container file
formats.

%description -n ctlrender
ctlrender to uruchamiany z linii poleceń program do nakładania
przekształceń CTL na obraz przy użyciu jednego lub więcej skryptów
CTL, potencjalnie także zmieniając w trakcie format pliku.

ctlrender obsługuje formaty plików OpenEXR, TIFF, DPX oraz ACES.

%prep
%setup -q -n CTL-%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake . \
	-DINSTALL_CMAKE_DIR=%{_libdir}/cmake/CTL \
	-DINSTALL_LIB_DIR=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/CTL

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG LICENSE README.md
%attr(755,root,root) %{_libdir}/libIlmCtl.so.*.*.*
%attr(755,root,root) %{_libdir}/libIlmCtlMath.so.*.*.*
%attr(755,root,root) %{_libdir}/libIlmCtlSimd.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/CtlManual.pdf
%attr(755,root,root) %{_libdir}/libIlmCtl.so
%attr(755,root,root) %{_libdir}/libIlmCtlMath.so
%attr(755,root,root) %{_libdir}/libIlmCtlSimd.so
%{_includedir}/CTL
%{_pkgconfigdir}/CTL.pc
%{_libdir}/cmake/CTL

%files -n openexr_ctl
%defattr(644,root,root,755)
%doc OpenEXR_CTL/README
%attr(755,root,root) %{_libdir}/libIlmImfCtl.so

%files -n openexr_ctl-devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/libIlmImfCtl.so
%{_includedir}/OpenEXR/ImfCtlApplyTransforms.h
%{_pkgconfigdir}/OpenEXR_CTL.pc

%files -n openexr_ctl-progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/exr_ctl_exr
%attr(755,root,root) %{_bindir}/exrdpx
%{_prefix}/lib/CTL

%files -n ctlrender
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ctlrender
