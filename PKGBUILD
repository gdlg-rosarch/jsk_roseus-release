# Script generated with Bloom
pkgdesc="ROS - roseus_smach * Euslisp state machine class. it will be moved. * Message publisher for visualizing current state by smach_viewer. * Simple pickle dump script for debugging state machine. * Execute state machine as a action server."
url='http://ros.org/wiki/roseus_smach'

pkgname='ros-kinetic-roseus-smach'
pkgver='1.6.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-tutorials'
'ros-kinetic-catkin'
'ros-kinetic-message-generation'
'ros-kinetic-roseus'
'ros-kinetic-rostest'
'ros-kinetic-smach'
'ros-kinetic-smach-msgs'
'ros-kinetic-smach-ros'
'ros-kinetic-std-msgs'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-tutorials'
'ros-kinetic-euslisp'
'ros-kinetic-message-runtime'
'ros-kinetic-roseus'
'ros-kinetic-rostest'
'ros-kinetic-smach'
'ros-kinetic-smach-msgs'
'ros-kinetic-smach-ros'
'ros-kinetic-std-msgs'
)

conflicts=()
replaces=()

_dir=roseus_smach
source=()
md5sums=()

prepare() {
    cp -R $startdir/roseus_smach $srcdir/roseus_smach
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

