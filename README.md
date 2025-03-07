## LiDAR 3D point cloud reconstrunction

### Intro

In this project, I focus on building 3D point cloud reconstrunction.

**CMake**
```C++
//go to build folder, open terminal
CMake ..
make
//Run xx.cpp 
./ xx
//Now you can see some details in your terminal
```

### 1. Viewer

Run `pcl_viewer name.pcd`  in terminal, you can see a 3D point window.

![Rabbit](image.png)

⚠️ Note: You may meet some problem like:
`pcl_viewer: ../../src/xcb_io.c:260: poll_for_event: Assertion !xcb_xlib_threads_sequence_lost' failed.
已放弃 (核心已转储)
` Run command again can solve it!

### 2. Filter

#### 2.1 SoR
