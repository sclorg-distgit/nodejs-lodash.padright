%{?scl:%scl_package nodejs-lodash.padright}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-lodash.padright

%global npm_name lodash.padright
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-lodash.padright
Version:	3.1.1
Release:	2%{?dist}
Summary:	The modern build of lodash’s `_.padRight` as a module.
Url:		https://lodash.com/
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
%endif

BuildRequires:	%{?scl_prefix}npm(lodash._basetostring)
BuildRequires:	%{?scl_prefix}npm(lodash._createpadding)

Requires:	%{?scl_prefix}npm(lodash._basetostring)
Requires:	%{?scl_prefix}npm(lodash._createpadding)

%description
The modern build of lodash’s `_.padRight` as a module.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/lodash.padright

%doc README.md LICENSE.txt

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.1-2
- rebuilt

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 3.1.1-1
- Initial build
