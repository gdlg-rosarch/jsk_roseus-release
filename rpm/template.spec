Name:           ros-hydro-roseus-tutorials
Version:        1.1.31
Release:        0%{?dist}
Summary:        ROS roseus_tutorials package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roseus_tutorials
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-ar-track-alvar
Requires:       ros-hydro-image-proc
Requires:       ros-hydro-image-view2
Requires:       ros-hydro-uvc-camera
Requires:       ros-hydro-visualization-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-roseus

%description
roseus_tutorials

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
* Fri Jan 23 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.31-0
- Autogenerated by Bloom

