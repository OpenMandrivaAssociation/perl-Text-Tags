%define module	Text-Tags
%define name	perl-%{module}
%define version 0.04
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release:	%{release} 
Summary:	Perl module to parse "folksonomy" space-separated tags
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Parses "folksonomies", which are 
simple space-or-comma-separated-but-optionally-quoted tag lists.

Specifically, tags can be any string, as long as they don't contain both a 
single and a double quote. Hopefully, this is a pretty obscure restriction. 
In addition, all whitespace inside tags is normalized to a single space 
(with no leading or trailing whitespace).

In a tag list string, tags can optionally be quoted with either single or 
double quotes. There is no escaping of either kind of quote, although you 
can include one type of quote inside a string quoted with the other. Quotes 
can also just be included inside tags, as long as they aren't at the 
beginning; thus a tag like joe's can just be entered without any extra quoting. 
Tags are separated by whitespace and/or commas, though quoted tags can run into 
each other without whitespace. Empty tags (put in explicitly with "" or '') are
ignored. (Note that commas are not normalized with whitespace, and can be 
included in a tag if you quote them.)

Why did the previous paragraph need to be so detailed? Because 
Text::Tags::Parser always successfully parses every line. That is, every single 
tags line converts into a list of tags, without any error conditions. For 
general use, you can just understand the rules as being separate tags with 
spaces or commas, and put either kind of quotes around tags that need to have 
spaces.


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/man3/*

