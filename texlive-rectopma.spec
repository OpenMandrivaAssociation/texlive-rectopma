# revision 19980
# category Package
# catalog-ctan /macros/latex/contrib/rectopma
# catalog-date 2010-10-02 17:24:09 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-rectopma
Version:	20101002
Release:	1
Summary:	Recycle top matter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rectopma
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rectopma.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rectopma.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Saves the arguments of \author and \title for reference (after
\maketitle) in a document. (\maketitle simply disposes of the
information, in the standard classes and some others.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rectopma/rectopma.sty
%doc %{_texmfdistdir}/doc/latex/rectopma/TestTitle.pdf
%doc %{_texmfdistdir}/doc/latex/rectopma/TestTitle.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
