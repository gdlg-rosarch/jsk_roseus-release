Name:           ros-hydro-jsk-roseus
Version:        1.2.1
Release:        0%{?dist}
Summary:        ROS jsk_roseus package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_roseus
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-euslisp
Requires:       ros-hydro-geneus
Requires:       ros-hydro-roseus
BuildRequires:  ros-hydro-catkin

%description
Metapackage that contains roseus package for jsk-ros-pkg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Jan 27 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.1-0
- Autogenerated by Bloom

* Mon Jan 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.32-0
- Autogenerated by Bloom

* Mon Jan 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.33-0
- Autogenerated by Bloom

* Mon Jan 26 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.0-0
- Autogenerated by Bloom

* Fri Jan 23 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.31-0
- Autogenerated by Bloom

* Wed Jan 14 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.30-0
- Autogenerated by Bloom

* Sat Dec 27 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.29-0
- Autogenerated by Bloom

* Mon Nov 10 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.26-0
- Autogenerated by Bloom

* Sat Oct 11 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.25-0
- Autogenerated by Bloom

* Wed Sep 24 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.24-0
- Autogenerated by Bloom

* Fri Sep 05 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.22-0
- Autogenerated by Bloom

