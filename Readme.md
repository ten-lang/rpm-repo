# Ten RPM Repository
This is used as an RPM repository for hosting pre-built binary
distributions of Ten's projects.  To add it to your system,
and enable installation of Ten's binaries, try the following:

    wget -O - https://git.io/fjOZI | sudo sh

If this doesn't work, with an error indicating that the URL
isn't valid; then use the full version:

    wget -O - https://raw.githubusercontent.com/ten-lang/rpm-repo/master/install.sh | sudo sh
