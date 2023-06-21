# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       qt5keychain

# >> macros
# << macros

Summary:    Qt API for storing passwords securely.
Version:    0.14.1
Release:    0
Group:      Applications
License:    BSD-3-clause
URL:        https://github.com/frankosterfeld/qtkeychain
Source0:    %{name}-%{version}.tar.gz
Source100:  qt5keychain.yaml
Patch0:     cmake-version.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig
BuildRequires:  cmake
BuildRequires:  qt5-qmake
BuildRequires:  qt5-qttools-linguist

%description
%{summary}.

%if "%{?vendor}" == "chum"
PackageName: qtkeychain
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

# cmake-version.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

%cmake .  \
    -DBUILD_TEST_APPLICATION=0 \
    -DBUILD_TRANSLATIONS=0 \
    -DLIBSECRET_SUPPORT=0

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%license COPYING
%{_libdir}/*.so.*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_includedir}/*
%{_datadir}/qt5/*

# << files devel
