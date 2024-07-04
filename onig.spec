#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v13
# autospec commit: 2659038
#
Name     : onig
Version  : 6.9.9
Release  : 29
URL      : https://github.com/kkos/oniguruma/releases/download/v6.9.9/onig-6.9.9.tar.gz
Source0  : https://github.com/kkos/oniguruma/releases/download/v6.9.9/onig-6.9.9.tar.gz
Summary  : Regular expression library
Group    : Development/Tools
License  : BSD-3-Clause
Requires: onig-bin = %{version}-%{release}
Requires: onig-lib = %{version}-%{release}
Requires: onig-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Oniguruma  ----   (C) K.Kosako
https://github.com/kkos/oniguruma
FIXED Security Issues (in Oniguruma 6.3.0):
CVE-2017-9224, CVE-2017-9225, CVE-2017-9226
CVE-2017-9227, CVE-2017-9228, CVE-2017-9229

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
%setup -q -n onig-6.9.9
cd %{_builddir}/onig-6.9.9
pushd ..
cp -a onig-6.9.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720123671
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-binary-compatible-posix-api=yes
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --enable-binary-compatible-posix-api=yes
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720123671
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/onig
cp %{_builddir}/onig-%{version}/COPYING %{buildroot}/usr/share/package-licenses/onig/061a5f18d5b7a5fe6a1da9419bef05b7d35f7cf6 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/onig-config

%files dev
%defattr(-,root,root,-)
/usr/include/oniggnu.h
/usr/include/onigposix.h
/usr/include/oniguruma.h
/usr/lib64/libonig.so
/usr/lib64/pkgconfig/oniguruma.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libonig.so.5.4.0
/usr/lib64/libonig.so.5
/usr/lib64/libonig.so.5.4.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/onig/061a5f18d5b7a5fe6a1da9419bef05b7d35f7cf6
