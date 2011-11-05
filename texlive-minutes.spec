# revision 16350
# category Package
# catalog-ctan /macros/latex/contrib/minutes
# catalog-date 2009-12-05 12:31:44 +0100
# catalog-license other-free
# catalog-version 1.8d
Name:		texlive-minutes
Version:	1.8d
Release:	1
Summary:	Typeset the minutes of meetings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/minutes
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minutes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minutes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minutes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Supports the creation of a collection of minutes. Features
include: - Support of tasks (who, schedule, what, time of
finishing; - possibility of creating a list of open tasks; -
inclusion of open tasks from other minutes; - Support for
attachments; - Support of schedule dates (in planning: support
for the calendar package); - Different versions ('secret
parts'); and - Macros for votes and decisions (list of
decisions). Support for minutes in a variety of languages is
available.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/minutes/minutes.sty
%doc %{_texmfdistdir}/doc/latex/minutes/MinStyGd.tex
%doc %{_texmfdistdir}/doc/latex/minutes/Overview.tex
%doc %{_texmfdistdir}/doc/latex/minutes/Protokol.tex
%doc %{_texmfdistdir}/doc/latex/minutes/README
%doc %{_texmfdistdir}/doc/latex/minutes/Sample.tex
%doc %{_texmfdistdir}/doc/latex/minutes/SampleDE.tex
%doc %{_texmfdistdir}/doc/latex/minutes/SampleEN.tex
%doc %{_texmfdistdir}/doc/latex/minutes/SampleNL.tex
%doc %{_texmfdistdir}/doc/latex/minutes/minutes.pdf
#- source
%doc %{_texmfdistdir}/source/latex/minutes/minutes.dtx
%doc %{_texmfdistdir}/source/latex/minutes/minutes.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
