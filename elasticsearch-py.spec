#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : elasticsearch-py
Version  : 2.4.0
Release  : 22
URL      : https://github.com/elastic/elasticsearch-py/archive/2.4.0.tar.gz
Source0  : https://github.com/elastic/elasticsearch-py/archive/2.4.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: elasticsearch-py-python
BuildRequires : PyYAML
BuildRequires : coverage
BuildRequires : funcsigs
BuildRequires : nose
BuildRequires : nosexcover-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pyaml
BuildRequires : pylibmc
BuildRequires : python-dev
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : six
BuildRequires : urllib3
BuildRequires : urllib3-python

%description
Python Elasticsearch Client
===========================
Official low-level client for Elasticsearch. Its goal is to provide common
ground for all Elasticsearch-related code in Python; because of this it tries
to be opinion-free and very extendable.

%package python
Summary: python components for the elasticsearch-py package.
Group: Default

%description python
python components for the elasticsearch-py package.


%prep
%setup -q -n elasticsearch-py-2.4.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
