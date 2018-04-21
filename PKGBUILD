# Script generated with Bloom
pkgdesc="ROS - The roseus_mongo package"


pkgname='ros-kinetic-roseus-mongo'
pkgver='1.6.3_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-mongodb-store'
'ros-kinetic-mongodb-store-msgs'
'ros-kinetic-roseus'
'ros-kinetic-rostest'
)

depends=('ros-kinetic-mongodb-store'
'ros-kinetic-mongodb-store-msgs'
'ros-kinetic-roseus'
)

conflicts=()
replaces=()

_dir=roseus_mongo
source=()
md5sums=()

prepare() {
    cp -R $startdir/roseus_mongo $srcdir/roseus_mongo
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

