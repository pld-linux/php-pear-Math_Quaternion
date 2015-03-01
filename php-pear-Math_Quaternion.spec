%define		status		beta
%define		pearname	Math_Quaternion
%include	/usr/lib/rpm/macros.php
Summary:	Classes that define Quaternions and their operations
Summary(pl.UTF-8):	klasy definiujące kwaterniony i operacje na nich
Name:		php-pear-%{pearname}
Version:	0.8.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
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

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Klasy służące do reprezentacji i obliczeń na kwaternionach. Zawierają
definicje podstawowych działań arytmetycznych w tej statycznej klasie.

Ta klasa ma w PEAR status: %{status}.

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
%{php_pear_dir}/data/%{pearname}
