Name:           ros-hydro-geneus
Version:        1.1.29
Release:        0%{?dist}
Summary:        ROS geneus package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-euslisp
Requires:       ros-hydro-genmsg
Requires:       ros-hydro-rospy
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-euslisp
BuildRequires:  ros-hydro-genmsg
BuildRequires:  ros-hydro-rospy

%description
EusLisp ROS message and service generators

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

