# Blender - Eevee Toon Solidify .py
A script to generate a real-time simulated toon shading for an object in Blender Eevee using Solidify modifier method.

### How to use :
    
   1. Launch Blender
    
   2. On one of the windows, click on the top-left dropdown icon and select **'Text Editor'** below **Scripting** column.
    
   3. Click **'Open'** on the top-middle of the window.
    
   4. Navigate to this **'script-eevee_toon_solidify.py'** file location and open it.
    
   5. On the **3D Viewport** window, select an object with at least one material.
    
   6. On the **Text Editor** window, click the **'Run Script'** button (the button with a triangle facing right as its icon) and wait until the process completes.
    
   7. (Optional) if there's certain parts of the model (with different materials) that don't need to be outlined; 
       replace the **'toon_solidify_outline'** material on the slot below that certain parts' material with **'toon_solidify_transparent'**

### Known issues :
1. Sometimes it will generate an error with something along the lines of "unallowed". I find closing and reopening Blender fixes it, make sure to save your progress first.
