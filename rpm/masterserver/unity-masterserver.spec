# Some defines for sanity
%define zipname MasterServer

Name: unity-masterserver		
Version: 2.0.1f1	
Release: 1%{?dist}
Summary: Unity Master Server pre-built Binary for sane Admins	

License: GPL
URL:	http://unity3d.com/master-server	
Source0: http://unity3d.com/files/master-server/%{zipname}-2.0.1f1.zip
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXX)
Patch0: linux-unity.patch	

%description
Unity Master Server 

%prep -T -c -n MasterServer
unzip -o %{SOURCE0}
%patch0 -p1

%build
make all

%install
mkdir -p  %{buildroot}/usr/bin
mkdir -p  %{buildroot}/etc/init.d/
install -m 755 config/unity-masterserver  %{buildroot}/etc/init.d/
install -m 755 MasterServer %{buildroot}/usr/bin/MasterServer

%clean
rm -rf ./*
rm -rf %{buildroot}

%files
/etc/init.d/unity-masterserver
/usr/bin/MasterServer

%changelog
* Sun Nov 2 2014 Jim Gorz <nrezinorn@gmail.com> - 2.0.1f
- Initial Build
