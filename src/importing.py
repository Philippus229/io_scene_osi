import bpy
import bpy_extras
import os
from . import addon
import xml.etree.ElementTree as ET
from mathutils import Euler
import os.path

class ImportOperator(bpy.types.Operator, bpy_extras.io_utils.ImportHelper):
    """Load an SMO stage file"""
    bl_idname = "import_scene.osi"
    bl_label = "Import Stage"
    bl_options = {'UNDO'}

    filename_ext = ".xml"
    filter_glob = bpy.props.StringProperty(default="*.xml", options={'HIDDEN'})
    filepath = bpy.props.StringProperty(name="File Path", description="Filepath used for importing the stage XML file.", maxlen=1024, default="")
    scenarioValue = bpy.props.IntProperty(name="Scenario", description="Scenario to import.", min=0, max=14)
    onlyground = bpy.props.BoolProperty(name="Only Main Ground", description="Only import main ground models.")

    @staticmethod
    def menu_func(self, context):
        self.layout.operator(ImportOperator.bl_idname, text="SMO Stage (.xml)")

    def execute(self, context):
        importer = Importer(self, context, self.properties.filepath, self.properties.scenarioValue, self.properties.onlyground)
        return importer.run()

class Importer:
    def __init__(self, operator, context, filepath, scenarioValue, onlyground):
        self.operator = operator
        self.context = context
        self.filepath = filepath
        self.scenarioValue = scenarioValue
        self.onlyground = onlyground

    def run(self):
        addon.stageFile = self.filepath
        addon.scenario = self.scenarioValue
        addon.groundonly = self.onlyground
        exec(addon.osiAddonPreferences.run(addon.osiAddonPreferences))
        return {'FINISHED'}
        
