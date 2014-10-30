rpm-kibana
==========

An RPM spec file build an RPM for [Kibana](https://github.com/elasticsearch/kibana)

NOTE: This spec file will build an rpm that installs kibana to /opt/kibana. 

To Build:
```
sudo yum -y install rpmdevtools && rpmdev-setuptree

PKGNAME="kibana"
wget https://raw.github.com/mwhahaha/rpm-${PKGNAME}/master/${PKGNAME}.spec -O ~/rpmbuild/SPECS/${PKGNAME}.spec
spectool -R -g ~/rpmbuild/SPECS/${PKGNAME}.spec
rpmbuild -ba ~/rpmbuild/SPECS/${PKGNAME}.spec
```

