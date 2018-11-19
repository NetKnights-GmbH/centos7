ifndef VERSION
        $(error VERSION not set. Set VERSION to build like VERSION=2.19.1)
	$(error This is a VERSION number in pypi repository, no github tag!)
endif
PI_VERSION=${VERSION}

info:
	@echo "buildrpm          - build a new RPM from python package index"
	@echo "fill-devel-repo   - put the newly built packages into the local DEVEL repo"
	@echo "fill-release-repo - put the newly built packages into the local release repo"
	@echo "make-repo         - fetch existing repo and build a new local repository with new packages"
	@echo "push-repo         - push the devel and productive repo to lancelot"

buildrpm:
	PI_VERSION=${PI_VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea.spec
	PI_VERSION=${PI_VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-server.spec
	PI_VERSION=${PI_VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-radius.spec

buildoracle:
	rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-cx-oracle.spec 

fill-release-repo:
	mkdir -p repository/centos/7/
	cp -r RPMS/* repository/centos/7/

fill-devel-repo:
	mkdir -p repository/centos-devel/7/
	cp -r RPMS/* repository/centos-devel/7/

make-repo:
	# Fetch old packages
	(cd repository; rsync -vr root@lancelot:/srv/www/rpmrepo/ .)
	(cd repository/centos/7/x86_64/; createrepo .)
	(cd repository/centos/7/noarch/; createrepo .)
	(cd repository/centos-devel/7/x86_64/; createrepo .)
	(cd repository/centos-devel/7/noarch/; createrepo .)

push-repo:
	(cd repository;	rsync -vr centos root@lancelot:/srv/www/rpmrepo/)
	(cd repository;	rsync -vr centos-devel root@lancelot:/srv/www/rpmrepo/)

clean:
	rm -fr repository
	rm -fr BUILD/*
	rm -fr RPMS/*
	rm -fr SRPMS/*
