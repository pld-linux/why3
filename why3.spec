Summary:	Software verification platform
Name:		why3
Version:	0.83
Release:	1
Group:		Applications
License:	LGPLv2 with exceptions
Source0:	https://gforge.inria.fr/frs/download.php/33490/%{name}-%{version}.tar.gz
# Source0-md5:	35f99e5f64939e50ea57f641ba2073ec
URL:		http://why3.lri.fr/
BuildRequires:	camlp5
BuildRequires:	coq >= 8.4
BuildRequires:	evince
BuildRequires:	gtksourceview2-devel
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-graph-devel
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	ocaml-lablgtk2-gtksourceview2-devel
BuildRequires:	ocaml-sqlite-devel
BuildRequires:	ocaml-zarith-devel
BuildRequires:	rubber
BuildRequires:	sqlite3-devel
Requires:	gtksourceview2
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Why3 is the next generation of the Why software verification platform.
Why3 clearly separates the purely logical specification part from
generation of verification conditions for programs. It features a rich
library of proof task transformations that can be chained to produce a
suitable input for a large set of theorem provers, including SMT
solvers, TPTP provers, as well as interactive proof assistants.

%package examples
Summary:	Example problems for why3
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description examples
Example problems for why3.

%prep
%setup -q

%build
%configure \
	--enable-doc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Move the gtksourceview language file to the right place
install -d $RPM_BUILD_ROOT%{_datadir}/gtksourceview-2.0
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/lang $RPM_BUILD_ROOT%{_datadir}/gtksourceview-2.0/language-specs

cp -a examples/* $RPM_BUILD_ROOT/%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README doc/manual.pdf
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/gtksourceview-2.0/language-specs/why3.lang
%{_libdir}/%{name}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
