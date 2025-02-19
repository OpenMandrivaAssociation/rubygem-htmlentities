%define oname htmlentities

Name:       rubygem-%{oname}
Version:    4.2.2
Release:    3
Summary:    A module for encoding and decoding (X)HTML entities
Group:      Development/Ruby
License:    MIT
URL:        https://htmlentities.rubyforge.org/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
A module for encoding and decoding (X)HTML entities.

%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/perf/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING.txt
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sun Dec 19 2010 Rémy Clouard <shikamaru@mandriva.org> 4.2.2-2mdv2011.0
+ Revision: 623063
- fix file list
- bump release

* Sat Oct 09 2010 Rémy Clouard <shikamaru@mandriva.org> 4.2.1-1mdv2011.0
+ Revision: 584333
- import rubygem-htmlentities

