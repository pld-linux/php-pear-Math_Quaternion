%include	/usr/lib/rpm/macros.php
%define		_class		Math
%define		_subclass	Quaternion
%define		_status		beta

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Classes that define Quaternions and their operations
Summary(pl):	%{_class}_%{_subclass} - klasy definiuj±ce kwaterniony i operacje na nich
Name:		php-pear-%{_pearname}
Version:	0.7.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	c52ea340a25502696f0d013d4ec05be3
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Math_Quaternion/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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

This class has in PEAR status: %{_status}.

%description -l pl
Klasy s³u¿±ce do reprezentacji i obliczeñ na kwaternionach. Zawieraj±
definicje podstawowych dzia³añ arytmetycznych w tej statycznej klasie.
Kwaterniony s± rozszerzeniem idei liczb zespolonych; kwaternion jest
zdefiniowany jako:
q = a + b*i + c*j + d*k
W roku 1844 Hamilton opisa³ system, w którym liczby sk³adaj± siê z
czê¶ci rzeczywistej oraz 3 urojonych, niezale¿nych czê¶ci (i,j,k),
takich ¿e:
i^2 = j^2 = k^2 = -1  oraz
ij = k, jk = i, ki = j  oraz
ji = -k, kj = -i, ik = -j
Powy¿sze zasady znane s± jako "regu³y Hamiltona".

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/test/*
%{php_pear_dir}/%{_class}/*.php
