
****
Face
****

These rig types implement components of a modular face.


.. _pinerig.face.aim:

Aim
===

Adds an aim constraint to the bone. Contrary to the **`Eye`** rig type, it requires no child chains to generate properly.
Creates a master control shared by all bones of this type in the same Aim Group.


Make Deform (Boolean)
   Creates a secondary deform bone.
Aim Group (String)
   If multiple aim rigs target the same group, a master control bone will be created as a target for the cluster.
Target Distance (Float)
   Allows to tweak the distance of the aim target from the aim group. The distance is not in Blender units, but rather a relative value from the scale of the rig and the averaged distance between all sub-rigs in the aim group.
Widget
   Allows to change the widget of the `aim` control bone upon generation.


.. _pinerig.face.eye:

Eye
===

Derivative of aim rig that mimics all the features of the default rigify `face.skin_eye <https://docs.blender.org/manual/en/latest/addons/rigging/rigify/rig_types/face.html#face-skin-eye>` rig type but with extra features like eyelid collision and Aim Groups.
Implements a skin system [parent controller](skin#parent-controllers) that manages two skin chains for the top and bottom eyelids in addition to generating the eye rotation mechanism.
The eyelids are rigged to follow the movement of the eyeball with adjustable influence.

Requirements : The bone with this pinerig-type must have two with stretchy chains tagged with .T/.B symmetry in the name to mark the eyelids. These eyelids chains must be connected at each end forming eye corners. The chains are rigged to follow the surface of the eye and twist to its normal.

Enable Eyelid Collision (Boolean)
   Generates a mechanism allowing the upper eyelid to collide with the lower one. This can be disabled through the bone property of the upper eyelid's middle controller. 
Create Eyeball and Iris Deforms (Boolean)
   Generates deform bones for the eyeball and the iris, the latter copying XZ scale from
   the eye target control. The iris is located at the tail of the ORG bone.
Eyelid Detach Option (Boolean)
   Generates a slider to disable the mechanism that keeps eyelid controls stuck to the surface of the eye.
Split Eyelid Follow Slider (Boolean)
   Generates two separate sliders for controlling the influence of the eye rotation on X and Z eyelid motion.
Eyelids Follow Default (Boolean)
   Depending on *Split Eyelid Follow Slider*, specifies the default values for the split follow sliders,
   or fixed factors to be multiplied with the single common follow influence slider value.
Aim Group (String)
   If multiple aim rigs target the same group, a master control bone will be created as a target for the cluster.
Target Distance (Float)
   Allows to tweak the distance of the aim target from the aim group. The distance is not in Blender units, but rather a relative value from the scale of the rig and the averaged distance between all sub-rigs in the aim group.
Widget
   Allows to change the widget of the `eye` control bone upon generation.


.. _pinerig.face.jaw:

Jaw
===

Base rig type used for the generation of a complex mouth rig. Mimics all the features of the default rigify `face.jaw <https://docs.blender.org/manual/en/latest/addons/rigging/rigify/rig_types/face.html#face-skin-jaw>` rig type. 
This rig can add jaw stretch and targeting controls, teeth an lip collision, lip zip and roll and extra lip controls.
The lip loops are sorted into layers based on the distance from corners to the common center and rigged with blended influence of the jaw and the master mouth control. 
Other child rigs become children of the jaw.

Requirements : The bone with this pinerig-type must have 4 child chains which connect together at their ends using ``.L/.R`` and ``.T/.B`` symmetry in order to generate properly. 
It can also need two children subrigs with the teeth pinerig-type for teeth collision.


.. card:: Jaw Settings

    Bottom Lip Influence (Float)
      Specifies the influence of the jaw on the inner bottom lip with mouth lock disabled.
   Locked Influence (Float)
      Specifies the influence of the jaw on both lips of locked mouth.
   Secondary Influence Falloff (Float)
      Specifies the factor by which influence fades away with each successive lip loop
      (for bottom lip loops the blend moves away from inner bottom lip to full jaw influence).
   Make Secondary Jaw Controls (Boolean)
      Adds stretching and target control bones to the jaw.


.. Teeth Settings

Add Teeth Collision (Boolean)
   Requires 2 teeth pinerig-types as children of the jaw. Generates mechanisms allowing the upper teeth to collide with the lower teeth. 
   This can be disabled using the bone property of the upper teeth's bone. Offset and Collision Stop Distance can also be tweaked that way after generation.


.. Lip Settings

Enable Lip Collision (Boolean)
   Generates the mechanisms allowing the upper lip to collide with the lower lip. This can be disabled using the bone property of any upper lip bone.
Create Lip Roll (Boolean)
   Generates the mechanisms allowing the lips to roll using action constraints and roll controlers at the top and bottom corners of the mouth.
Create Lip Zip (Boolean)
   Generates the mechanisms allowing the lips to close using a zip controler at the left and right corners of the mouth.
Lip Zip Interpolation Mode ('Linear' , 'Smooth')
   Allows to choose how the lip zip mechanism interpolates between the bones in the chain.


.. Extra Lips Settings

Create Extra Lips Controls (Boolean)
   Creates new lip bones distributed along the nodes formed by the original lip bones. This allows to have more tweakers if needed.
Extra Lip Bones Number (Integer)
   Generates more bone per segment of the original lip. 
   '1' will create one extra_bone per node. 
   '2' will create one extra_bone per mouth corner (where the lip chains connect at their ends : Top, Bottom, Left and Right) and one extra_bone per subdivided bone segment. 
   '3' will create one extra_bone per node and subdivided bone segment.
Generate Extra Lips Deform (Boolean)
   Generates deform bones for the extra lips.
Disable Default Lips Deform (Boolean)
   Disables the deform of the original lip bones, allowing only the extra_lips to have deformation.


.. _pinerig.face.teeth:

Teeth
=====

A simple copy rig that allows teeth to individually follow the jaw or not via bone properties. 
It is also necessary to have this rig type for teeth collision that can be set up in the jaw pinerig-type.

Requirements : The bone with this pinerig-type must be a child of the jaw pinerig-type and have a .T/.B symmetry in the name to mark the upper and lower teeth.

Widget
   Allows to change the widget of the `teeth` control bone upon generation.