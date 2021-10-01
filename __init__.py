# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "sollumz",
    "author" : "skylumz",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Import-Export"
}

import bpy

# from .ydrimport import ImportYdrXml, ydr_menu_func_import
from .ybnimport import ImportYbnXml, ybn_menu_func_import
from .ybnexport import ExportYbnXml, ybn_menu_func_export
# from .yddimport import ImportYddXml, ydd_menu_func_import
from .sollumz_properties import DrawableProperties, GeometryProperties, TextureProperties, ShaderProperties, CollisionProperties, BoundProperties, BoundFlags, assign_properties
from .sollumz_ui import SOLLUMZ_PT_MAIN_PANEL, SOLLUMZ_PT_MAT_PANEL, SOLLUMZ_PT_SHADER_PANEL

# Development: Reload submodules
from . import resources

import importlib
importlib.reload(resources)
# importlib.reload(resources.cwxml)
# importlib.reload(resources.polygon)
# importlib.reload(resources.bound)

classes = (ExportYbnXml, SOLLUMZ_PT_MAIN_PANEL, SOLLUMZ_PT_MAT_PANEL, SOLLUMZ_PT_SHADER_PANEL, 
DrawableProperties, GeometryProperties, TextureProperties, ShaderProperties, CollisionProperties, BoundProperties, BoundFlags, ImportYbnXml)
# ImportYdrXml, ImportYbnXml, ImportYddXml, ImportYbnXml

def register():
    for c in classes:
        bpy.utils.register_class(c)
    # bpy.types.TOPBAR_MT_file_import.append(ydr_menu_func_import)
    bpy.types.TOPBAR_MT_file_import.append(ybn_menu_func_import)
    bpy.types.TOPBAR_MT_file_export.append(ybn_menu_func_export)
    # bpy.types.TOPBAR_MT_file_import.append(ydd_menu_func_import)
    assign_properties()

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    # bpy.types.TOPBAR_MT_file_import.remove(ydr_menu_func_import)
    bpy.types.TOPBAR_MT_file_import.remove(ybn_menu_func_import)
    bpy.types.TOPBAR_MT_file_export.remove(ybn_menu_func_export)
    # bpy.types.TOPBAR_MT_file_import.remove(ydd_menu_func_import)