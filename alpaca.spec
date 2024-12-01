%undefine _debugsource_packages
%define oname Alpaca

Name:           alpaca
Version:        2.9.0
Release:        1
Summary:        An Ollama client made with GTK4 and Adwaita 
License:        GPL-3.0
Group:          Tools
URL:            https://jeffser.com/alpaca/
Source0:        https://github.com/Jeffser/Alpaca/archive/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  appstream
BuildRequires:  meson
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(gtksourceview-5)

Requires:  numactl
Requires:  gtk4
Requires:  vte3
Requires:  %{_lib}vte-gir3.91
Requires:  libadwaita-common
Requires:  python3
Requires:  python-pypdf
Requires:  python-pytube
Requires:  python-html2text
Requires:  python-requests
Requires:  python-pillow
Requires:  python-youtube-transcript-api
Requires:  python-gobject3
Requires:  python-gi

Requires: ollama

%description
Alpaca is an Ollama client where you can manage and chat with multiple models, 
Alpaca provides an easy and begginer friendly way of interacting with local AI, everything is open source and powered by Ollama.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/alpaca
%{_bindir}/alpaca_search_provider
%{_datadir}/Alpaca/
%{_datadir}/applications/com.jeffser.Alpaca.desktop
%{_datadir}/applications/com.jeffser.Alpaca.SearchProvider.desktop
%{_datadir}/dbus-1/services/com.jeffser.Alpaca.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/com.jeffser.Alpaca.search-provider.ini
%{_datadir}/glib-2.0/schemas/com.jeffser.Alpaca.gschema.xml
%{_datadir}/metainfo/com.jeffser.Alpaca.metainfo.xml
%{_iconsdir}/hicolor/*x*/apps/com.jeffser.Alpaca.png
%{_iconsdir}/hicolor/scalable/apps/com.jeffser.Alpaca.svg
%{_iconsdir}/hicolor/symbolic/apps/com.jeffser.Alpaca-symbolic.svg
