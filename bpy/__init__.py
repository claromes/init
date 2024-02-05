bl_info = {
    "name" : "",
    "description" : "",
    "author" : "Claromes",
    "version" : (0, 1, 0),
    "blender" : (4, 0, 2),
    "location" : "",
    "doc_url": "",
    "tracker_url": "",
    "category": ""
}

import bpy
# from . import

classes = ()

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # append
    # bpy.types.VIEW3D_HT_header.append(header_pnl.PANEL.draw)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # remove
    # bpy.types.VIEW3D_HT_header.remove(header_pnl.PANEL.draw)