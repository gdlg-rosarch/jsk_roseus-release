Name:           ros-indigo-roseus-smach
Version:        1.1.30
Release:        0%{?dist}
Summary:        ROS roseus_smach package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roseus_smach
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-euslisp
Requires:       ros-indigo-roseus
Requires:       ros-indigo-smach
Requires:       ros-indigo-smach-msgs
Requires:       ros-indigo-smach-ros
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-euslisp
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-smach
BuildRequires:  ros-indigo-smach-msgs
BuildRequires:  ros-indigo-smach-ros

%description
roseus_smach * Euslisp state machine class. it will be moved. * Message
publisher for visualizing current state by smach_viewer. * Simple pickle dump
script for debugging state machine. * Execute state machine as a action server.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jan 14 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.30-0
- Autogenerated by Bloom

* Sat Dec 27 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.29-0
- Autogenerated by Bloom

* Mon Dec 22 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.27-1
- Autogenerated by Bloom

