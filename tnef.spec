Summary:	Decodes MS-TNEF attachments
Name:		tnef
Version:	1.4.6
Release:	%mkrel 1
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
