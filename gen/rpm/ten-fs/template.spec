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

%define _installpath %{_libdir}/ten/fs/%(echo ${VER} | tr . -)/

%description


%prep
%autosetup

%build
make


%install
mkdir -p %{buildroot}/%{_installpath}/
cp fs.so %{buildroot}/%{_installpath}/


%files
%license LICENSE
%{_installpath}/fs.so

%changelog
${LOG}
