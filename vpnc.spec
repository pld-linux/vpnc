%define		_beta	rm+zomb.1
Summary:	VPN Client for Cisco EasyVPN
Summary(pl):	Klient VPN dla Cisco EasyVPN
Name:		vpnc
Version:	0.2
Release:	0.%{_beta}.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.unix-ag.uni-kl.de/~massar/vpnc/%{name}-%{version}-%{_beta}.tar.gz
# Source0-md5:	ded67de747874c4245ed8405146dc94a
URL:		http://www.unix-ag.uni-kl.de/~massar/vpnc/
BuildRequires:	libgcrypt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A VPN client compatible with Cisco's EasyVPN equipment.

%description -l pl
Klient VPN kompatybilny ze sprz�tem Cisco obs�uguj�cym EasyVPN.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
%{__make} \
	CFLAGS="%{rpmcflags} -g '-DVERSION=\"%{version}-%{_beta}\"'"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir},%{_mandir}/man8}

install %{name}		$RPM_BUILD_ROOT%{_bindir}
install %{name}-*	$RPM_BUILD_ROOT%{_bindir}
install %{name}.conf	$RPM_BUILD_ROOT%{_sysconfdir}
install %{name}.8	$RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/%{name}.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
