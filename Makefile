PI_VERSION=2.10dev5
info:
	@echo "buildrpm"
	@echo "repo"
	@echo "clean"

buildrpm:
	PI_VERSION=${PI_VERSION} rpmbuild -ba SPECS/privacyidea.spec
	PI_VERSION=${PI_VERSION} rpmbuild -ba SPECS/privacyidea-server.spec

repo:
	mkdir -p repository/centos/7/
	cp -r RPMS/* repository/centos/7/
	(cd repository/centos/7/noarch/; createrepo .)
	tar -zcf repository.tgz repository

clean:
	rm -fr repository
	rm -fr BUILD/*
	rm -fr RPMS/*
	rm -fr SRPMS/*
