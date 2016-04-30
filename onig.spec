#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : onig
Version  : 5.9.6
Release  : 7
URL      : http://www.geocities.jp/kosako3/oniguruma/archive/onig-5.9.6.tar.gz
Source0  : http://www.geocities.jp/kosako3/oniguruma/archive/onig-5.9.6.tar.gz
Summary  : Regular expression library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: onig-bin
Requires: onig-lib

%description
Oniguruma  ----   (C) K.Kosako <sndgk393 AT ybb DOT ne DOT jp>
http://www.geocities.jp/kosako3/oniguruma/

%package bin
Summary: bin components for the onig package.
Group: Binaries

%description bin
bin components for the onig package.


%package dev
Summary: dev components for the onig package.
Group: Development
Requires: onig-lib
Requires: onig-bin

%description dev
dev components for the onig package.


%package lib
Summary: lib components for the onig package.
Group: Libraries

%description lib
lib components for the onig package.


%prep
%setup -q -n onig-5.9.6

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/onig-config

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
