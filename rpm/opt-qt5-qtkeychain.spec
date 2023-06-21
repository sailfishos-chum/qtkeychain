Name:       opt-qt5-qtkeychain

%global qt_version 5.15.9

Summary:    Qt API for storing passwords securely.
Version:    0.13.2
Release:    0
Group:      Applications
License:    BSD-3-clause
URL:        https://github.com/frankosterfeld/qtkeychain
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig
BuildRequires:  cmake
#BuildRequires:  opt-qt5-qmake
#BuildRequires:  opt-qt5-qttools-linguist >= %{qt_version}
BuildRequires:  opt-qt5-qtbase-devel >= %{qt_version}
BuildRequires:  opt-qt5-qtbase-private-devel >= %{qt_version}

%description
%{summary}.

%if "%{?vendor}" == "chum"
PackageName: opt-qt5-qtkeychain
PackagerName: nephros
Custom:
  Repo: https://github.com/frankosterfeld/qtkeychain
  PackagingRepo: https://gitlab.com/nephros/qtkeychain
Categories:
 - Library
%endif


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q -n %{name}-%{version}/upstream

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
cd build

export CMAKE_PREFIX_PATH=%{_opt_qt5_prefix}
cmake .  \
    -DBUILD_TEST_APPLICATION=0 \
    -DBUILD_TRANSLATIONS=0 \
    -DLIBSECRET_SUPPORT=0

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_includedir}/*
%{_datadir}/qt5/*
