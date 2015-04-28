#roseus_smach
- - -

This package includes euslisp imprementation of state machine and [smach](http://wiki.ros.org/smach).

## requirements

- [roseus](http://wiki.ros.org/roseus)
- [smach](http://wiki.ros.org/smach)
- [smach_viewer](http://wiki.ros.org/smach_viewer) (optional for visualization)

## sample

Sample codes are available on `sample` directory.

- `sample/state-machine-ros-sample.l`
  - simple state machine
  ![](http://bl.ocks.org/furushchev/raw/9b1ed0aa57b47537cd2d/smach-simple.gif)
  ```lisp
  roseus state-machine-ros-sample.l
  (smach-exec-simple)
  ```
  - nested state machine
  ![](http://bl.ocks.org/furushchev/raw/9b1ed0aa57b47537cd2d/smach-nested.gif)
  ```lisp
  roseus state-machine-ros-sample.l
  (smach-exec-nested)
  ```
  - state machine with userdata
  ![](http://bl.ocks.org/furushchev/raw/9b1ed0aa57b47537cd2d/smach-userdata.gif)
  ```lisp
  roseus state-machine-ros-sample.l
  (smach-exec-userdata)
  ```
- `sample/parallel-state-machine-sample.l`

  - state machine with parallel action execution
  ![](http://bl.ocks.org/furushchev/raw/9b1ed0aa57b47537cd2d/smach-parallel.gif)
  ```lisp
  roseus parallel-state-machine-sample.l
  (demo)
  ```
  
  
