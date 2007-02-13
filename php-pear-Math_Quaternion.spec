%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Quaternion
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_class}_%{_subclass} - Classes that define Quaternions and their operations
Summary(pl.UTF-8):	%{_class}_%{_subclass} - klasy definiujące kwaterniony i operacje na nich
Name:		php-pear-%{_pearname}
Version:	0.7.1
Release:	4
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	c52ea340a25502696f0d013d4ec05be3
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Math_Quaternion/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes that represent and manipulate quaternions. Contain definitions
for basic arithmetic functions in a static class. Quaternions are an
extension of the idea of complex numbers, and a quaternion is defined as:
q = a + b*i + c*j + d*k
In 1844 Hamilton described a system in which numbers were composed of
a real part and 3 imaginary and independent parts (i,j,k), such that:
i^2 = j^2 = k^2 = -1 and
ij = k, jk = i, ki = j and
ji = -k, kj = -i, ik = -j
The above are known as "Hamilton's rules".

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasy służące do reprezentacji i obliczeń na kwaternionach. Zawierają
definicje podstawowych działań arytmetycznych w tej statycznej klasie.
Kwaterniony są rozszerzeniem idei liczb zespolonych; kwaternion jest
zdefiniowany jako:
q = a + b*i + c*j + d*k
W roku 1844 Hamilton opisał system, w którym liczby składają się z
części rzeczywistej oraz 3 urojonych, niezależnych części (i,j,k),
takich że:
i^2 = j^2 = k^2 = -1  oraz
ij = k, jk = i, ki = j  oraz
ji = -k, kj = -i, ik = -j
Powyższe zasady znane są jako "reguły Hamiltona".

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

install -d ./%{php_pear_dir}/tests/%{_pearname}
mv ./%{php_pear_dir}/{%{_class}/test/*,tests/%{_pearname}}

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
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
