*****
Installation & Updates
*****

These single-bone rig types are used to generate features than can tedious to repeat multiple time throughout the metarig.
They must be applied separately to every bone even within a connected chain, and can have connected children controlled by a different rig type.
This is unlike chain-based rig types that usually consume the whole connected chain.

--------------------

.. _requirements:

Requirements
======

This addon requires Blender 4.3.0 or later. 
Earlier versions of Blender will not work because the addon uses features that were introduced after Blender 4.3.0.

--------------------

.. _purchase-and-download:

Purchase and Download
====

Where to purchase the addon or to retreive the latest updates:

- **Purchase on Superhive (formerly Blender Market)**: 
    | - Check your emails, Superhive should have sent you an email containing the links to download the files.
    | - Log in to your account and go to the orders page: https://blendermarket.com/account/orders
- **Purchase on Gumroad**:
    | - Log in to your Gumroat account: https://gumroad.com/
    | - When updating, go to your `Library` page, click on the name of the product, and download files: https://app.gumroad.com/library

--------------------

.. _installation:

Installation
======

| 1. Download the zipped code here from Github. (Check in the release tab for the latest stable release)
| 2. In Blender, open `Edit` -> `Preferences` -> `Addons` -> Enable `Rigify` (if it's not already done).
| 3. Click on the addons settings dropdown and use `Install from Disk`.
| 4. Navigate to where you saved the zip file and click validate **`Install from Disk`**.
| 5. Once activated, go to `Edit` -> `Preferences` -> `Addons` and search **`Pinerig`** and enable it.
| 6. Be sure to install the feature set by clicking on the **`Install Featureset`** button.
| 7. If the Pinerig UI appears in the N-panel and in the rigify rig type data property, you are all set!

--------------------

.. _update:

Update
======

The addon currently has no support for extension updates, therefore in order to update the addon, perform the following steps:

- **Be sure to backup your project, so you can go back in case things don't work out as intended.**
- Check the changelogs for any breaking changes that might impact your project and any special update instructions.
- Download the version you want to install.
- Uninstall the Rigify feature set and the addon in Blender (through `Edit` -> `Preferences` -> `Addons`). 
- Go into the folder where you installed the previous version and delete it. Put the new zip in it's place.
- Re-do the installation from step 2 onwards.
