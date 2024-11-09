%define oname Alpaca

Name:           alpaca
Version:        2.7.0
Release:        1
Summary:        An Ollama client made with GTK4 and Adwaita 
License:        GPL-3.0
Group:          Networking/Instant Messenger
URL:            https://github.com/Jeffser/Alpaca/
Source0:        https://github.com/Jeffser/Alpaca/archive/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  appstream-util
BuildRequires:  meson
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(gtksourceview-5)

Requires:  gtk4
Requires:  vtk3
Requires:  python3
python-pypdf
python-pytube
python-html2text

Requires: ollama

%description
Alpaca is an Ollama client where you can manage and chat with multiple models, 
Alpaca provides an easy and begginer friendly way of interacting with local AI, everything is open source and powered by Ollama.

%prep
%autosetup -p1 -a1

%build
%meson
%meson_build

%install
%meson_install

%files
