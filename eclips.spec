Summary:	EFL based image viewer
Summary(pl.UTF-8):	Przeglądarka obrazków oparta na EFL
Name:		eclips
Version:	0.0.4
%define	_snap	20050702
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Applications
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/misc/%{name}-%{_snap}.tar.gz
# Source0-md5:	14402490ec8f362e349c02c60a8723ac
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	etox-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eclips is an image viewer based on Ecore, Evas and Imlib2. It is
designed to do one thing and one thing only: display refreshing
slideshows or single images (webcams) while providing variable desktop
translucency to blend easily into the background. Eclips is
specialized in cool effects like fading in and out when changing
images, keeping constant background transparency to provide three or
more visual layers, and many more.

%description -l pl.UTF-8
eclips to przeglądarka obrazków oparta na bibliotekach Ecore, Evas i
Imlib2. Została zaprojektowana do jednej rzeczy i tylko jednej rzeczy:
wyświetlania odświeżanych przeglądów slajdów albo pojedynczych
obrazków (kamer internetowych) udostępniając zmienną przezroczystość
pulpitu przechodzącą w tło. Eclips jest specjalizowany w fajnych
efektach, takich jak przejścia przy zmianie obrazków, utrzymywanie
stałej przezroczystości tła dla zapewnienia trzech lub więcej
widocznych warstw i wiele więcej.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
