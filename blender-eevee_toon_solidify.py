'''
This script generates simulated toon shading using Solidify modifier on an object
Only tested on EEVEE so far, you're welcome to try on other renderer if available (Cycles, etc.)
How to use :
    1. Launch Blender
    
    2. On one of the windows, click on the top-left dropdown icon and select 'Text Editor' below Scripting column.
    
    3. Click 'Open' on the top-middle of the window.
    
    4. Navigate to this 'script-eevee_toon_solidify.py' file location and open it.
    
    5. On the 3D Viewport window, select an object with at least one material.
    
    6. On the Text Editor window, click the 'Run Script' button (the button with a triangle facing right as its icon) and wait until the process completes.
    
    7. (Optional) if there's certain parts of the model (with different materials) that don't need to be outlined; 
        replace the 'toon_solidify_outline' material on the slot below that certain parts' material with 'toon_solidify_transparent'
'''
import bpy

index = 0
object = bpy.context.view_layer.objects.active

# Creating the material for the outline
material_outline = bpy.data.materials.get('toon_solidify_outline')
if material_outline is None:
    material_outline = bpy.data.materials.new(name='toon_solidify_outline')
    material_outline.use_backface_culling = True
    material_outline.use_nodes = True
    material_outline.node_tree.links.clear()
    material_outline.node_tree.nodes.clear()
    material_outline_nodes = material_outline.node_tree.nodes
    material_outline_links = material_outline.node_tree.links
    material_outline_output = material_outline_nodes.new(type='ShaderNodeOutputMaterial')
    material_outline_shader = material_outline_nodes.new(type='ShaderNodeEmission')
    material_outline_shader.inputs[0].default_value = (0,0,0,1)
    material_outline_shader.inputs[1].default_value = 1
    material_outline_links.new(material_outline_shader.outputs[0], material_outline_output.inputs[0])

# Creating the material for the transparent outline
material_transparent = bpy.data.materials.get('toon_solidify_transparent')
if material_transparent is None:
    material_transparent = bpy.data.materials.new(name='toon_solidify_transparent')
    material_transparent.use_backface_culling = True
    material_transparent.use_nodes = True
    material_transparent.blend_method = 'BLEND'
    material_transparent.node_tree.links.clear()
    material_transparent.node_tree.nodes.clear()
    material_transparent_nodes = material_transparent.node_tree.nodes
    material_transparent_links = material_transparent.node_tree.links
    material_transparent_output = material_transparent_nodes.new(type='ShaderNodeOutputMaterial')
    material_transparent_shader = material_transparent_nodes.new(type='ShaderNodeBsdfTransparent')
    material_transparent_links.new(material_transparent_shader.outputs[0], material_transparent_output.inputs[0])

# Counting the amount of materials inside the object

material_slots = []
material_slot_index = 0
for material in object.data.materials: 
    material_slots.append([material_slot_index, material.blend_method])
    material_slot_index += 1

# Placing outline materials below each existing materials in the object
for material in material_slots:
    bpy.ops.object.material_slot_add()
    if (material[1] == 'BLEND'): object.active_material = material_transparent
    else: object.active_material = material_outline
    if index > 0:
        for i in range(index): bpy.ops.object.material_slot_move(direction='UP')
    index += 2

# Adds Solidify modifier into the object with certain properties
# Feel free to adjust the Solidify modifier's properties later
if object.modifiers.get('Solidify') is None: bpy.ops.object.modifier_add(type = 'SOLIDIFY')
object.modifiers['Solidify'].thickness = 0.001
object.modifiers['Solidify'].offset = 1
object.modifiers['Solidify'].use_rim = False
object.modifiers['Solidify'].use_flip_normals = True
object.modifiers['Solidify'].material_offset = 1
