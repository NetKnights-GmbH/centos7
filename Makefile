ifndef VERSION
        $(error VERSION not set. Set VERSION to build like VERSION=v2.19.1)
endif
PI_VERSION=${VERSION}

info:
	@echo "buildrpm"
	@echo "repo"
	@echo "clean"

buildrpm:
	PI_VERSION=${PI_VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea.spec
	PI_VERSION=${PI_VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-server.spec
	PI_VERSION=${PI_VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-radius.spec

repo:
	mkdir -p repository/centos/7/
	cp -r RPMS/* repository/centos/7/
	# Fetch old packages
	(cd repository; rsync -vr root@lancelot:/srv/www/rpmrepo/ .)
	(cd repository/centos/7/x86_64/; createrepo .)
	(cd repository/centos/7/noarch/; createrepo .)
	(cd repository;	rsync -vr centos root@lancelot:/srv/www/rpmrepo/)

clean:
	rm -fr repository
	rm -fr BUILD/*
	rm -fr RPMS/*
	rm -fr SRPMS/*
