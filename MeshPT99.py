from __future__ import print_function
import os
import vtk

class MeshPT99Viewer:
    def __init__(self, data_dir):
        # Read the data
        filename = "mesh_xct_s24_d0pt99_diamond.ply"

        # Read Mesh
        meshSource = vtk.vtkPLYReader()
        meshSource.SetFileName(filename)
        meshSource.Update()
        
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(meshSource.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetOpacity(0.3)
        self.actor = actor
        self.meshSource = meshSource


