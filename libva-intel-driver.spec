#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libva-intel-driver
Version  : 1.7.2
Release  : 8
URL      : https://www.freedesktop.org/software/vaapi/releases/libva-intel-driver/libva-intel-driver-1.7.2.tar.bz2
Source0  : https://www.freedesktop.org/software/vaapi/releases/libva-intel-driver/libva-intel-driver-1.7.2.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: libva-intel-driver-lib
BuildRequires : libdrm-dev
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(libva-wayland)
BuildRequires : pkgconfig(libva-x11)

%description
libva-intel-driver
VA driver for Intel G45 & HD Graphics family
License
-------
Please read the COPYING file available in this package.

%package lib
Summary: lib components for the libva-intel-driver package.
Group: Libraries

%description lib
lib components for the libva-intel-driver package.


%prep
%setup -q -n libva-intel-driver-1.7.2

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -O3 "
export FCFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -O3 "
export FFLAGS="$CFLAGS -falign-functions=32 -fno-semantic-interposition -O3 "
export CXXFLAGS="$CXXFLAGS -falign-functions=32 -fno-semantic-interposition -O3 "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/dri/i965_drv_video.so
