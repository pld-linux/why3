Summary:	Software verification platform
Name:		why3
Version:	1.4.0
Release:	2
License:	LGPLv2 with exceptions
Group:		Applications
Source0:	https://gforge.inria.fr/frs/download.php/38425/%{name}-%{version}.tar.gz
# Source0-md5:	9755cedf1edfcacff652149783e18647
URL:		http://why3.lri.fr/
BuildRequires:	camlp5
BuildRequires:	coq >= 8.13
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-graph-devel
BuildRequires:	ocaml-lablgtk3-devel
BuildRequires:	ocaml-lablgtk3-gtksourceview-devel
BuildRequires:	ocaml-menhir-devel
BuildRequires:	ocaml-num-devel
BuildRequires:	ocaml-sqlite-devel
BuildRequires:	ocaml-zarith-devel
BuildRequires:	rubber
BuildRequires:	sqlite3-devel
%requires_eq	ocaml-runtime
# same as ocaml-zarith
ExclusiveArch:	%{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	ocamlx?\\\(Why3\\\)

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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# Move the gtksourceview language file to the right place
install -d $RPM_BUILD_ROOT%{_datadir}/gtksourceview-3.0
%{__mv} $RPM_BUILD_ROOT%{_datadir}/%{name}/lang $RPM_BUILD_ROOT%{_datadir}/gtksourceview-3.0/language-specs

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md README.md
%attr(755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/gtksourceview-3.0/language-specs/why3.lang
%{_datadir}/gtksourceview-3.0/language-specs/why3c.lang
%{_datadir}/gtksourceview-3.0/language-specs/why3py.lang
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/coq
%{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/commands
%attr(755,root,root) %{_libdir}/%{name}/commands/*.cmxs
%attr(755,root,root) %{_libdir}/%{name}/why3-call-pvs
%attr(755,root,root) %{_libdir}/%{name}/why3cpulimit
%attr(755,root,root) %{_libdir}/%{name}/why3server

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
