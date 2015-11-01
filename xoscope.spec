Name:		xoscope
Version:	2.1 
Release:	1%{?dist}
Summary:	a digital oscilloscope using input from a sound card                 
License:	GPLv2
URL:		http://sourceforge.net/projects/xoscope
Source0:	http://xoscope.sourceforge.net/%{name}-%{version}.tar.gz 

  
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gtk2-devel >= 2.18
BuildRequires:	libtool
BuildRequires:	perl-devel
BuildRequires:	comedilib-devel
BuildRequires:  gtkdatabox-devel >= 0.9.2
BuildRequires:	fftw3-devel
Requires:       gtk2
Requires:	pulseaudio-utils
Requires:	pulseaudio-esound-compat
%description
Sound card oscilloscope data visualizer for EsounD and/or a ProbeScope/osziFOX 
 

%prep
%setup -q


%build
%configure
make  %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc %{_datadir}/man/man1/%{name}.1.gz
%doc %{_datadir}/pixmaps/
%doc /usr/bin/%{name}


%changelog
* Thu Oct 29 2015 petev <pete0verse@gmail.com> 2.1-1
- Initial package
