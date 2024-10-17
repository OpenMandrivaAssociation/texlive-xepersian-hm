Name:		texlive-xepersian-hm
Version:	56272
Release:	2
Summary:	Fixes kashida feature in xepersian package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xepersian-hm
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian-hm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian-hm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xepersian-hm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The kashida feature in xepersian has problems with some fonts
such as the HM Series fonts and the XB Series fonts. This
package fixes these problems. The package requires xepersian
and l3keys2e.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/xelatex/xepersian-hm
%{_texmfdistdir}/tex/xelatex/xepersian-hm
%doc %{_texmfdistdir}/doc/xelatex/xepersian-hm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
