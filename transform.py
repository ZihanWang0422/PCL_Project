import open3d as o3d
import laspy
import numpy as np

def las_to_pcd_with_open3d(las_path, pcd_path):
    # 1. 读取LAS文件
    las = laspy.read(las_path)
    
    # 2. 提取坐标（laspy自动处理缩放和偏移）
    x = las.x
    y = las.y
    z = las.z
    
    # 3. 创建Open3D点云对象
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.vstack((x, y, z)).T
    
    # 4. 可选：添加颜色信息（如果LAS包含RGB）
    if hasattr(las, 'red') and hasattr(las, 'green') and hasattr(las, 'blue'):
        # 归一化到 [0,1] 范围（LAS通常使用16位存储）
        colors = np.vstack((las.red/65535.0, 
                           las.green/65535.0, 
                           las.blue/65535.0)).T
        pcd.colors = o3d.utility.Vector3dVector(colors)
    
    # 5. 保存为PCD格式
    o3d.io.write_point_cloud(pcd_path, pcd)
    
    # 可选：可视化验证
    o3d.visualization.draw_geometries([pcd])

# 使用示例
las_to_pcd_with_open3d("input.las", "output.pcd")