Build environment for building CentOS packages

Works for CentOS7 and CentOS8.

Make will fetch the version from GitHub.

E.g. You can build a devel repo like this:

    VERSION=2.23 make clean buildrpm fill-devel-repo make-repo
