# `turtlesim_circle`

This package sends `geometry_msgs.msg.Twist` type to `turtle1/smd_vel` topic resulting in `turtle1` to continously loop around in a circle.

To begin, you need to first run turtlesim buy running:

```bash
ros2 run turtlesim turtlesim_node
```

In a different terminal, run:

```bash
ros2 run turtlesim_circle move_circle
```

The result should look like this:

<img src="/asset/turtle_circle.png" width=900>

The package also allows parameters on linear x axis and angular z axis. The command is written below:

```bash
ros2 run turtlesim_circle move_circle --ros-args -p linear_x_axis:=<float_value> angular_z_axis:=<float_value>
```

<img src="/asset/turtle_circle_param.png" width=900>
