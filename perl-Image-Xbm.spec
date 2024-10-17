%define upstream_name	 Image-Xbm
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Load, create, manipulate and save xbm image files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SU/SUMMER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Image::Base)
BuildArch:	noarch

%description
This class module provides basic load, manipulate and save functionality for
the xbm file format. It inherits from Image::Base which provides additional
manipulation functionality, e.g. new_from_image(). See the Image::Base pod for
information on adding your own functionality to all the Image::Base derived
classes.

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
%doc README
%{perl_vendorlib}/Image
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 402544
- update to 0.56

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.08-11mdv2009.0
+ Revision: 241489
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-9mdv2008.0
+ Revision: 86476
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-8mdv2007.0
- Rebuild

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-7mdk
- better summary and description
- spec cleanup
- better URL
- %%mkrel

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.08-6mdk
- fix buildrequires in a backward compatible way
- remove MANIFEST file

* Mon Nov 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.08-5mdk 
- rebuild

* Sat Aug 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.08-4mdk 
- fix directory ownership (distlint)
- make test

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.08-3mdk 
- rpmbuildupdate aware

