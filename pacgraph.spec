%define		commit e495c03
Summary:	Draws a graph of installed packages
Name:		pacgraph
Version:	20110717
Release:	0.1
License:	GPL
Group:		Applications
Source0:	https://download.github.com/keenerd-%{name}-%{commit}.tar.gz
# Source0-md5:	fdf09c8cdea9c9e58c6fc2acc79a0528
Patch0:		%{name}-pld.patch
URL:		http://kmkeen.com/pacgraph/
Requires:	python3
Requires:	python3-modules
Suggests:	ImageMagick
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Render a graph of installed packages to console, svn or png image.
Good for finding bloat.

%package tk
Summary:	Interactive tk based GUI for %{name}
Group:		Applications
Requires:	python3-tkinter

%description tk
Interactive tk based GUI for %{name}

%prep
%setup -qn keenerd-%{name}-%{commit}
%patch0 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT

install -D pacgraph $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -D pacgraph-tk $RPM_BUILD_ROOT/%{_bindir}/%{name}-tk
install -D %{name}.1 $RPM_BUILD_ROOT/%{_mandir}/man1/%{name}.1

find $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-tk
