Build environment for building CentOS packages

make will fetch the version from GitHub.

E.g. You can build a devel repo like this:

    VERSION=2.23 make clean buildrpm fill-devel-repo make-repo
