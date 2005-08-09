Summary:	VPN Client for Cisco EasyVPN
Summary(pl):	Klient VPN dla Cisco EasyVPN
Name:		vpnc
Version:	0.3.3
Release:	2
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.unix-ag.uni-kl.de/~massar/vpnc/%{name}-%{version}.tar.gz
# Source0-md5:	e7518cff21326fe7eb9795b60c25ae6a
Source1:	%{name}cfg
Patch0:		%{name}-bash.patch
URL:		http://www.unix-ag.uni-kl.de/~massar/vpnc/
BuildRequires:	libgcrypt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A VPN client compatible with Cisco's EasyVPN equipment.

%description -l pl
Klient VPN kompatybilny ze sprzêtem Cisco obs³uguj±cym EasyVPN.

%prep
%setup -q 
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags} -g '-DVERSION=\"%{version}\"'"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{_mandir}/man8,/var/run/%{name}}

install %{name}		$RPM_BUILD_ROOT%{_bindir}
install %{name}-*	$RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1}	$RPM_BUILD_ROOT%{_bindir}
install pcf2vpnc	$RPM_BUILD_ROOT%{_bindir}
install %{name}.conf	$RPM_BUILD_ROOT%{_sysconfdir}
install %{name}.8	$RPM_BUILD_ROOT%{_mandir}/man8
ln -sf %{_bindir}/vpnc-script $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/%{name}.conf
%{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/*
%dir /var/run/%{name}
%{_mandir}/man8/*
