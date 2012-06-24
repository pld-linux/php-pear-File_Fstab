%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	Fstab
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - read and write fstab files
Summary(pl):	%{_pearname} - odczyt i zapis plik�w fstab
Name:		php-pear-%{_pearname}
Version:	2.0.2
Release:	3
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	39eb66d6d26cd8cecc9c01dc002365f5
URL:		http://pear.php.net/package/File_Fstab/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File_Fstab is an easy-to-use package which can read & write UNIX fstab
files. It presents a pleasant object-oriented interface to the fstab.
Features:
- Supports blockdev, label, and UUID specification of mount device.
- Extendable to parse non-standard fstab formats by defining a new
  Entry class for that format.
- Easily examine and set mount options for an entry.
- Stable, functional interface.
- Fully documented with PHPDoc.

In PEAR status of this package is: %{_status}.

%description -l pl
File_Fstab to �atwy w u�yciu pakiet odczytuj�cy i zapisuj�cy uniksowe
pliki fstab. Oferuje on mi�y zorientowany obiektowo interfejs do
fstaba. Cechy pakietu:
- obs�uguje okre�lanie urz�dzenia poprzez urz�dzenie blokowe, etykiet�
  i UUID
- rozszerzalny w celu analizy niestandardowych format�w fstab poprzez
  zdefiniowanie nowej klasy Entry dla danego formatu
- �atwe sprawdzanie i ustawianie opcji montowania dla danej pozycji
- stabilny, funkcjonalny interfejs
- w pe�ni udokumentowany przy u�yciu PHPDoc.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv ./%{php_pear_dir}/docs .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/example.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
