%define major		1
%define libname		%mklibname microdns %{major}
%define develname	%mklibname microdns -d

Name:		libmicrodns
Version:	0.2.0
Release:	%mkrel 2
Summary:	Minimal mDNS resolver library
Group:		System/Libraries
License:	LGPLv2+
URL:		https://github.com/videolabs/libmicrodns
Source0:	https://github.com/videolabs/libmicrodns/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	meson
BuildRequires:	gcc

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
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	microdns-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}.

#------------------------------------------------

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n %{libname}
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libmicrodns.so.%{major}{,.*}

%files -n %{develname}
%{_includedir}/microdns/
%{_libdir}/libmicrodns.so
%{_libdir}/pkgconfig/microdns.pc
