%define __prefix /opt

Name:           kibana
Summary:        A browser based analytics and search dashboard for Elasticsearch
Version:        3.1.1
Release:        1%{?dist}
License:        Apache Software License 2.0
Group:          Application/System
Prefix:         %{_prefix}

Url:            http://www.elasticsearch.org/overview/kibana
Source0:        https://download.elasticsearch.org/kibana/kibana/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Kibana is an open source (Apache Licensed), browser based analytics and search dashboard for Elasticsearch. Kibana is a snap to setup and start using. Kibana strives to be easy to get started with, while also being flexible and powerful, just like Elasticsearch.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p %{buildroot}%{__prefix}/%{name}/
%{__cp} -r {app,css,favicon.ico,font,img,vendor,config.js,index.html} %{buildroot}%{__prefix}/%{name}/
%{__cp} -r {LICENSE.md,README.md} %{buildroot}%{__prefix}/%{name}/
%{__cp} config.js %{buildroot}%{__prefix}/%{name}/config.default.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{__prefix}/%{name}/app
%{__prefix}/%{name}/css
%{__prefix}/%{name}/favicon.ico
%{__prefix}/%{name}/font
%{__prefix}/%{name}/img
%{__prefix}/%{name}/config.default.js
%{__prefix}/%{name}/index.html
%{__prefix}/%{name}/LICENSE.md
%{__prefix}/%{name}/README.md
%{__prefix}/%{name}/vendor
%config(noreplace) %{__prefix}/%{name}/config.js

%changelog
* Thu Oct 08 2014 Alex Schultz <aschultz@next-development.com> - 3.1.1-1
- Kibana 3.1.1
