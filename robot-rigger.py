import bpy

# Toggle this to True if you need to debug the script
BONE_RIGGER_LOG = False

bl_info = {
    "name": "Robot Rigger",
    "blender": (2, 80, 0),
    "category": "Object",
    "description": "Automatically match bones to objects. Designed to make rigging mechencial objects much easier with name pattern matching",
    "author": "Ash Blue",
    "version": (1, 0),
    "location": "View3D > UI > Robot Rigger",
    "warning": "",
    "doc_url": "",
    "tracker_url": ""
}

class RigObjectsOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.rig_objects_operator"
    bl_label = "Rig Objects"

    def execute(self, context):
        armature = None
        objects = []
        
        for obj in bpy.context.selected_objects:            
            if obj.type == 'ARMATURE':
                armature = obj
            else:
                objects.append(obj)
                
        if armature:
            self.match_bones_and_objects(armature, objects)
        
        self.br_log(f"Armature: {armature.name if armature else 'None'}, Objects: {len(objects)}")
        
        return {'FINISHED'}
    
    def match_bones_and_objects(self, armature, objects):
        pattern_base = bpy.context.scene.bone_matching_pattern

        # Loop over bones and objects to find matches
        for bone in armature.data.bones:
            pattern = pattern_base.replace("[BONE]", bone.name)
            
            for obj in objects:
                if pattern in obj.name:
                    self.br_log(f"Match found: Bone '{bone.name}' and Object '{obj.name}' in pattern '{pattern}'")
                    self.bind_obj_to_bone(armature, obj, bone)
    
    def bind_obj_to_bone(self, armature, obj, bone):        
        # Store the original world matrix of the object
        original_matrix = obj.matrix_world.copy()
        
        obj.parent = armature
        obj.parent_type = 'BONE'
        obj.parent_bone = bone.name
        
        # Restore the original world matrix to prevent moving the object
        obj.matrix_world = original_matrix
        
    def br_log(self, text):
        if BONE_RIGGER_LOG:
            self.report({'INFO'}, text)

class UnrigObjectsOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.unrig_objects_operator"
    bl_label = "Unrig Objects"

    def execute(self, context):
        armature = None
        objects = []

        # Find the armature and objects
        for obj in bpy.context.selected_objects:
            if obj.type == 'ARMATURE':
                armature = obj
            else:
                objects.append(obj)

        if armature:
            self.unrig_objects(armature, objects)

        self.br_log("Unrigging completed.")
        
        return {'FINISHED'}

    def unrig_objects(self, armature, objects):
        for obj in objects:
            if obj.parent == armature and obj.parent_type == 'BONE':
                # Store the original world matrix
                original_matrix = obj.matrix_world.copy()

                # Clear parent and keep the transform
                obj.parent = None
                obj.matrix_world = original_matrix
                self.br_log(f"Unrigged Object '{obj.name}' from Bone '{obj.parent_bone}'")
                
    def br_log(self, text):
        if BONE_RIGGER_LOG:
            self.report({'INFO'}, text)

class BoneRiggerPanel(bpy.types.Panel):
    bl_label = "Robot Rigger"
    bl_idname = "OBJECT_PT_bone_rigger"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Edit'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        layout.operator(RigObjectsOperator.bl_idname)
        layout.operator(UnrigObjectsOperator.bl_idname)
        
        box = layout.box()
        box.label(text="Pattern:")
        box.prop(scene, "bone_matching_pattern")

def register():
    bpy.utils.register_class(RigObjectsOperator)
    bpy.utils.register_class(UnrigObjectsOperator)
    bpy.utils.register_class(BoneRiggerPanel)
    
    bpy.types.Scene.bone_matching_pattern = bpy.props.StringProperty(
        name="",
        default=".B[BONE]",
        description="Pattern to match bones with objects"
    )

def unregister():
    bpy.utils.unregister_class(RigObjectsOperator)
    bpy.utils.unregister_class(UnrigObjectsOperator)
    bpy.utils.unregister_class(BoneRiggerPanel)
    
    # Delete data so it doesn't leave behind residue for serialization
    del bpy.types.Scene.bone_matching_pattern

if __name__ == "__main__":
    register()
