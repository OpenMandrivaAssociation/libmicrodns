%define major		1
%define libname		%mklibname microdns
%define develname	%mklibname microdns -d

Name:		libmicrodns
Version:	0.2.0
Release:	1
Summary:	Minimal mDNS resolver library
Group:		System/Libraries
License:	LGPLv2+
URL:		https://github.com/videolabs/libmicrodns
Source0:	https://github.com/videolabs/libmicrodns/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	meson

%description
Minimal mDNS resolver (and announcer) library.

#------------------------------------------------

%package -n	%{libname}
Summary:	Minimal mDNS resolver library
Group:		System/Libraries

%description -n	%{libname}
Minimal mDNS resolver (and announcer) library.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	microdns-devel = %{EVRD}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files -n %{libname}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libmicrodns.so.%{major}{,.*}

%files -n %{develname}
%{_includedir}/microdns/
%{_libdir}/libmicrodns.so
%{_libdir}/pkgconfig/microdns.pc
