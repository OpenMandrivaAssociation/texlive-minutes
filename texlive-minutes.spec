Name:		texlive-minutes
Version:	42186
Release:	1
Summary:	Typeset the minutes of meetings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/minutes
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minutes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minutes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minutes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/minutes
%doc %{_texmfdistdir}/doc/latex/minutes
#- source
%doc %{_texmfdistdir}/source/latex/minutes

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
