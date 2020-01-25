%define		php_min_version 5.0.0
Summary:	Markdown text-to-html converter
Name:		php-markdown
Version:	1.0.1o
Release:	2
License:	BSD-Style License
Group:		Development/Languages/PHP
Source0:	http://littoral.michelf.ca/code/php-markdown/%{name}-%{version}.zip
# Source0-md5:	fccaa1285c27a82bea15385591856250
URL:		http://michelf.ca/projects/php-markdown/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
BuildRequires:	unzip
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautopear	pear
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
PHP Markdown is a port to PHP of the Markdown program written by John
Gruber. Markdown is two things: a plain text markup syntax, and a
software tool that converts the plain text markup to HTML for
publishing on the web.

The Markdown syntax allows you to write text naturally and format it
without using HTML tags. More importantly: in Markdown format, your
text stays enjoyable to read for a human being, and this is true
enough that it makes a Markdown document publishable as-is, as plain
text. If you are using text-formatted email, you already know some
part of the syntax.

%prep
%setup -qc
mv "PHP Markdown %{version}"/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p markdown.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.text
%{php_data_dir}/markdown.php
