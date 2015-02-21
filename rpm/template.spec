Name:           ros-jade-roseus
Version:        1.2.6
Release:        0%{?dist}
Summary:        ROS roseus package

Group:          Development/Libraries
License:        BSD
URL:            http://pr.willowgarage.com/wiki/roseus
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-actionlib-msgs
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-euslisp
Requires:       ros-jade-geneus
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-jskeus
Requires:       ros-jade-message-runtime
Requires:       ros-jade-rosbash
Requires:       ros-jade-roscpp
Requires:       ros-jade-roslang
Requires:       ros-jade-rosmsg
Requires:       ros-jade-rosnode
Requires:       ros-jade-rospack
Requires:       ros-jade-rostest
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
Requires:       ros-jade-tf
Requires:       ros-jade-tf2-ros
Requires:       ros-jade-visualization-msgs
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-actionlib-msgs
BuildRequires:  ros-jade-angles
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-euslisp
BuildRequires:  ros-jade-geneus
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-jskeus
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-mk
BuildRequires:  ros-jade-rosbash
BuildRequires:  ros-jade-rosbuild
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-roslang
BuildRequires:  ros-jade-rosmsg
BuildRequires:  ros-jade-rosnode
BuildRequires:  ros-jade-rospack
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-rostopic
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-tf2-ros
BuildRequires:  ros-jade-visualization-msgs

%description
EusLisp client for ROs Robot Operating System.

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
* Sat Feb 21 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.6-0
- Autogenerated by Bloom

* Fri Feb 13 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.5-0
- Autogenerated by Bloom

* Thu Feb 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.4-0
- Autogenerated by Bloom

* Tue Feb 10 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.3-0
- Autogenerated by Bloom

