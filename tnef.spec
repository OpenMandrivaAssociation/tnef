Summary:	Decodes MS-TNEF attachments
Name:		tnef
Version:	1.4.18
Release:	1
License:	GPL
Group:		Networking/Mail
URL:		http://sourceforge.net/projects/tnef/
Source0:	https://github.com/verdammelt/tnef/archive/%{version}.tar.gz
BuildRequires:	mawk
BuildRequires:	gettext-devel
BuildRequires:	autoconf2.5
BuildRequires:	libtool

%description
TNEF is a program for unpacking MIME attachments of type "application/ms-tnef".
This is a Microsoft only attachment. Due to the proliferation of Microsoft
Outlook and Exchange mail servers, more and more mail is encapsulated into
this format. The TNEF program allows one to unpack the attachments which were
encapsulated into the TNEF attachment. Thus alleviating the need to use
Microsoft Outlook to view the attachment.

%prep
%setup -q

%build
autoreconf -fiv
%serverbuild
%configure

%make

%check
make check

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS THANKS doc/FAQ
%{_bindir}/tnef
%{_mandir}/man1/tnef.1*
