Name:           ros-hydro-roseus-msgs
Version:        1.1.30
Release:        1%{?dist}
Summary:        ROS roseus_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-geneus
BuildRequires:  ros-hydro-audio-common
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-control-msgs
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-geneus
BuildRequires:  ros-hydro-jsk-common
BuildRequires:  ros-hydro-jsk-interactive
BuildRequires:  ros-hydro-jsk-interactive-marker
BuildRequires:  ros-hydro-jsk-model-tools
BuildRequires:  ros-hydro-jsk-planning
BuildRequires:  ros-hydro-jsk-recognition
BuildRequires:  ros-hydro-jsk-rqt-plugins
BuildRequires:  ros-hydro-jsk-rviz-plugins
BuildRequires:  ros-hydro-move-base-msgs
BuildRequires:  ros-hydro-moveit-full-pr2
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-pr2-controllers-msgs
BuildRequires:  ros-hydro-pr2-description
BuildRequires:  ros-hydro-pr2-gazebo
BuildRequires:  ros-hydro-pr2-msgs
BuildRequires:  ros-hydro-pr2eus
BuildRequires:  ros-hydro-roseus
BuildRequires:  ros-hydro-rtmros-common
BuildRequires:  ros-hydro-rviz

%description
Special package that generates roseus msgs for all installed packages

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
* Tue Apr 28 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.30-1
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

