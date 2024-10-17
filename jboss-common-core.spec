%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             jboss-common-core
Version:          2.2.22
Release:          1.3
Summary:          JBoss Common Classes
Group:            Development/Java
License:          LGPLv2+ and ASL 1.1
URL:              https://www.jboss.org

# svn export http://anonsvn.jboss.org/repos/common/common-core/tags/2.2.22.GA/ jboss-common-core-2.2.22.GA
# tar cafJ jboss-common-core-2.2.22.GA.tar.xz jboss-common-core-2.2.22.GA
Source0:          %{name}-%{namedversion}.tar.xz
# The URLLister* family of classes was removed because the apache-slide:webdavlib is a dead project and the classes aren't used in JBoss AS 7 at all. 
Patch0:           %{name}-%{namedversion}-URLLister-removal.patch

BuildArch:        noarch

BuildRequires:    java-devel
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-plugin-cobertura
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-ejb-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    jboss-parent
BuildRequires:    junit
BuildRequires:    jboss-logging

%description
JBoss Common Core Utility classes

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

rm -rf projectSet.psf .settings/ .project .classpath

%build
# Some failed tests
# Failed tests: testJavaLangEditors(org.jboss.test.util.test.propertyeditor.PropertyEditorsUnitTestCase):
#   PropertyEditor: org.jboss.util.propertyeditor.BooleanEditor, getAsText() == expectedStringOutput ' expected:<null> but was:<null>
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Tue Jul 01 2014 Marek Goldmann <mgoldman@redhat.com> - 2.2.22-1
- Upstream release 2.2.22.GA, upgrade to xmvn

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.18-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.2.18-11
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2.18-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jul 20 2012 Marek Goldmann <mgoldman@redhat.com> 2.2.18-7
- Fixed BR

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 2.2.18-5
- Relocated jars to _javadir

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Marek Goldmann <mgoldman@redhat.com> 2.2.18-3
- Requires typo

* Sun Oct 02 2011 Marek Goldmann <mgoldman@redhat.com> 2.2.18-2
- Another license field fix

* Tue Sep 20 2011 Marek Goldmann <mgoldman@redhat.com> 2.2.18-1
- Upstream release 2.2.18
- License field fix

* Mon Aug 01 2011 Marek Goldmann <mgoldman@redhat.com> 2.2.17-1
- Initial packaging

