import vtk
import numpy as np
import pandas as pd

# colortype:颜色模式

# file_name:星图名称，对应不同文件地址。

# mag：筛选星星亮度

class vtkTimerCallback():
    def __init__(self):
        self.timer_count = 0

    def execute(self, obj, event):
        # print(self.timer_count)
        self.actor.RotateY(10/100)
        # self.actor.SetPosition(self.timer_count, self.timer_count, 0)
        iren = obj
        iren.GetRenderWindow().Render()


def celestial_sphere(colortype='black_mode',file_name='BSC',mag=None):

    ## DATA
    # Generate random points w/ random RGB colors
    file_name_dict={'BSC':"./BSC.csv",'Hipparcos':'./hip_small.csv'}
    df=pd.read_csv(file_name_dict['BSC'])
    #db=pd.read_csv('./bound_small.csv')
    if mag:
        df=df[df.Vmag==mag]
    # 转换经纬度坐标为三维坐标
    def latlong2xyz(lat,lon,R=1):
        R=1
        lat=lat/180*np.arccos(-1)
        lng=lon/180*np.arccos(-1)
        x = R*np.cos(lat)*np.cos(lng)
        y = R*np.cos(lat)*np.sin(lng)
        z = R*np.sin(lat)
        x=round(x,3)
        y=round(y,3)
        z=round(z,3)
        return [x,y,z]

    # 转换b-v数据为rgb
    def bv2rgb(bv):
        if bv < -0.40: bv = -0.40
        if bv > 2.00: bv = 2.00

        r = 0.0
        g = 0.0
        b = 0.0

        if  -0.40 <= bv<0.00:
            t=(bv+0.40)/(0.00+0.40)
            r=0.61+(0.11*t)+(0.1*t*t)
        elif 0.00 <= bv<0.40:
            t=(bv-0.00)/(0.40-0.00)
            r=0.83+(0.17*t)
        elif 0.40 <= bv<2.10:
            t=(bv-0.40)/(2.10-0.40)
            r=1.00
        if  -0.40 <= bv<0.00:
            t=(bv+0.40)/(0.00+0.40)
            g=0.70+(0.07*t)+(0.1*t*t)
        elif 0.00 <= bv<0.40:
            t=(bv-0.00)/(0.40-0.00)
            g=0.87+(0.11*t)
        elif 0.40 <= bv<1.60:
            t=(bv-0.40)/(1.60-0.40)
            g=0.98-(0.16*t)
        elif 1.60 <= bv<2.00:
            t=(bv-1.60)/(2.00-1.60)
            g=0.82-(0.5*t*t)
        if  -0.40 <= bv<0.40:
            t=(bv+0.40)/(0.40+0.40)
            b=1.00
        elif 0.40 <= bv<1.50:
            t=(bv-0.40)/(1.50-0.40)
            b=1.00-(0.47*t)+(0.1*t*t)
        elif 1.50 <= bv<1.94:
            t=(bv-1.50)/(1.94-1.50)
            b=0.63-(0.6*t*t)

        return [255*r, 255*g, 255*b]

    # 三维坐标
    xyz=list()
    for i,j in zip(df['J2000_d'],df['J2000_a']) :
        xyz.append(latlong2xyz(i,j))


    # rgb
    rgb=list()
    for i in df['BV']:
        if colortype in ['black_mode']:
            rgb.append(bv2rgb(i))
        else:
            rgb.append([0,0.8,0])

    #透明度：利用vmag的大小转换，最大值为243，最小为189
    #(5-np.log(3+df.iloc[i,11]))*2/10*255 —— 这个最大最小的区别会更大，感觉更大的数据的话这个会比较好
    alpha=list()
    for i in df['Vmag']:
        if file_name=='BSC':
            a=(5-np.log(3+i))*2/10*255
        else:
            a=(0.875-i/16)*255
        alpha.append(a)

    # Point size
    point_size =4

    ## VTK
    # Create the geometry of a point (the coordinate)
    points = vtk.vtkPoints()
    # Create the topology of the point (a vertex)
    vertices = vtk.vtkCellArray()
    # Setup colors
    Colors = vtk.vtkUnsignedCharArray()
    Colors.SetNumberOfComponents(4)
    Colors.SetName("Colors")
    # Add points
    for i in range(0, len(xyz)):
        p = xyz[i]
        id = points.InsertNextPoint(p)
        vertices.InsertNextCell(1)
        vertices.InsertCellPoint(id)
        Colors.InsertNextTuple4(rgb[i][0], rgb[i][1], rgb[i][2],alpha[i])
    # Create a polydata object
    point = vtk.vtkPolyData()
    # Set the points and vertices we created as the geometry and topology of the polydata
    point.SetPoints(points)
    point.SetVerts(vertices)
    point.GetPointData().SetScalars(Colors)
    point.Modified()
    # Visualize
    mapper = vtk.vtkPolyDataMapper()
    if vtk.VTK_MAJOR_VERSION <= 5:
        mapper.SetInput(point)
    else:
        mapper.SetInputData(point)

    # 加入球体
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetCenter(0.0, 0.0, 0.0) #球体中心点
    sphereSource.SetRadius(1.0) # 球体半径
    # Make the surface smooth.
    sphereSource.SetPhiResolution(100)
    sphereSource.SetThetaResolution(100)
    mapper2 = vtk.vtkPolyDataMapper()
    mapper2.SetInputConnection(sphereSource.GetOutputPort())
    sphere_Actor = vtk.vtkActor()
    sphere_Actor.SetMapper(mapper2)
    sphere_Actor.GetProperty().SetColor((0.,0.,0.2)) #球面颜色（0-1）
    sphere_Actor.GetProperty().SetOpacity(1)

    '''
    # 加入球体
    sphereSource2 = vtk.vtkSphereSource()
    sphereSource2.SetCenter(0.0, 0.0, 0.0)  # 球体中心点
    sphereSource2.SetRadius(0.2)  # 球体半径
    # Make the surface smooth.
    sphereSource2.SetPhiResolution(100)
    sphereSource2.SetThetaResolution(100)
    map_to_sphere = vtk.vtkTextureMapToSphere()
    map_to_sphere.SetInputConnection(sphereSource2.GetOutputPort())
    map_to_sphere.PreventSeamOff()
    # Read the image data from a file
    reader = vtk.vtkJPEGReader()
    reader.SetFileName( 'C:\\Users\\zhaoyue\\Desktop\\under.jpg')
    # Create texture object
    texture = vtk.vtkTexture()
    texture.SetInputConnection(reader.GetOutputPort())
    mapper3 = vtk.vtkPolyDataMapper()
    mapper3.SetInputConnection(map_to_sphere.GetOutputPort())
    sphere_Actor2 = vtk.vtkActor()
    sphere_Actor2.SetMapper(mapper3)
    sphere_Actor2.SetTexture(texture)
    '''


    '''
    planeSource = vtk.vtkPlaneSource()
    planeSource.SetCenter(0.0, 0.0, 0.0)
    planeSource.SetNormal(0.0, 1.0, 0.0)
    planeSource.Update()
    plane = planeSource.GetOutput()
    # Create a mapper and actor
    mapper4 = vtk.vtkPolyDataMapper()
    mapper4.SetInputData(plane)
    actor4 = vtk.vtkActor()
    actor4.SetMapper(mapper4)
    actor4.GetProperty().SetColor((0.26, 0.51, 0.77))
    '''

    ## ACTOR
    # Create an actor
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetPointSize(point_size)
    axes = vtk.vtkAxesActor()
    actor.RotateX(-30)
    actor.RotateZ(180)

    ## RENDER
    renderer = vtk.vtkRenderer()
    # Add actor to the scene
    renderer.AddActor(actor)
    renderer.AddActor(sphere_Actor)
    #renderer.AddActor(sphere_Actor2)

    # Background
    renderer.SetBackground(0,0,0) # 背景颜色（0-1）
    # Reset camera
    renderer.ResetCamera()
    renderer.GetActiveCamera().Zoom(4)
    # Render window
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindow.SetSize(480, 480)
    # Interactor
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    #renderWindowInteractor.SetInteractorStyle(0)
    renderWindowInteractor.SetRenderWindow(renderWindow)
    #renderWindowInteractor.SetInteractorStyle(KeyPressInteractorStyle(parent=renderWindowInteractor))
    renderWindowInteractor.Initialize()


    # Sign up to receive TimerEvent
    cb = vtkTimerCallback()
    cb.actor = actor
    renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
    renderWindowInteractor.CreateRepeatingTimer(100)

    # Begin interaction
    renderWindow.Render()
    renderWindowInteractor.Start()

celestial_sphere()