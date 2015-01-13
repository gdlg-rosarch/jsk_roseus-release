Name:           ros-hydro-euslisp
Version:        1.1.30
Release:        0%{?dist}
Summary:        ROS euslisp package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/euslisp
Source0:        %{name}-%{version}.tar.gz

Requires:       derelict-postgresql-devel
Requires:       libX11-devel
Requires:       libXext-devel
Requires:       libjpeg-turbo-devel
Requires:       libpng-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       postgresql-devel
Requires:       ros-hydro-rostest
Requires:       xorg-x11-fonts-100dpi
BuildRequires:  derelict-postgresql-devel
BuildRequires:  git
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  postgresql-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-rosbuild
BuildRequires:  ros-hydro-rostest
BuildRequires:  xorg-x11-fonts-100dpi

%description
This packages contains humanoid robot modeling software based on EusLisp
language developed by researchers and students at JSK Robotics Laboratory at the
University of Tokyo, Japan.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
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
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
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

