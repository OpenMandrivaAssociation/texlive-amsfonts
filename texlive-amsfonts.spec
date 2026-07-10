%global tl_name amsfonts
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.04
Release:	%{tl_revision}.1
Summary:	TeX fonts from the American Mathematical Society
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/amsfonts
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsfonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsfonts.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsfonts.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
An extended set of fonts for use in mathematics, including: extra
mathematical symbols; blackboard bold letters (uppercase only); fraktur
letters; subscript sizes of bold math italic and bold Greek letters;
subscript sizes of large symbols such as sum and product; added sizes of
the Computer Modern small caps font; cyrillic fonts (from the University
of Washington); Euler mathematical fonts. All fonts are provided as
Adobe Type 1 files, and all except the Euler fonts are provided as
Metafont source. The distribution also includes the canonical Type 1
versions of the Computer Modern family of fonts. Basic LaTeX support for
the symbol fonts is provided by amsfonts.sty, with names of individual
symbols defined in amssymb.sty. The Euler fonts are supported by
separate packages; details can be found in the documentation.

