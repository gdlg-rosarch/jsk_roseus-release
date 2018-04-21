# Script generated with Bloom
pkgdesc="ROS - roseus_tutorials"
url='http://ros.org/wiki/roseus_tutorials'

pkgname='ros-kinetic-roseus-tutorials'
pkgver='1.6.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-roseus'
'ros-kinetic-rostest'
)

depends=('ros-kinetic-ar-track-alvar'
'ros-kinetic-checkerboard-detector'
'ros-kinetic-image-proc'
'ros-kinetic-image-view2'
'ros-kinetic-jsk-recognition-msgs'
'ros-kinetic-opencv-apps'
'ros-kinetic-posedetection-msgs'
'ros-kinetic-pr2eus'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=roseus_tutorials
source=()
md5sums=()

prepare() {
    cp -R $startdir/roseus_tutorials $srcdir/roseus_tutorials
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

