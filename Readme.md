# Ten RPM Repository
This is used as an RPM repository for hosting pre-built binary
distributions of Ten's projects.  The `ten-lang.repo` file
should be copied into your `/etc/yum.repos.d/` directory to
enable installations.  This can be done easily with:

    sudo wget -O /etc/yum.repos.d/ten-lang.repo https://raw.githubusercontent.com/ten-lang/rpm-repo/master/ten-lang.repo
    sudo yum update

