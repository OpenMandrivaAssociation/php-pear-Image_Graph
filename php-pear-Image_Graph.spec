%define		_class		Image
%define		_subclass	Graph
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.7.2
Release:	%mkrel 7
Summary:	A package for displaying (numerical) data as a graph/chart/plot
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Image_Graph
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires(post): php-gd
Requires(preun): php-gd
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
