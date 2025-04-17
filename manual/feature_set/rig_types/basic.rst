
*****
Basic
*****

These single-bone rig types are used to generate features than can tedious to repeat multiple time throughout the metarig.
They must be applied separately to every bone even within a connected chain,
and can have connected children controlled by a different rig type.
This is unlike chain-based rig types that usually consume the whole connected chain.

.. _pinerig.basic.piston:

Piston
======

Adds a simple piston rig to the bone. There is an option to disable control bones.
Start and end parents parameters can be entered in the form of string names of the bones that will become the parent of each ends of the piston.

Requirement: A chain of at least two connected bones.

Make Control (Boolean)
   Creates controls bones for each ends of the piston.
Widget (Boolean)
   Choose a registered widget type for the control bones.
Parent Head (Boolean)
   Name of the bone in the generated rig that will be the parent of the tail of the piston. Leaving it empty will default it to the parent of the ORG bone.
Parent Tail (Boolean)
   Name of the bone in the generated rig that will be the parent of the tail of the piston. Leaving it empty will default it to `Parent Head`.


.. _pinerig.basic.root:

Root
====

Adds multiple roots (up to 3) to the rig while generating widgets appropriately.
All children of this bone will be parented to the last root in the rig _('root_03' if root_number = 3, 'root_2' if root_number = 2)_.
All bones without a parent in the metarig will be parented upon generation to the master root _('root' regardless of root_number's value)_.

Requirement : The bone using this meta-rig type should not be named 'root' as to not trigger an error with the default Rigify generation script. 
Using 'Root' or anything else is fine though. The master root will always be named 'root' after generation.

Number of root bones (Integer)
   Number of root bones that will be generated _(min = 1, max = 3)_.

Register Parent (Boolean)
   Registers the rig as a potential parent scope for its child sub-rigs' parent switches.

   Tags (String)
      Specifies additional comma-separated tag keywords for the registered parent scope.
      They can be used by other rigs to filter parent choices, or for selecting the default parent.

      Some of the existing tags that are useful here:

      ``injected`` (special)
         The parent scope will be made available for all children of the *parent* sub-rig,
         rather than just this rig's children.
      ``held_object``
         A control for the object held in the character's hand. Preferred by finger IK.

         The ``injected,held_object`` combination is perfect for such a control.


.. _pinerig.basic.single_axis_pivot:

Single Axis Pivot
=================

Adds a pivot bone with mechanisms and controls to allow it (and its children sub-rigs) to rotate along a single axis.
Useful for elongated props like guns and blades.

Widget Type
   Allows selecting one of the predefined widgets to generate for the master control instead of the `spin_pivot`.


.. _pinerig.basic.ball:

Ball
====

Adds a simple ball rig with squash and stretch controls that can be rotated anywhere independently from the spin control.
This rig type is quite useful to get a quick but versatile squash and stretch setup working for props or cartoony characters.
A pivot bone can also be added if needed.

Extra Pivot (Boolean)
   Adds a custom pivot bone for the main control.
Assign Tweak Collections (Boolean)
   If enabled, allows placing the squash and pivot bones into the specified bone collections.
