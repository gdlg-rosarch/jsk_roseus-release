Name:           ros-kinetic-jsk-roseus
Version:        1.6.0
Release:        3%{?dist}
Summary:        ROS jsk_roseus package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_roseus
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-euslisp
Requires:       ros-kinetic-geneus
Requires:       ros-kinetic-roseus
BuildRequires:  ros-kinetic-catkin

%description
Metapackage that contains roseus package for jsk-ros-pkg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Mar 11 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.6.0-3
- Autogenerated by Bloom

* Sat Mar 11 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.6.0-1
- Autogenerated by Bloom

* Fri Oct 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.6.0-0
- Autogenerated by Bloom

