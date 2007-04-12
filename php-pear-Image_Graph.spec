%define name php-pear-Image_Graph
%define rname Image_Graph

%define _provides_exceptions pear(docs
%define _requires_exceptions pear(Image/Graph/Color.php)\\|pear(Image/Canvas.php)

%define pear_phpdir %{_datadir}/pear
%define pear_docdir %{_datadir}/pear/docs
%define pear_extdir %{_libdir}/php/extensions
%define pear_datadir %{_datadir}/pear/data
%define pear_testdir %{_datadir}/pear/tests

Summary:	A package for displaying (numerical) data as a graph/chart/plot
Name:		%{name}
Version:	0.7.2
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Image_Graph
Source0:	http://pear.php.net/get/%{rname}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires(post): php-gd
Requires(preun): php-gd
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-buildroot

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

%setup -q -n %rname-%version
mv ../package.xml .

find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
find -type f | grep -v "\.gif" | grep -v "\.png" | grep -v "\.jpg" | xargs dos2unix -U

%build

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{pear_phpdir}/Image/Graph
install -d %{buildroot}%{pear_phpdir}/packages
install -d %{buildroot}%{pear_docdir}/Image/Graph/examples

install -m0644 Graph.php %{buildroot}%{pear_phpdir}/Image/Graph.php
cp -aRf Graph/* %{buildroot}%{pear_phpdir}/Image/Graph/
cp -aRf docs/examples/* %{buildroot}%{pear_docdir}/Image/Graph/examples/

find %{buildroot} -type f -exec sed -i 's|^#!/usr/local/bin/php|#!/usr/bin/php|' {} \;
install -m0644 package.xml %{buildroot}%{pear_phpdir}/packages/%{rname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{pear_phpdir}/Image/Graph
%dir %{pear_phpdir}/Image/Graph/Axis
%dir %{pear_phpdir}/Image/Graph/Axis/Marker
%dir %{pear_phpdir}/Image/Graph/DataPreprocessor
%dir %{pear_phpdir}/Image/Graph/DataSelector
%dir %{pear_phpdir}/Image/Graph/Dataset
%dir %{pear_phpdir}/Image/Graph/Figure
%dir %{pear_phpdir}/Image/Graph/Fill
%dir %{pear_phpdir}/Image/Graph/Grid
%dir %{pear_phpdir}/Image/Graph/Images
%dir %{pear_phpdir}/Image/Graph/Images/Icons
%dir %{pear_phpdir}/Image/Graph/Images/Maps
%dir %{pear_phpdir}/Image/Graph/Layout
%dir %{pear_phpdir}/Image/Graph/Line
%dir %{pear_phpdir}/Image/Graph/Marker
%dir %{pear_phpdir}/Image/Graph/Marker/Pointing
%dir %{pear_phpdir}/Image/Graph/Plot
%dir %{pear_phpdir}/Image/Graph/Plot/Fit
%dir %{pear_phpdir}/Image/Graph/Plot/Smoothed
%dir %{pear_phpdir}/Image/Graph/Plotarea

%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Axis/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Axis/Marker/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/DataPreprocessor/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/DataSelector/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Dataset/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Figure/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Fill/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Grid/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Images/Icons/*.png
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Images/Maps/README
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Layout/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Line/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Marker/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Marker/Pointing/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Plot/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Plot/Fit/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Plot/Smoothed/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/Plotarea/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/Graph/*.php
%attr(0644,root,root) %{pear_phpdir}/Image/*.php

%dir %{pear_docdir}/Image/Graph/examples
%dir %{pear_docdir}/Image/Graph/examples/data
%dir %{pear_docdir}/Image/Graph/examples/images

%attr(0644,root,root) %{pear_docdir}/Image/Graph/examples/*.php
%attr(0644,root,root) %{pear_docdir}/Image/Graph/examples/*.html
%attr(0644,root,root) %{pear_docdir}/Image/Graph/examples/images/*.png
%attr(0644,root,root) %{pear_docdir}/Image/Graph/examples/images/*.jpg
%attr(0644,root,root) %{pear_docdir}/Image/Graph/examples/*.png
%attr(0644,root,root) %{pear_docdir}/Image/Graph/examples/data/*.txt
%attr(0644,root,root) %{pear_phpdir}/packages/%{rname}.xml


