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
Requires(pre):	texlive-tlpkg
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

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/tex/plain
%dir %{_datadir}/texmf-dist/doc/fonts/amsfonts
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/source/latex/amsfonts
%dir %{_datadir}/texmf-dist/tex/latex/amsfonts
%dir %{_datadir}/texmf-dist/tex/plain/amsfonts
%dir %{_datadir}/texmf-dist/fonts/afm/public/amsfonts
%dir %{_datadir}/texmf-dist/fonts/map/dvips/amsfonts
%dir %{_datadir}/texmf-dist/fonts/source/public/amsfonts
%dir %{_datadir}/texmf-dist/fonts/tfm/public/amsfonts
%dir %{_datadir}/texmf-dist/fonts/type1/public/amsfonts
%dir %{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm
%dir %{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra
%dir %{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic
%dir %{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler
%dir %{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont
%dir %{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols
%dir %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra
%dir %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic
%dir %{_datadir}/texmf-dist/fonts/source/public/amsfonts/dummy
%dir %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols
%dir %{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra
%dir %{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic
%dir %{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/dummy
%dir %{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler
%dir %{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols
%dir %{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm
%dir %{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra
%dir %{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic
%dir %{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler
%dir %{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont
%dir %{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols
%doc %{_datadir}/texmf-dist/doc/fonts/amsfonts/OFL-FAQ.txt
%doc %{_datadir}/texmf-dist/doc/fonts/amsfonts/OFL.txt
%doc %{_datadir}/texmf-dist/doc/fonts/amsfonts/README
%doc %{_datadir}/texmf-dist/doc/fonts/amsfonts/amsfndoc.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/amsfonts/amsfonts.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/amsfonts/amssymb.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/amsfonts/cmmib57.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/amsfonts/eufrak.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/amsfonts/euscript.pdf
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmb10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbsy10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx12.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx6.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbx9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbxsl10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmbxti10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmcsc10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmdunh10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmex10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmff10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmfi10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmfib8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cminch.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmitt10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi12.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi6.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmi9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmmib10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr12.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr17.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr6.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmr9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsl10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsl12.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsl8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsl9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsltt10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmss10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmss12.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmss17.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmss8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmss9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssbx10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssdc10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssi10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssi12.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssi17.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssi8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssi9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssq8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmssqi8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy6.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmsy9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtcsc10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtex10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtex8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtex9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmti10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmti12.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmti7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmti8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmti9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtt10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtt12.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtt8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmtt9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmu10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cm/cmvtt10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmbsy5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmbsy6.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmbsy7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmbsy8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmbsy9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmcsc8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmcsc9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmex7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmex8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmex9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmmib5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmmib6.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmmib7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmmib8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cmextra/cmmib9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic/wncyb10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic/wncyi10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic/wncyr10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic/wncysc10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/cyrillic/wncyss10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/euex10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/euex7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/euex8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/euex9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufb10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufb5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufb7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufm10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufm5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eufm7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurb10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurb5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurb7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurm10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurm5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eurm7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusb10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusb5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusb7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusm10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusm5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/euler/eusm7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy6.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasy9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lasyb10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lcircle1.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lcirclew.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lcmss8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lcmssb8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/lcmssi8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/line10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/latxfont/linew10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam6.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msam9.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm10.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm5.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm6.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm7.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm8.afm
%{_datadir}/texmf-dist/fonts/afm/public/amsfonts/symbols/msbm9.afm
%{_datadir}/texmf-dist/fonts/map/dvips/amsfonts/cm.map
%{_datadir}/texmf-dist/fonts/map/dvips/amsfonts/cmextra.map
%{_datadir}/texmf-dist/fonts/map/dvips/amsfonts/cyrillic.map
%{_datadir}/texmf-dist/fonts/map/dvips/amsfonts/euler.map
%{_datadir}/texmf-dist/fonts/map/dvips/amsfonts/latxfont.map
%{_datadir}/texmf-dist/fonts/map/dvips/amsfonts/symbols.map
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmbsy5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmbsy6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmbsy7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmbsy8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmbsy9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmcsc8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmcsc9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmex7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmex8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmex9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmmib5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmmib6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmmib7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmmib8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cmextra/cmmib9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrcsc.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrfont.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrilu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrital.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrmax.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrpunc.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrspl.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrspu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/cyrti.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/serb.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/serbspu.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyb9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyi9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyr9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncysc10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyss10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyss8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/cyrillic/wncyss9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/dummy/dummy.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/amsya.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/amsyb.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/asymbols.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/bsymbols.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msam9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm5.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm6.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm7.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm8.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/msbm9.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/xbbase.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/xbbold.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/amsfonts/symbols/xbcaps.mf
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmbsy9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmcsc8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmcsc9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmex9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cmextra/cmmib9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyb9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyi9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyr9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncysc10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyss10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyss8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/cyrillic/wncyss9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/dummy/dummy.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/euex10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/euex7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/euex8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/euex9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufb9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eufm9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurb9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eurm9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusb9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/euler/eusm9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msam9.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm5.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm6.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm7.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm8.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/amsfonts/symbols/msbm9.tfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmb10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmb10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbsy10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbsy10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx12.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx6.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbx9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxsl10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxsl10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxti10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmbxti10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmcsc10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmcsc10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmdunh10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmdunh10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmex10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmff10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmff10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfi10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfi10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfib8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmfib8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cminch.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cminch.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmitt10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmitt10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi12.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi6.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmi9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmmib10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr12.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr17.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl12.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsl9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsltt10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsltt10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss12.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss17.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss17.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmss9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssbx10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssbx10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssdc10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssdc10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi12.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi17.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi17.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssi9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssq8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssq8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssqi8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmssqi8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtcsc10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtcsc10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtex9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti12.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmti9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt12.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt12.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmtt9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmu10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmu10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmvtt10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cm/cmvtt10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy6.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmbsy9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmcsc9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmex9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib6.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cmextra/cmmib9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyb10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyb10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyi10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyi10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyr10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyr10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncysc10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncysc10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyss10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/cyrillic/wncyss10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/euex9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufb7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eufm7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurb7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eurm7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusb7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/euler/eusm7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy6.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasy9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasyb10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lasyb10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcircle1.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcircle1.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcirclew.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcirclew.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmss8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmss8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssb8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssb8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssi8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/lcmssi8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/line10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/line10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/linew10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/latxfont/linew10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam6.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msam9.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm5.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm5.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm6.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm6.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm7.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm7.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm8.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm8.pfm
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm9.pfb
%{_datadir}/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm9.pfm
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/amsfndoc.cyr
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/amsfndoc.def
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/amsfndoc.fnt
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/amsfndoc.ins
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/amsfndoc.tex
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/amsfonts.bug
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/amsfonts.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/amsfonts.faq
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/amsfonts.ins
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/amssymb.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/cmmib57.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/eufrak.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/euscript.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsfonts/manifest.txt
%{_datadir}/texmf-dist/tex/latex/amsfonts/amsfonts.sty
%{_datadir}/texmf-dist/tex/latex/amsfonts/amssymb.sty
%{_datadir}/texmf-dist/tex/latex/amsfonts/cmmib57.sty
%{_datadir}/texmf-dist/tex/latex/amsfonts/eucal.sty
%{_datadir}/texmf-dist/tex/latex/amsfonts/eufrak.sty
%{_datadir}/texmf-dist/tex/latex/amsfonts/euscript.sty
%{_datadir}/texmf-dist/tex/latex/amsfonts/ueuex.fd
%{_datadir}/texmf-dist/tex/latex/amsfonts/ueuf.fd
%{_datadir}/texmf-dist/tex/latex/amsfonts/ueur.fd
%{_datadir}/texmf-dist/tex/latex/amsfonts/ueus.fd
%{_datadir}/texmf-dist/tex/latex/amsfonts/umsa.fd
%{_datadir}/texmf-dist/tex/latex/amsfonts/umsb.fd
%{_datadir}/texmf-dist/tex/plain/amsfonts/amssym.def
%{_datadir}/texmf-dist/tex/plain/amsfonts/amssym.tex
%{_datadir}/texmf-dist/tex/plain/amsfonts/cyracc.def
