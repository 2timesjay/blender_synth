import bpy

# Create a new scene
scene = bpy.data.scenes.new('Scene')

# Add the default cube to the scene
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))

# Set the resolution
scene.render.resolution_x = 640
scene.render.resolution_y = 480

# Set the output file format
scene.render.image_settings.file_format = 'PNG'

# Set the output file path
scene.render.filepath = '/path/to/output/file.png'

bpy.ops.render.render(write_still=True)