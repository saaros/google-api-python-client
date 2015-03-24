Name:           python2-google-api-client
Version:        %{major_version}
Release:        %{minor_version}%{?dist}
Url:            http://github.com/ohmu/google-api-client
Summary:        Python 2 client library for Google's discovery based APIs
License:        ASL 2.0
Source0:        googleapipysdk-rpm-src.tar.gz
Requires:       python-httplib2, python-six, python-uri-templates, python2-oauth2client
BuildRequires:  pytest, python-unittest2, %{requires}
BuildArch:      noarch

%description
This is the Python 2 client library for Google's discovery based APIs. To
get started, please see the
http://google.github.io/google-api-python-client.  Additionally,
http://api-python-client-doc.appspot.com/ is available for all of the APIs
supported by this library.


%if %{?python3_sitelib:1}0
%package -n python3-google-api-client
Summary:        Python 3 client library for Google's discovery based APIs
Requires:       python3-httplib2, python3-six, python3-uri-templates, python3-oauth2client
BuildRequires:  python3-pytest, python3-unittest2, %{requires}
BuildArch:      noarch

%description -n python3-google-api-client
This is the Python 3 client library for Google's discovery based APIs. To
get started, please see the
http://google.github.io/google-api-python-client.  Additionally,
http://api-python-client-doc.appspot.com/ is available for all of the APIs
supported by this library.
%endif


%prep
%setup -q -n googleapipysdk


%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%if %{?python3_sitelib:1}0
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%endif


%check
python2 -m pytest
%if %{?python3_sitelib:1}0
python3 -m pytest
%endif



%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python_sitelib}/*

%if %{?python3_sitelib:1}0
%files -n python3-google-api-client
%defattr(-,root,root,-)
%doc LICENSE README.md
%{python3_sitelib}/*
%endif


%changelog
* Tue Mar 24 2015 Oskari Saarenmaa <os@ohmu.fi> - 1.3.1-50
- Initial
