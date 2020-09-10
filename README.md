Build environment for building CentOS packages

make will fetch the version from GitHub.

E.g. You can build a devel repo like this:

    VERSION=2.23 make clean buildrpm fill-devel-repo make-repo

If you want to build privacyidea-selinux you need to adapt the privacyidea-selinux.spec file and run:

    make clean buildselinux fill-release-repo make-repo push-repo

