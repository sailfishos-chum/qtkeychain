Name:       opt-qt5-qtkeychain

%global qt_version 5.15.9

Summary:    Qt API for storing passwords securely
Version:    0.14.1
Release:    0
Group:      Applications
License:    BSD-3-Clause
URL:        https://github.com/frankosterfeld/qtkeychain
Source0:    %{name}-%{version}.tar.gz

# filter qml provides
%global __provides_exclude_from ^%{_opt_qt5_archdatadir}/qml/.*\\.so$
%{?opt_qt5_default_filter}

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig
BuildRequires:  cmake
BuildRequires:  opt-qt5-qtbase-devel >= %{qt_version}
BuildRequires:  opt-qt5-qtbase-private-devel >= %{qt_version}


%description
%{summary}.

%if "%{?vendor}" == "chum"
PackageName: opt-qt5-qtkeychain
PackagerName: nephros
Custom:
  Repo: https://github.com/frankosterfeld/qtkeychain
  PackagingRepo: https://github.com/sailfishos-chum/qtkeychain
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
cmake ..  \
    -DCMAKE_INSTALL_PREFIX=%{_opt_qt5_prefix} \
    -DBUILD_TEST_APPLICATION=0 \
    -DBUILD_TRANSLATIONS=0 \
    -DLIBSECRET_SUPPORT=0

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
cd build
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_opt_qt5_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_opt_qt5_libdir}/*.so
%{_opt_qt5_libdir}/cmake/*
%{_opt_qt5_includedir}/*
%{_opt_qt5_archdatadir}/*
