Name:		texlive-rectopma
Version:	19980
Release:	2
Summary:	Recycle top matter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rectopma
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rectopma.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rectopma.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
