Name:           ten
Version:        ${VER}
Release:        ${REL}
Summary:        The Ten programming language CLI.

License:        MIT
URL:            https://github.com/ten-lang/ten
Source0:        https://github.com/ten-lang/ten/archive/v${VER}.tar.gz
BuildRequires:  make gcc binutils tar libten libtml readline
Requires:       libten >= ${VER} libtml readline

%description


%prep
%autosetup


%build
make
make PROFILE=debug


%install
mkdir -p %{buildroot}/%{_bindir}/
cp ten %{buildroot}/%{_bindir}/
cp ten-debug %{buildroot}/%{_bindir}/


%files
%license LICENSE
%{_bindir}/ten
%{_bindir}/ten-debug



%changelog
${LOG}
