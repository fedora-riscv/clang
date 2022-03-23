%global toolchain clang

Name: test
Version: 1
Release: 1
Summary: Test package for checking that RPM packages using -fopenmp build correctly
License: MIT

BuildRequires: clang
BuildRequires: libomp

%description
clang was adding RUNPATH to binaries that use OpenMP, and since RUNPATH
is prohibited in Fedora builds, this was causing packages using clang
and OpenMP to fail to build.

%build
echo 'int main(int argc, char **argv) { return 0; }' | %{build_cc} ${CFLAGS} -x c -fopenmp -c - -o main

%check
./main

%install
install -D main %{buildroot}%{_bindir}

%files
%{_bindir}/main
