%define		_class		Image
%define		_subclass	Graph
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.8.0
Release:	2
Summary:	A package for displaying (numerical) data as a graph/chart/plot
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Image_Graph
Source0:	http://download.pear.php.net/package/Image_Graph-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires(post): php-gd
Requires(preun): php-gd
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Image_Graph provides a set of classes that creates
graphs/plots/charts based on (numerical) data. Many different plot
types are supported: Bar, line, area, step, impulse, scatter,
radar, pie, map, candlestick, band, box & whisker and smoothed
line, area and radar plots. The graph is highly customizable,
making it possible to get the exact look and feel that is
required. The output is controlled by a driver mechanism, which
facilitates easy output to many different output formats, amongst
others, GD (PNG, JPEG, GIF, WBMP), PDF (using PDFLib), ShockWave
Flash (using Ming) and Scalable Vector Graphics (SVG). Image_Graph
is compatible with both PHP4 and PHP5 and can be used with both
GD1 and GD2 (GD2 is recommended)

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-10mdv2012.0
+ Revision: 742020
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-9
+ Revision: 679372
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-8mdv2011.0
+ Revision: 613691
- the mass rebuild of 2010.1 packages

* Fri Dec 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.2-7mdv2010.1
+ Revision: 473544
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.2-6mdv2010.0
+ Revision: 441197
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-5mdv2009.1
+ Revision: 322159
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-4mdv2009.0
+ Revision: 236897
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 06 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-3mdv2008.1
+ Revision: 106351
- fix #35340 (PHP Pear Image_Graph does not install correctly)


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-2mdv2007.0
+ Revision: 81902
- Import php-pear-Image_Graph

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-2mdk
- rule out some more faulty deps

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-1mdk
- 0.7.2
- rule out faulty deps

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-1mdk
- 0.7.1
- new group (Development/PHP)

* Tue Sep 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-7mdk
- fix deps

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2mdk
- fix deps

* Sun May 29 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-1mdk
- initial Mandriva package


