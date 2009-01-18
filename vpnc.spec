#
# Conditional build:
%bcond_with	openssl		# with openssl support (possible GPL violation)
#
Summary:	VPN Client for Cisco EasyVPN
Summary(pl.UTF-8):	Klient VPN dla Cisco EasyVPN
Name:		vpnc
Version:	0.5.3
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.unix-ag.uni-kl.de/~massar/vpnc/%{name}-%{version}.tar.gz
# Source0-md5:	4378f9551d5b077e1770bbe09995afb3
Source1:	%{name}cfg
Patch0:		%{name}-bash.patch
URL:		http://www.unix-ag.uni-kl.de/~massar/vpnc/
BuildRequires:	libgcrypt-devel
%{?with_openssl:BuildRequires:	openssl-devel}
BuildRequires:	perl-base
Requires:	bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A VPN client compatible with Cisco's EasyVPN equipment.

%description -l pl.UTF-8
Klient VPN kompatybilny ze sprzętem Cisco obsługującym EasyVPN.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall '-DVERSION=\"%{version}\"'%{?with_openssl: -DOPENSSL_GPL_VIOLATION}" \
	%{?with_openssl:OPENSSLLIBS="-lcrypto"}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/%{name},%{_mandir}/man{1,8},/var/run/%{name}}

install %{name}		$RPM_BUILD_ROOT%{_bindir}
install cisco-decrypt	$RPM_BUILD_ROOT%{_bindir}
install %{name}-{disconnect,script}	$RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1}	$RPM_BUILD_ROOT%{_bindir}
install pcf2vpnc	$RPM_BUILD_ROOT%{_bindir}
install %{name}.conf	$RPM_BUILD_ROOT%{_sysconfdir}
install %{name}.8	$RPM_BUILD_ROOT%{_mandir}/man8
install *.1		$RPM_BUILD_ROOT%{_mandir}/man1
ln -sf %{_bindir}/vpnc-script $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_sysconfdir}/%{name}
%attr(755,root,root) %{_bindir}/*
%dir /var/run/%{name}
%{_mandir}/man8/*
%{_mandir}/man1/*
