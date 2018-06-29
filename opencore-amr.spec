Name:           opencore-amr
Version:        0.1.5
Release:        1%{?dist}
Summary:        OpenCORE Adaptive Multi Rate Narrowband and Wideband speech lib
License:        ASL 2.0
URL:            http://sourceforge.net/projects/opencore-amr/

Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         opencore-amr-0.1.3-fix_pc.patch

%description
Library of OpenCORE Framework implementation of Adaptive Multi Rate Narrowband
and Wideband speech codec.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1
mv opencore/README opencore/README.opencore

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%ldconfig_scriptlets

%files
%license LICENSE
%doc README opencore/ChangeLog opencore/NOTICE opencore/README.opencore
%{_libdir}/libopencore-amrnb.so.*
%{_libdir}/libopencore-amrwb.so.*

%files devel
%{_includedir}/opencore-amrnb
%{_includedir}/opencore-amrwb
%{_libdir}/libopencore-amrnb.so
%{_libdir}/libopencore-amrwb.so
%{_libdir}/pkgconfig/opencore-amrnb.pc
%{_libdir}/pkgconfig/opencore-amrwb.pc

%changelog
* Fri Jun 29 2018 Simone Caronni <negativo17@gmail.com> - 0.1.5-1
- Update to 0.1.5.
- Clean up SPEC file.

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.3-3
- Mass rebuilt for Fedora 19 Features

* Fri May 18 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.1.3-2
- Fix pkgconfig include

* Sun May 13 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.1.3-1
- Update to 0.1.3

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.1.2-3
- Rebuilt for c++ ABI breakage

* Wed Jan 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  4 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.2-1
- New upstream release 0.1.2

* Thu Jul 30 2009 Hans de Goede <j.w.r.degoede@hhs.nl> 0.1.1-1
- First version of the RPM Fusion package
