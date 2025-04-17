*****
Extra
*****

These rig types are used to give new objects/constraints/modifiers attached to the rig.

--------------------

.. _pinerig.extra.lattice:

Lattice
=======

:bdg-success:`single bone`

| Inspired from CloudRig, creates a lattice with master and tweak control.
| Adds 3 bones : ``LTC-master``, ``LTC-tweak`` and ``MCH-LTC-parent``, along with a lattice object.
| Strength and falloff parameters are accessible in pose mode on any controller bone.

- **Lattice** *(Object)*
    The lattice object that will be generated. If empty, one will be created.
- **Regenerate lattice** *(Boolean)*
    | Whether the lattice should be re-generated from scratch or not. 
    | Disable this if you want to customize the lattice, otherwise any changes beside the object's name, will be lost when you re-generate the rig.
- **Object to link** *(Object)*
    | Object which will have a lattice modifier added to it upon generation. 
    | Must be of type Mesh, Text, Curve, Surface or Lattice.

--------------------

.. _pinerig.extra.warp:

Warp
====

:bdg-success:`single bone`

| Creates a lattice-like control but using a Warp modifier on the targeted object(s)/
| Adds 3 bones : ``WRP-master``, ``WRP-tweak`` and ``MCH-WRP-parent``, along with a warp modifier to the targeted object(s).
| The strength and falloff of the warp is tuned with the ``warp_strength / warp_falloff`` custom bone parameter of warp_master.

- **Mesh** *(Object)*
    The mesh object that will have the warp modifier added to.
- **Regenerate warp** *(Boolean)*
    Resets the warp modifier if set to True.