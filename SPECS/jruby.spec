
%define _jprefix         /opt/jruby

Name: jruby
Version: 1.7.9
Release: 2%{?dist}
License: EPL/GPL/LGPL
Group: Development/Languages
URL: http://jruby.org
Summary: A Java implementation of the Ruby language
Source0:  http://jruby.org.s3.amazonaws.com/downloads/%{version}/%{name}-bin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: jre >= 1.6.0

%description
A Java implementation of the Ruby language

%prep

%setup -q

%build

%install
rm -rf      $RPM_BUILD_ROOT
mkdir -p    $RPM_BUILD_ROOT%{_jprefix}
mkdir -p    $RPM_BUILD_ROOT%{_bindir}
mkdir -p    $RPM_BUILD_ROOT%{_docdir}/%{name}
ln -s       %{_jprefix}/bin/jruby $RPM_BUILD_ROOT%{_bindir}/jruby

cp -r       $RPM_BUILD_DIR/%{name}-%{version}/*       $RPM_BUILD_ROOT/%{_jprefix}
cp -r       $RPM_BUILD_DIR/%{name}-%{version}/docs/*  $RPM_BUILD_ROOT/%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}
%{_jprefix}
%{_bindir}/jruby

%changelog
* Wed Jul 30 2014 Pavel Chechetin <paulche@yandex.ru> 1.7.9-2
- Customize instalation path 
* Wed Jan 8 2014 Simon Thulbourn <simon.thulbourn@bbc.co.uk> 1.7.9-1
- Initial release
