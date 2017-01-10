PI_VERSION=2.17
info:
	@echo "buildrpm"
	@echo "repo"
	@echo "clean"

buildrpm:
	PI_VERSION=${PI_VERSION} rpmbuild -ba SPECS/privacyidea.spec
	PI_VERSION=${PI_VERSION} rpmbuild -ba SPECS/privacyidea-server.spec
	PI_VERSION=${PI_VERSION} rpmbuild -ba SPECS/privacyidea-radius.spec

repo:
	mkdir -p repository/centos/7/
	cp -r RPMS/* repository/centos/7/
	(cd repository/centos/7/x86_64/; createrepo .)
	(cd repository/centos/7/noarch/; createrepo .)
	(cd repository;	rsync -vr centos root@lancelot:/srv/www/rpmrepo/)

clean:
	rm -fr repository
	rm -fr BUILD/*
	rm -fr RPMS/*
	rm -fr SRPMS/*
