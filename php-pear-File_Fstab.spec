%include	/usr/lib/rpm/macros.php
%define         _class          File
%define         _subclass       Fstab
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - read and write fstab files
Summary(pl):	%{_pearname} - odczyt i zapis plików fstab
Name:		php-pear-%{_pearname}
Version:	2.0.0
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	71bdfc8f6773364dd540e024feb93921
URL:		http://pear.php.net/package/Class_Subclass/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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
File_Fstab to ³atwy w u¿yciu pakiet odczytuj±cy i zapisuj±cy uniksowe
pliki fstab. Oferuje on mi³y zorientowany obiektowo interfejs do
fstaba. Cechy pakietu:
- obs³uguje okre¶lanie urz±dzenia poprzez urz±dzenie blokowe, etykietê
  i UUID
- rozszerzalny w celu analizy niestandardowych formatów fstab poprzez
  zdefiniowanie nowej klasy Entry dla danego formatu
- ³atwe sprawdzanie i ustawianie opcji montowania dla danej pozycji
- stabilny, funkcjonalny interfejs
- w pe³ni udokumentowany przy u¿yciu PHPDoc.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/Entry.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/example.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
