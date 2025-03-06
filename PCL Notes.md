## PCL Notes

### 1.PCL documents

[Point Cloud Library | The Point Cloud Library (PCL) is a standalone, large scale, open project for 2D/3D image and point cloud processing.](https://pointclouds.org/)

[PCL(Point Cloud Library)学习记录（2025）](https://www.yuque.com/huangzhongqing/pcl)

[PCL(Point Cloud Library)学习指南&资料推荐（2025版） - 知乎](https://zhuanlan.zhihu.com/p/268524083)

[边缘疯狂试探的个人空间-边缘疯狂试探个人主页-哔哩哔哩视频](https://space.bilibili.com/504859351/lists/536852?type=series)

### 2.PCL environments

配置PCL Ubuntu环境可参考下面文章：

[Ubuntu环境下PCL配置](https://blog.csdn.net/qq_41092406/article/details/117930972)



### 3. 点云可视化

（1）

```python
// An highlighted block

#include <pcl/visualization/cloud_viewer.h>
#include <iostream>
#include <pcl/io/io.h>
#include <pcl/io/pcd_io.h>
#include <pcl/io/ply_io.h>
#include <pcl/point_types.h>

using namespace pcl;
using namespace pcl::io;

int user_data;

void
viewerOneOff(pcl::visualization::PCLVisualizer& viewer)
{
    viewer.setBackgroundColor(1.0, 0.5, 1.0);
    pcl::PointXYZ o;
    o.x = 1.0;
    o.y = 0;
    o.z = 0;
    //viewer.addSphere(o, 0.25, "sphere", 0);
    std::cout << "i only run once" << std::endl;

}

void
viewerPsycho(pcl::visualization::PCLVisualizer& viewer)
{
    static unsigned count = 0;
    std::stringstream ss;
    ss << "Once per viewer loop: " << count++;
    //viewer.removeShape("text", 0);
    //viewer.addText(ss.str(), 200, 300, "text", 0);

    //FIXME: possible race condition here:
    user_data++;
}

int
main()
{

    pcl::PointCloud<pcl::PointXYZRGBA>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZRGBA>);
    pcl::io::loadPCDFile("rabbit.pcd", *cloud);

    pcl::visualization::CloudViewer viewer("Cloud Viewer");

    //blocks until the cloud is actually rendered
    viewer.showCloud(cloud);

    //use the following functions to get access to the underlying more advanced/powerful
    //PCLVisualizer

    //This will only get called once
    viewer.runOnVisualizationThreadOnce(viewerOneOff);

    //This will get called once per visualization iteration
    viewer.runOnVisualizationThread(viewerPsycho);
    while (!viewer.wasStopped())
    {
        //you can also do cool processing here
        //FIXME: Note that this is running in a separate thread from viewerPsycho
        //and you should guard against race conditions yourself...
        user_data++;
    }
    return 0;
}

```

数据结构：

* ​



## 4.Filter

(1) SoR

```c++
#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/filters/statistical_outlier_removal.h>

int
main ()
{
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZ>);
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_filtered (new pcl::PointCloud<pcl::PointXYZ>);

  // Fill in the cloud data
  pcl::PCDReader reader;
  // Replace the path below with the path where you saved your file
  reader.read<pcl::PointXYZ> ("table_scene_lms400.pcd", *cloud);

  std::cerr << "Cloud before filtering: " << std::endl;
  std::cerr << *cloud << std::endl;

  // Create the filtering object
  pcl::StatisticalOutlierRemoval<pcl::PointXYZ> sor;
  sor.setInputCloud (cloud);
  sor.setMeanK (50);
  sor.setStddevMulThresh (1.0);
  sor.filter (*cloud_filtered);

  std::cerr << "Cloud after filtering: " << std::endl;
  std::cerr << *cloud_filtered << std::endl;

  pcl::PCDWriter writer;
  writer.write<pcl::PointXYZ> ("table_scene_lms400_inliers.pcd", *cloud_filtered, false);

  sor.setNegative (true);
  sor.filter (*cloud_filtered);
  writer.write<pcl::PointXYZ> ("table_scene_lms400_outliers.pcd", *cloud_filtered, false);

  return (0);
}
```

