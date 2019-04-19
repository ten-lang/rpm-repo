Name:           libtml
Version:        ${VER}
Release:        ${REL}
Summary:        The Ten Module Loader library.

License:        MIT
URL:            https://github.com/ten-lang/libtml
Source0:        https://github.com/ten-lang/libtml/archive/v${VER}.tar.gz
BuildRequires:  make gcc binutils tar libten


# debuginfo.sh isn't good at detecting debug info instatic libraries.
%global debug_package %{nil}

%description


%prep
%autosetup

%build
make
make PROFILE=debug


%install
mkdir -p %{buildroot}/%{_libdir}/
cp libtml.a %{buildroot}/%{_libdir}/


%files
%license LICENSE
%{_libdir}/libtml.a

%changelog
${LOG}
