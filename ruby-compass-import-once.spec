#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	compass-import-once
Summary:	Speed up your Sass compilation by making @import only import each file once
Name:		ruby-%{pkgname}
Version:	1.0.5
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	2197cae9d2fa582007391f5ae60ad52b
URL:		https://github.com/chriseppstein/compass/tree/master/import-once
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-diff-lcs
BuildRequires:	ruby-rake
BuildRequires:	ruby-sass-globbing
%endif
Requires:	ruby-sass < 3.5
Requires:	ruby-sass >= 3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Changes the behavior of Sass's @import directive to only import a file
once.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/compass-import-once.rb
%{ruby_vendorlibdir}/compass/import-once.rb
%{ruby_vendorlibdir}/compass/import-once
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
