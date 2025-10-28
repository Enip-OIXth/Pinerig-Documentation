
*****
Limbs
*****

These rig types handle generation of different kind of limbs and their features, like fingers.


--------------------

.. _pinerig.limbs.finger:

Finger
==================

:bdg-info:`Bone Chain`

Will create a bendy and stretchy finger chain with a master control bone that controls the rotation of all joints through its scale.
The master bone can rotate each individual phalanx using it's local X, Y and Z scale.
By default, 'X' is for the first phalanx, 'Y' for the second one and 'Z' for the tip of the finger.

.. important::
   Requirement: The bone with this pinerig-type must be a chain of at least two connected bones.


- **Bend Rotation Axis** *(Automatic, X, Y, Z, -X, -Y, -Z)*
   Defines the automatic rotation axis to be linked to the scale of the master bone.
- **B-Bone Segments** *(Integer)*
   Defines the number of b-bone segments each tweak control will be split into.
- **IK Control**
   Generates a very simple IK mechanism with only one control.

   IK starts its work with the shape of the finger defined by FK controls and adjusts it
   to make the fingertip touch the IK control. It is designed as a tool to temporarily keep
   the fingertip locked to a surface it touches, rather than a fully featured posing system.

   To improve performance, the switchable parent for the IK control contains only one option beside None.
   Thus it is advised to add a 'held object' control using the `basic.pivot <https://docs.blender.org/manual/en/latest/addons/rigging/rigify/rig_types/basic.html#rigify-rigs-basic-pivot>`_
   rig to act as the common parent for the fingers with a fully functional parent switch.
- **IK Local Location**
   Specifies the value of the Local Location option for IK controls, which decides if the location
   channels are aligned to the local control orientation or world.
- **Assign Tweak Layers**
   If enabled, allows placing the Tweak controls in different bone collections from the main controls.
- **Assign Extra IK Layers**
   If enabled, allows placing the extra IK control in different bone collections from the main controls.

.. note::

   Rotation Axis (Bend Rotation Axis in the case of `Finger`_)
   affects the `roll <https://docs.blender.org/manual/en/latest/animation/armatures/bones/editing/bone_roll.html>`_ of the generated bones.
   Automatic mode recalculates the generated bones roll while
   any of the Manual modes copy the roll of the meta-rig bones.


--------------------

.. _pinerig.limbs.shoulder:


Shoulder
================

:bdg-success:`Single Bone`

Creates a shoulder rig with an automatic rotation mechanism when it's children limb is moved in IK. 
The mechanism can be toggled off to keep the default rigify behaviour.
Also added a way to add specific widgets to the control bone.

.. important::
   Requirement : The bone with this pinerig-type must have a child chain with a valid '.arm' rigify-type in order to generate properly.


--------------------

.. _pinerig.limbs.arm:

Arm
=========

:bdg-info:`Bone Chain`

Will create a fully featured bendy and stretchy arm depending on the user-defined options.
Adds an option to create joint lock bones assigned to the ``tweak`` bone collection. 
Those bones are handy if a character interacts with a surface like a desk or while crawling, as they act a bit like an IK for elbows joints.

.. important::
   Requirement: A chain of three connected bones (upper_arm, forearm, hand).


- **Add Joint Lock** *(Boolean)*
   Create joint lock bone assigned to the ``tweak`` bone collection. This bone can also be used as a switchable parent candidate for the ``hand_ik`` control bone.
- **IK Wrist Pivot**
   Generates an extra child of the hand IK control that rotates around the tail of the hand bone.
- **Rotation Axis** *(Automatic, X, Z)*
   Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
- **Limb Segments** *(Integer)*
   Defines the number of additional tweak controls each limb bone will have on the final rig.
- **B-Bone Segments** *(Integer)*
   Defines the number of b-bone segments each tweak control will be split into.
- **Custom IK Pivot**
   Generates an extra control for the end of the IK limb that allows rotating it around an arbitrarily placed pivot.
- **Assign FK Layers**
   If enabled, allows placing the FK chain in different bone collections from the IK bones.
