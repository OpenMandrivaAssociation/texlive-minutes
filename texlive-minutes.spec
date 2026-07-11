%global tl_name minutes
%global tl_revision 42186

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8f
Release:	%{tl_revision}.1
Summary:	Typeset the minutes of meetings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/minutes
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minutes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minutes.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/minutes.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Supports the creation of a collection of minutes. Features include:
Support of tasks (who, schedule, what, time of finishing; possibility of
creating a list of open tasks; inclusion of open tasks from other
minutes; Support for attachments; Support of schedule dates (in
planning: support for the calendar package); Different versions ('secret
parts'); and Macros for votes and decisions (list of decisions). Support
for minutes in German, Dutch and English is provided.

