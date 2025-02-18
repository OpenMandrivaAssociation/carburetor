Name:           carburetor 
Version:        5.0.0
Release:        1
Summary:        Graphical settings app for tractor in GTK

License:        GPL-3.0-or-later
URL:            https://framagit.org/tractor/carburetor/
Source0:        https://framagit.org/tractor/carburetor/-/archive/%{version}/carburetor-%{version}.tar.bz2

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

Requires:  gtk4
Requires:  python
Requires:  python-gobject3
Requires:  python-gi
Requires:  python-pycountry
Requires:  libadwaita-common
Requires:  tractor
Requires:  dconf
Requires:  tor
Recommends:  %{_lib}event2.1_7

%description
Experience seamless anonymous browsing with Carburetor - your privacy shield across devices. Built for GNU/Linux with GNOME integration and powered by Tor network.
Key Features:
📱 Cross-Platform Privacy: Works seamlessly on phones and desktops
🛡️ Tor Network Integration: Automatic encryption and IP masking
🎯 GNOME-First Design: Native look and feel for GTK environments
🚀 One-Click Security: Connect to Tor with a single button
🔧 Smart Configuration: Automatic optimal setup with manual override
📦 Distro-Ready: Available in major package repositories

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