- **Assign Tweak Layers**
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.


--------------------

.. _pinerig.limbs.leg:

Leg
=========

:bdg-info:`Bone Chain`

Will create a fully featured bendy and stretchy leg depending on the user-defined options.
Adds an option to create joint lock bones assigned to the ``tweak`` bone collection. 
Those bones are handy if a character interacts with a surface like a desk or while crawling, as they act a bit like an IK for elbow/knee joints.

.. important::
   Requirement: A chain of four connected bones (thigh, shin, foot, toe) with one unconnected
   child of the foot to be used as the heel pivot.


- **Add Joint Lock** *(Boolean)*
   Create joint lock bone assigned to the ``tweak`` bone collection. This bone can also be used as a switchable parent candidate for the ``foot_ik`` control bone.
- **Foot Pivot** *(Ankle, Toe, Ankle & Toe)*
   Specifies where to put the pivot location of the main IK control, or whether to generate an additional
   pivot control at the base of the toe.
- **Separate IK Toe**
   Specifies that two separate toe controls should be generated for IK and FK instead of sharing one bone.
   This is necessary to get fully correct IK-FK snapping in all possible poses.
- **Toe Tip Roll**
   Generates a slider to switch the heel control to pivot on the tip rather than the base of the toe
   (for roll this obviously only applies on forward roll).

- **Rotation Axis** *(Automatic, X, Z)*
   Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
- **Limb Segments** *(Integer)*
   Defines the number of additional tweak controls each limb bone will have on the final rig.
- **B-Bone Segments** *(Integer)*
   Defines the number of b-bone segments each tweak control will be split into.
- **Custom IK Pivot**
   Generates an extra control for the end of the IK limb that allows rotating it around an arbitrarily placed pivot.
- **Assign FK Layers**
   If enabled, allows placing the FK chain in different bone collections from the IK bones.
- **Assign Tweak Layers**
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.


--------------------

.. _pinerig.limbspaw:

Paw
=========

:bdg-info:`Bone Chain`

Will create a fully featured bendy and stretchy paw depending on the user-defined options.

.. important::
   Requirement: A chain of four or five connected bones (thigh, shin, paw, *optional* digit, toe).


- **Rotation Axis** *(Automatic, X, Z)*
   Defines the bend axis for the IK chain. FK chains will have a totally free degree of rotation on all axes.
- **Limb Segments** *(Integer)*
   Defines the number of additional tweak controls each limb bone will have on the final rig.
- **B-Bone Segments** *(Integer)*
   Defines the number of b-bone segments each tweak control will be split into.
- **Custom IK Pivot**
   Generates an extra control for the end of the IK limb that allows rotating it around an arbitrarily placed pivot.
- **Assign FK Layers**
   If enabled, allows placing the FK chain in different bone collections from the IK bones.
- **Assign Tweak Layers**
   If enabled, allows placing the Tweak controls in different bone collections from the IK bones.


--------------------

.. _pinerig.limbs.front_paw:

Front Paw
===============

:bdg-info:`Bone Chain`

Derivative of `Paw`_ with extended IK suitable for use in front paws.
The additional IK limits the degree of change in the angle between shin and
paw bones (2nd and 3rd) as the main IK control moves and rotates.

.. note::
   For best results, the shin bone should not be parallel to either thigh or paw in rest pose,
   i.e. there should be some degree of bend in all joints of the paw.

- **Heel IK Influence**
   Influence of the extended IK. At full rotating the main IK control or digit bone would
   not affect the rotation of the paw bone, while lower values provide some blending.


--------------------

.. _pinerig.limbs.rear_paw:


Rear Paw
==============

:bdg-info:`Bone Chain`

Derivative of `Paw`_ with extended IK suitable for use in rear paws.
The additional IK tries to maintain thigh and paw bones (1st and 3rd) in a nearly parallel orientation
as the main IK control moves and rotates.

.. note::
   For best results, thigh and paw bones should start nearly parallel in the rest pose.

