Summary: NethServer Business
Name: nethserver-business
Version: 1.0.2
Release: 1%{?dist}
License: GPL
Source0: %{name}-%{version}.tar.gz
Source1: %{name}-cockpit.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name} 

Requires: nethserver-base
Requires: nethserver-mssql
Requires: nethserver-samba

BuildRequires: nethserver-devtools

%description
Business Cube 2 integration for NethServer

%prep
%setup

%build
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
tar xvf %{SOURCE1} -C %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%clean
rm -rf %{buildroot}

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update
%attr(0440,root,root) /etc/sudoers.d/50_nsapi_nethserver_business


%changelog
* Fri Mar 26 2021 Federico Ballarini <fed.ballarini@gmail.com> - 1.0.2-1
- Business Cube: unable to start update procedure - Bug NethServer/dev#6467

* Thu Nov 26 2020 Federico Ballarini <fed.ballarini@gmail.com> - 1.0.1-1
- Business Cube: unable to work into Agg/Sbc folder - Bug NethServer/dev#6332
- Business Cube: improve Cockpit interface - Bug NethServer/dev#6349

* Thu Jul 16 2020 Federico Ballarini <fed.ballarini@gmail.com> - 1.0.0-1
- Initial package
