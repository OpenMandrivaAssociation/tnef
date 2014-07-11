Summary:	Decodes MS-TNEF attachments
Name:		tnef
Version:	1.4.8
Release:	8
License:	GPL
Group:		Networking/Mail
URL:		http://sourceforge.net/projects/tnef/
Source0:	http://prdownloads.sourceforge.net/tnef/%{name}-%{version}.tar.gz
Patch0:		tnef-1.4.5-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	mawk
BuildRequires:	gettext-devel
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
TNEF is a program for unpacking MIME attachments of type "application/ms-tnef".
This is a Microsoft only attachment. Due to the proliferation of Microsoft
Outlook and Exchange mail servers, more and more mail is encapsulated into
this format. The TNEF program allows one to unpack the attachments which were
encapsulated into the TNEF attachment. Thus alleviating the need to use
Microsoft Outlook to view the attachment.

%prep

%setup -q
%patch0 -p0

%build
%serverbuild

%configure2_5x

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/FAQ
%{_bindir}/tnef
%{_mandir}/man1/tnef.1*


%changelog
* Wed Apr 20 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4.8-1mdv2011.0
+ Revision: 656186
- 1.4.8

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.4.7-2mdv2011.0
+ Revision: 608033
- rebuild

* Fri Feb 12 2010 Frederik Himpe <fhimpe@mandriva.org> 1.4.7-1mdv2010.1
+ Revision: 505081
- update to new version 1.4.7

* Thu Oct 15 2009 Oden Eriksson <oeriksson@mandriva.com> 1.4.6-1mdv2010.0
+ Revision: 457549
- 1.4.6

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.4.5-2mdv2010.0
+ Revision: 427407
- rebuild

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.5-1mdv2009.1
+ Revision: 316158
- 1.4.5
- fix build with -Werror=format-security (P0)

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.4.3-5mdv2009.0
+ Revision: 225775
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-4mdv2008.1
+ Revision: 179657
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 10 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-3mdv2008.0
+ Revision: 51031
- use the new %%serverbuild macro


* Tue Jan 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-2mdv2007.0
+ Revision: 109407
- rebuilt against new libintl major (8)

* Tue Dec 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-1mdv2007.1
+ Revision: 95320
- 1.4.3
- fix deps
- rebuild
- Import tnef

* Fri Aug 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-1mdv2007.0
- 1.4.2
- fix deps

* Fri Apr 28 2006 Oden Eriksson <oeriksson@mandriva.com> 1.4.1-1mdk
- 1.4.1

* Mon Dec 19 2005 Lenny Cartier <lenny@mandriva.com> 1.3.4-1mdk
- 1.3.4

* Fri May 27 2005 Lenny Cartier <lenny@mandriva.com> 1.3.3-1mdk
- 1.3.3

* Sun Mar 06 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 1.3.2-1mdk
- 1.3.2
- run the tests

* Tue Jun 08 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.3.1-2mdk
- rebuilt with gcc v3.4.x

* Sat Apr 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 1.2.3.1-1mdk
- 1.2.3.1

