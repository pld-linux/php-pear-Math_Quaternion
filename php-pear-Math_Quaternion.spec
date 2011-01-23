%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Math_Quaternion
Summary:	%{_class}_%{_subclass} - Classes that define Quaternions and their operations
Summary(pl.UTF-8):	%{_class}_%{_subclass} - klasy definiujące kwaterniony i operacje na nich
Name:		php-pear-%{_pearname}
Version:	0.8.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f4dfc1b6b2bf0fc057835b2cbba186a1
URL:		http://pear.php.net/package/Math_Quaternion/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes that represent and manipulate quaternions. Contain definitions
for basic arithmetic functions in a static class.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasy służące do reprezentacji i obliczeń na kwaternionach. Zawierają
definicje podstawowych działań arytmetycznych w tej statycznej klasie.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Math/Quaternion.php
%{php_pear_dir}/Math/QuaternionOp.php

%{php_pear_dir}/data/%{_pearname}
