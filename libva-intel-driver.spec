#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libva-intel-driver
Version  : 2.2.0
Release  : 32
URL      : https://github.com/intel/intel-vaapi-driver/releases/download/2.2.0/intel-vaapi-driver-2.2.0.tar.bz2
Source0  : https://github.com/intel/intel-vaapi-driver/releases/download/2.2.0/intel-vaapi-driver-2.2.0.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: libva-intel-driver-lib = %{version}-%{release}
Requires: libva-intel-driver-license = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(intel-gen4asm)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_intel)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-wayland)
BuildRequires : pkgconfig(libva-x11)
BuildRequires : pkgconfig(x11)
Patch1: 0001-Check-for-python3-rather-than-python2.patch

%description
intel-vaapi-driver
VA driver for Intel G45 & HD Graphics family
License
-------
Please read the COPYING file available in this package.

%package lib
Summary: lib components for the libva-intel-driver package.
Group: Libraries
Requires: libva-intel-driver-license = %{version}-%{release}

%description lib
lib components for the libva-intel-driver package.


%package license
Summary: license components for the libva-intel-driver package.
Group: Default

%description license
license components for the libva-intel-driver package.


%prep
%setup -q -n intel-vaapi-driver-2.2.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570653599
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%reconfigure --disable-static --enable-hybrid-codec
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1570653599
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libva-intel-driver
cp COPYING %{buildroot}/usr/share/package-licenses/libva-intel-driver/COPYING
cp test/gtest/LICENSE %{buildroot}/usr/share/package-licenses/libva-intel-driver/test_gtest_LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/dri/i965_drv_video.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libva-intel-driver/COPYING
/usr/share/package-licenses/libva-intel-driver/test_gtest_LICENSE
