Build environment for building CentOS 7 package

make will fetch this version from the python package index.

E.g. You can build a devel repo like this:

    VERSION=2.23 make clean buildrpm fill-devel-repo make-repo
