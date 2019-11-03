#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : onig
Version  : 6.9.3
Release  : 25
URL      : https://github.com/kkos/oniguruma/releases/download/v6.9.3/onig-6.9.3.tar.gz
Source0  : https://github.com/kkos/oniguruma/releases/download/v6.9.3/onig-6.9.3.tar.gz
Summary  : Regular expression library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: onig-bin = %{version}-%{release}
Requires: onig-lib = %{version}-%{release}
Requires: onig-license = %{version}-%{release}

%description
[![Build Status](https://travis-ci.org/kkos/oniguruma.svg?branch=master)](https://travis-ci.org/kkos/oniguruma)
[![Code Quality: Cpp](https://img.shields.io/lgtm/grade/cpp/g/kkos/oniguruma.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kkos/oniguruma/context:cpp)
[![Total Alerts](https://img.shields.io/lgtm/alerts/g/kkos/oniguruma.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/kkos/oniguruma/alerts)

%package bin
Summary: bin components for the onig package.
Group: Binaries
Requires: onig-license = %{version}-%{release}

%description bin
bin components for the onig package.


%package dev
Summary: dev components for the onig package.
Group: Development
Requires: onig-lib = %{version}-%{release}
Requires: onig-bin = %{version}-%{release}
Provides: onig-devel = %{version}-%{release}
Requires: onig = %{version}-%{release}
Requires: onig = %{version}-%{release}

%description dev
dev components for the onig package.


%package lib
Summary: lib components for the onig package.
Group: Libraries
Requires: onig-license = %{version}-%{release}

%description lib
lib components for the onig package.


%package license
Summary: license components for the onig package.
Group: Default

%description license
license components for the onig package.


%prep
%setup -q -n onig-6.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565194505
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1565194505
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/onig
cp COPYING %{buildroot}/usr/share/package-licenses/onig/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/onig-config

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libonig.so
/usr/lib64/pkgconfig/oniguruma.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libonig.so.5
/usr/lib64/libonig.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/onig/COPYING
