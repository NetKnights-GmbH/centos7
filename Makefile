# Makefile for building CentOS RPMs

ifndef VERSION
  error_text = "VERSION not set. Set VERSION to build like VERSION=2.19.1!\
                This is a github tag (without leading 'v')!"
  $(error $(error_text))
endif
PI_VERSION=${VERSION}

info:
	@echo "buildrpm          - build a new RPM from python package index"
	@echo "signrpm           - sign the RPMs"
	@echo "fill-devel-repo   - put the newly built packages into the local DEVEL repo"
	@echo "fill-release-repo - put the newly built packages into the local release repo"
	@echo "make-repo         - fetch existing repo and build a new local repository with new packages"
	@echo "push-repo         - push the devel and productive repo to lancelot"

buildrpm:
	PI_VERSION=${PI_VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea.spec
	PI_VERSION=${PI_VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-server.spec

buildradius:
	PI_VERSION=${PI_VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-radius.spec

buildoracle:
	rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-cx-oracle.spec

signrpm:
	find RPMS/ -name *.rpm -exec 'rpmsign' '--addsign' '{}' ';'

fill-release-repo: signrpm
	mkdir -p repository/centos/7/
	cp -r RPMS/* repository/centos/7/

fill-devel-repo: signrpm
	mkdir -p repository/centos-devel/7/
	cp -r RPMS/* repository/centos-devel/7/

make-repo:
	mkdir -p repository
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
