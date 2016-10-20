Name:           ros-kinetic-roseus
Version:        1.6.0
Release:        0%{?dist}
Summary:        ROS roseus package

Group:          Development/Libraries
License:        BSD
URL:            http://pr.willowgarage.com/wiki/roseus
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib
Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-actionlib-tutorials
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-euslisp
Requires:       ros-kinetic-geneus
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-jskeus
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-rosbash
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslang
Requires:       ros-kinetic-rosmsg
Requires:       ros-kinetic-rosnode
Requires:       ros-kinetic-rospack
Requires:       ros-kinetic-rostest
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-tf2-ros
Requires:       ros-kinetic-visualization-msgs
BuildRequires:  coreutils
BuildRequires:  ros-kinetic-actionlib
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-actionlib-tutorials
BuildRequires:  ros-kinetic-angles
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-euslisp
BuildRequires:  ros-kinetic-geneus
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-jskeus
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-mk
BuildRequires:  ros-kinetic-rosbash
BuildRequires:  ros-kinetic-rosbuild
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslang
BuildRequires:  ros-kinetic-rosmsg
BuildRequires:  ros-kinetic-rosnode
BuildRequires:  ros-kinetic-rospack
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rostopic
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-tf2-ros
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  xorg-x11-server-Xvfb

%description
EusLisp client for ROs Robot Operating System.

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
* Fri Oct 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.6.0-0
- Autogenerated by Bloom

