import addon_utils
import bmesh
import bpy
import mathutils
import os
import xml.etree.ElementTree as ET
from mathutils import Euler
import os.path

# ---- Globals ----

objspath = ""
stageFile = ""
scenario = 0
groundonly = False

def osi_colbox(self, data, expand_property):
    # Creates an expandable and collapsible box for the UILayout.
    box = self.box()
    split = box.split(0.5)
    row = split.row(align=True)
    row.prop(data, expand_property, icon="TRIA_DOWN" if getattr(data, expand_property) else "TRIA_RIGHT",
             icon_only=True, emboss=False)
    row.label(getattr(data.rna_type, expand_property)[1]["name"])
    return box, split

# ---- Preferences ----

class osiAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    # General
    game_path = bpy.props.StringProperty(name="RomFS", description="Path to the Super Mario Odyssey RomFS.", subtype='DIR_PATH')
    objs_path = bpy.props.StringProperty(name="Models", description=" Path to the Odyssey Editor Models folder.", subtype='DIR_PATH')
    
    def draw(self, context):
        box = self.layout.box()
        box.label("General Options:", icon='FILE_FOLDER')
        box.prop(self, "game_path")
        if not self.game_path:
            box.label("Please set a RomFS directory path.", icon='ERROR')
        elif not os.path.isdir(os.path.join(self.game_path, "ObjectData")):
            box.label("Invalid RomFS directory. It does not have an ObjectData subfolder.", icon='ERROR')
        else:
            box.label("The RomFS path is valid!", icon='FILE_TICK')
        
        box.prop(self, "objs_path")
        if not self.game_path:
            box.label("Please set a Models directory path.", icon='ERROR')
        elif not os.path.isdir(os.path.join(self.objs_path, "GameTextures")):
            box.label("Invalid Models directory. It does not have an GameTextures subfolder.", icon='ERROR')
        else:
            box.label("The Models path is valid!", icon='FILE_TICK')

    def run(self):
        objspath = bpy.context.user_preferences.addons[__package__].preferences.objs_path
        tree = ET.parse(stageFile)
        root = tree.getroot()
        for a in root.findall('C0'):
            b = a[scenario]
            for c in b.findall('C0'):
                if c.attrib['Name'] == 'ObjectList':
                    for d in c.findall('C1'):
                        if len(d.attrib) == 0:
                            objName = ''
                            stageName = ''
                            resourcePath = ''
                            unitConfigName = ''
                            objPath = ""
                            objPosX = 0.0
                            objPosY = 0.0
                            objPosZ = 0.0
                            objRotX = 0.0
                            objRotY = 0.0
                            objRotZ = 0.0
                            objScaleX = 0.0
                            objScaleY = 0.0
                            objScaleZ = 0.0
        
                            for string in d.findall('FF'):
                                if len(string.attrib) == 2:
                                    if string.attrib['Name'] == 'ModelName':
                                        objName = string.attrib['StringValue']
        
                            for string in d.findall('A0'):
                                if len(string.attrib) == 2:
                                    if string.attrib['Name'] == 'ModelName':
                                        objName = string.attrib['StringValue']
        
                                    if string.attrib['Name'] == 'UnitConfigName':
                                        unitConfigName = string.attrib['StringValue']
        
                            for attribute in d.findall('C1'):
                                if len(attribute.attrib) == 1:
                                    for value in attribute.findall('D2'):
                                        if len(value.attrib) == 2:
                                            if value.attrib['Name'] == 'X':
                                                string = value.attrib['StringValue']
                                                string = string.replace(',', '.')
                                                if attribute.attrib['Name'] == 'Rotate':
                                                    objRotX = float(string)
        
                                                if attribute.attrib['Name'] == 'Scale':
                                                    objScaleX = float(string)
        
                                                if attribute.attrib['Name'] == 'Translate':
                                                    objPosX = float(string)
                                            
                                            if value.attrib['Name'] == 'Y':
                                                string = value.attrib['StringValue']
                                                string = string.replace(',', '.')
                                                if attribute.attrib['Name'] == 'Rotate':
                                                    objRotY = float(string)
        
                                                if attribute.attrib['Name'] == 'Scale':
                                                    objScaleY = float(string)
        
                                                if attribute.attrib['Name'] == 'Translate':
                                                    objPosY = float(string)
                                            
                                            if value.attrib['Name'] == 'Z':
                                                string = value.attrib['StringValue']
                                                string = string.replace(',', '.')
                                                if attribute.attrib['Name'] == 'Rotate':
                                                    objRotZ = float(string)
        
                                                if attribute.attrib['Name'] == 'Scale':
                                                    objScaleZ = float(string)
        
                                                if attribute.attrib['Name'] == 'Translate':
                                                    objPosZ = float(string)
        
                            someString = ''
                            someString2 = ''
                            if unitConfigName != '':
                                unitConfigName2 = unitConfigName + '.obj'
                                objPath = objspath + str(unitConfigName2)
                                someString = unitConfigName[len(unitConfigName) - 6]
                                someString += unitConfigName[len(unitConfigName) - 5]
                                someString += unitConfigName[len(unitConfigName) - 4]
                                someString2 = unitConfigName[1]
                                someString2 += unitConfigName[2]
                                someString2 += unitConfigName[3]
                            else:
                                objName2 = objName + '.obj'
                                objPath = objspath + str(objName2)
                                someString = objName[len(objName) - 6]
                                someString += objName[len(objName) - 5]
                                someString += objName[len(objName) - 4]
                                someString2 = objName[1]
                                someString2 += objName[2]
                                someString2 += objName[3]
                                
                            if groundonly == False:
                            	someString = 'Gro'
                            
                            if someString == 'Gro' or someString == 'und' or someString2 == 'Key' or someString == 'ing' or someString == 'ild' or someString == 'own' or someString == 'ava' or someString == 'Pan' or someString == 'ceL' or (someString == 'tep' and someString2 == 'Lav'):
                                if os.path.isfile(objPath):
                                    imported_object = bpy.ops.import_scene.obj(filepath=objPath)
                                    obj_object = bpy.context.selected_objects[0]
                                    obj_object.location = (objPosX, objPosY, objPosZ)
                                    obj_object.rotation_euler = Euler((objRotX, objRotY, objRotZ), 'XYZ')
                                    obj_object.scale = (objScaleX, objScaleY, objScaleZ)
        
        print('Done!')
