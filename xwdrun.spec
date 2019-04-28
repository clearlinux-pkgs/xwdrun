#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xwdrun
Version  : 1
Release  : 1
URL      : http://localhost/cgit/projects/xwdrun/snapshot/xwdrun-1.tar.bz2
Source0  : http://localhost/cgit/projects/xwdrun/snapshot/xwdrun-1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT-Opengroup
Requires: xwdrun-bin = %{version}-%{release}
Requires: xwdrun-license = %{version}-%{release}
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xkbfile)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)

%description
xwd - dump an image of an X window
All questions regarding this software should be directed at the
Xorg mailing list:

%package bin
Summary: bin components for the xwdrun package.
Group: Binaries
Requires: xwdrun-license = %{version}-%{release}

%description bin
bin components for the xwdrun package.


%package license
Summary: license components for the xwdrun package.
Group: Default

%description license
license components for the xwdrun package.


%prep
%setup -q -n xwdrun-1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556491704
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1556491704
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xwdrun
cp COPYING %{buildroot}/usr/share/package-licenses/xwdrun/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xwdrun

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xwdrun/COPYING
