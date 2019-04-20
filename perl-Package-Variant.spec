#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Package-Variant
Version  : 1.003002
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/Package-Variant-1.003002.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/Package-Variant-1.003002.tar.gz
Summary  : Parameterizable packages
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Import::Into)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(strictures)

%description
NAME
Package::Variant - Parameterizable packages
SYNOPSIS
Creation of anonymous variants:

%package dev
Summary: dev components for the perl-Package-Variant package.
Group: Development
Provides: perl-Package-Variant-devel = %{version}-%{release}
Requires: perl-Package-Variant = %{version}-%{release}

%description dev
dev components for the perl-Package-Variant package.


%prep
%setup -q -n Package-Variant-1.003002

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Package/Variant.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Package::Variant.3
