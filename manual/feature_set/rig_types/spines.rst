
******
Spines
******

These rigs are used to generate spine structures.

--------------------

.. _pinerig.spines.spine:

Spine
==================

:bdg-info:`Bone Chain`

| Defines a bendy and stretchy b-bones spine.
| Adds a way to rename the master control ``center of gravity`` bone named ``torso`` in rigify.
| Clarifies some parameters like pivot position and changes the custom widget for the master control.

- **Hips Pivot Position** *(Integer)*
   Defines how many bones in the spine chain will be affected by the hips control rather than the chest control.
- **Custom Pivot Control** *(Boolean)*
   Create a rotation pivot that can be repositioned arbitrarily.
- **Center of Gravity Bone Name** *(String)*
   Sets the name of the COG bone (root of the torso) created at the hips.
- **Assign Tweak Layers**
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.
- **FK Controls** *(Boolean)*
   Specifies whether to generate an FK control chain.
- **Assign FK Layers**
   If enabled, allows placing the FK chain in different bone collections from the IK bones.

--------------------

.. _pinerig.spines.head:

Head
=================

:bdg-info:`Bone Chain`

Defines a head rig with follow torso controls.

- **Add Head Squash** *(Boolean)*
   Create a ``head_squash`` bone at the top of the head, which allows simple squash and stretch deformations.
- **Create Headtrack** *(Boolean)*
   | Generate a headtracking mechanism and extend it to the parent spine. 
   | The headtrack control can be reparented like a pivot bone.
- **Assign Tweak Layers**
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.
