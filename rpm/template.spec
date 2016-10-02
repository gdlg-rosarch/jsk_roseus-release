Name:           ros-jade-jsk-roseus
Version:        1.6.0
Release:        0%{?dist}
Summary:        ROS jsk_roseus package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_roseus
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-euslisp
Requires:       ros-jade-geneus
Requires:       ros-jade-roseus
BuildRequires:  ros-jade-catkin

%description
Metapackage that contains roseus package for jsk-ros-pkg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Oct 02 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.6.0-0
- Autogenerated by Bloom

* Sat May 28 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.5.3-0
- Autogenerated by Bloom

* Fri Apr 22 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.5.1-0
- Autogenerated by Bloom

* Mon Mar 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.5.0-0
- Autogenerated by Bloom

* Wed Nov 25 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.4.1-0
- Autogenerated by Bloom

* Wed Nov 18 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.4.0-1
- Autogenerated by Bloom

* Tue Nov 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.4.0-0
- Autogenerated by Bloom

* Tue Sep 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.9-0
- Autogenerated by Bloom

* Sat Sep 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.8-0
- Autogenerated by Bloom

* Tue Aug 18 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.7-0
- Autogenerated by Bloom

* Fri Jun 19 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.6-0
- Autogenerated by Bloom

* Fri May 15 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.5-0
- Autogenerated by Bloom

* Sun May 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.4-0
- Autogenerated by Bloom

* Wed Apr 29 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.3-0
- Autogenerated by Bloom

* Tue Apr 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.2-3
- Autogenerated by Bloom

* Tue Apr 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.2-2
- Autogenerated by Bloom

* Tue Apr 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.2-1
- Autogenerated by Bloom

* Tue Apr 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.2-0
- Autogenerated by Bloom

* Sun Apr 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.1-1
- Autogenerated by Bloom

* Sun Apr 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.1-0
- Autogenerated by Bloom

* Fri Apr 24 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.3.0-0
- Autogenerated by Bloom

* Sun Feb 22 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.7-0
- Autogenerated by Bloom

* Sat Feb 21 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.6-0
- Autogenerated by Bloom

* Fri Feb 13 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.5-0
- Autogenerated by Bloom

* Thu Feb 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.4-0
- Autogenerated by Bloom

* Tue Feb 10 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.3-0
- Autogenerated by Bloom

