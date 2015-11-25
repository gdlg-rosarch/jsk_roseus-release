Name:           ros-indigo-roseus-mongo
Version:        1.4.1
Release:        0%{?dist}
Summary:        ROS roseus_mongo package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-mongodb-store
Requires:       ros-indigo-mongodb-store-msgs
Requires:       ros-indigo-roseus
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-mongodb-store
BuildRequires:  ros-indigo-mongodb-store-msgs
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-rostest

%description
The roseus_mongo package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Nov 25 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 1.4.1-0
- Autogenerated by Bloom

* Tue Nov 03 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 1.4.0-0
- Autogenerated by Bloom

* Tue Sep 15 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 1.3.9-0
- Autogenerated by Bloom

* Sat Sep 12 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 1.3.8-0
- Autogenerated by Bloom

* Tue Aug 18 2015 Yuki Furuta <furushchev@jsk.imi.i.u-tokyo.ac.jp> - 1.3.7-0
- Autogenerated by Bloom

