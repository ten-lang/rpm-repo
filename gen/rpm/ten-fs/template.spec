Name:           ten-fs
Version:        ${VER}
Release:        ${REL}
Summary:        Filesystem access for Ten.

License:        MIT
URL:            https://github.com/ten-lang/ten-fs
Source0:        https://github.com/ten-lang/ten-fs/archive/v${VER}.tar.gz
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
mkdir -p %{buildroot}/%{_libdir}/ten/
cp fs.so %{buildroot}/%{_libdir}/ten/


%files
%license LICENSE
%{_libdir}/ten/

%changelog
${LOG}
