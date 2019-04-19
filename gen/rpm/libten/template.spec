Name:           libten
Version:        ${VER}
Release:        ${REL}
Summary:        The Ten programming language implementation library.

License:        MIT
URL:            https://github.com/ten-lang/libten
Source0:        https://github.com/ten-lang/libten/archive/v${VER}.tar.gz
BuildRequires:  make gcc binutils tar

%description


%prep
%autosetup


%build
make
make PROFILE=debug


%install
mkdir -p %{buildroot}/%{_libdir}/
cp libten.so %{buildroot}/%{_libdir}/
cp libten.a %{buildroot}/%{_libdir}/
cp libten-debug.so %{buildroot}/%{_libdir}/
cp libten-debug.a %{buildroot}/%{_libdir}/


%files
%license LICENSE
%{_libdir}/libten.so
%{_libdir}/libten.a
%{_libdir}/libten-debug.so
%{_libdir}/libten-debug.a



%changelog
${LOG}
