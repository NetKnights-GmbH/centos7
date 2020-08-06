#Makefile variable OS
OS = ${shell rpm -q --queryformat '%{VERSION}' centos-release | cut -c1 }

info:
	@echo "buildrpm          - build a new RPM from a GitHub tag"
	@echo "buildradius       - build a new RPM for the radius plugin"
	@echo "buildselinux      - build a new RPM with Selinux Policy for privacyidea base on centos"
	@echo "signrpm           - sign all RPMs"
	@echo "fill-devel-repo   - put the newly built packages into the local DEVEL repo"
	@echo "fill-release-repo - put the newly built packages into the local release repo"
	@echo "make-repo         - fetch existing repo and build a new local repository with new packages"
	@echo "push-repo         - push the devel and productive repo to lancelot"
	@echo "Info about the running OS level of the centos machine:" $(OS)

buildrpm:
ifndef VERSION
	$(eval VERSION := $(shell curl --silent https://api.github.com/repos/privacyidea/privacyidea/tags | head | grep -Po '"name": "v?\K.*?(?=")' ))
	@echo "Warning: VERSION not set. Using the latest tag from GitHub: $(VERSION)"
endif
	PI_VERSION=${VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea.spec
	PI_VERSION=${VERSION} rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-server.spec

buildradius:
ifndef VERSION
	$(eval VERSION := $(shell curl --silent https://api.github.com/repos/privacyidea/FreeRADIUS/tags | head | grep -Po '"name": "v?\K.*?(?=")' ))
	@echo "Warning: VERSION not set. Using the latest tag from GitHub: $(VERSION)"
endif
	PI_VERSION=$(VERSION) rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-radius.spec

buildselinux:
	rpmbuild --define "_topdir `pwd`" -ba SPECS/privacyidea-selinux.spec

signrpm: buildrpm
	find RPMS/ -name *.rpm -exec 'rpmsign' '--addsign' '{}' ';'

fill-release-repo: signrpm
	mkdir -p repository/centos/$(OS)/
	cp -r RPMS/* repository/centos/$(OS)/

fill-devel-repo: signrpm
	mkdir -p repository/centos-devel/$(OS)/
	cp -r RPMS/* repository/centos-devel/$(OS)/

make-repo:
	# Fetch old packages
	(cd repository; rsync -vr root@lancelot:/srv/www/rpmrepo/ .)
	(cd repository/centos/$(OS)/x86_64/; createrepo .)
	(cd repository/centos/$(OS)/noarch/; createrepo .)
	(cd repository/centos-devel/$(OS)/x86_64/; createrepo .)
	(cd repository/centos-devel/$(OS)/noarch/; createrepo .)

push-repo:
	(cd repository;	rsync -vr centos root@lancelot:/srv/www/rpmrepo/)
	(cd repository;	rsync -vr centos-devel root@lancelot:/srv/www/rpmrepo/)

clean:
	rm -fr repository
	rm -fr BUILD/*
	rm -fr RPMS/*
	rm -fr SRPMS/*

