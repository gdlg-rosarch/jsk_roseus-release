# Script generated with Bloom
pkgdesc="ROS - EusLisp client for ROs Robot Operating System."
url='http://pr.willowgarage.com/wiki/roseus'

pkgname='ros-kinetic-roseus'
pkgver='1.6.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('coreutils'
'ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-actionlib-tutorials'
'ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-euslisp'
'ros-kinetic-geneus'
'ros-kinetic-geometry-msgs'
'ros-kinetic-jskeus'
'ros-kinetic-message-generation'
'ros-kinetic-mk'
'ros-kinetic-rosbash'
'ros-kinetic-rosbuild'
'ros-kinetic-roscpp'
'ros-kinetic-roslang'
'ros-kinetic-rosmsg'
'ros-kinetic-rosnode'
'ros-kinetic-rospack'
'ros-kinetic-rostest'
'ros-kinetic-rostopic'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
'ros-kinetic-tf2-ros'
'ros-kinetic-visualization-msgs'
'xorg-server-xvfb'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-actionlib-tutorials'
'ros-kinetic-dynamic-reconfigure'
'ros-kinetic-euslisp'
'ros-kinetic-geneus'
'ros-kinetic-geometry-msgs'
'ros-kinetic-jskeus'
'ros-kinetic-message-runtime'
'ros-kinetic-rosbash'
'ros-kinetic-roscpp'
'ros-kinetic-roslang'
'ros-kinetic-rosmsg'
'ros-kinetic-rosnode'
'ros-kinetic-rospack'
'ros-kinetic-rostest'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-tf'
'ros-kinetic-tf2-ros'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=roseus
source=()
md5sums=()

prepare() {
    cp -R $startdir/roseus $srcdir/roseus
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

