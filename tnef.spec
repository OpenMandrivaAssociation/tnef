Summary:	Decodes MS-TNEF attachments
Name:		tnef
Version:	1.4.3
Release:	%mkrel 5
License:	GPL
Group:		Networking/Mail
URL:		http://sourceforge.net/projects/tnef/
Source0:	http://prdownloads.sourceforge.net/tnef/%{name}-%{version}.tar.bz2
BuildRequires:	mawk
BuildRequires:	gettext-devel
BuildRequires:	autoconf2.5
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-buildroot

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
%serverbuild

%configure2_5x

%make

%check
make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/FAQ
%{_bindir}/tnef
%{_mandir}/man1/tnef.1*
