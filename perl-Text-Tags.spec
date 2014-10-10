%define upstream_name	 Text-Tags
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module to parse "folksonomy" space-separated tags
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 406190
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.04-4mdv2009.0
+ Revision: 242056
- rebuild
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-2mdv2008.0
+ Revision: 87031
- rebuild


* Thu Jun 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2007.0
- New release 0.04
- spec cleanup
- HTTP source URL

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.03-2mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Fri Mar 03 2006 Michael Scherer <misc@mandriva.org> 0.03-1mdk
- New release 0.03

* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 0.02-2mdk
- Do not ship empty dir

* Wed Sep 21 2005 Michael Scherer <misc@mandriva.org> 0.02-1mdk
- First mandriva package

