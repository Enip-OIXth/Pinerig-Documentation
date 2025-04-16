---
layout: page
title: Installation and Updates
permalink: /installation
description: "Here you can find the installation instructions for the plugin."
---

## Requirements

This addon requires Blender 4.3.0 or later. 
Earlier versions of Blender will not work because the addon uses features that were introduced only in Blender 4.3.0.

## Installation

1. Download the zipped code here from Github. (Check in the release tab for the latest stable release)
2. In Blender, open `Edit` -> `Preferences` -> `Addons` -> Enable and expand `Rigify` -> **`Install Feature Set from File`**. 
3. Navigate to where you saved the zip file and click **`Add external feature set`**.
4. Once activated, go to `Edit` -> `Preferences` -> `Addons` and search **`Pinerig`** and enable it.
5. The UI will appear in the armature Rigify properties panel in the `Properties` tab.


## Updating from an earlier version

The addon currently has no support for extension updates, therefore in order to update the addon, perform the following steps:

- **Be sure to backup your project, so you can go back in case things don't work out as intended.**
- Check the [CHANGES.md]({{site.repo}}/blob/main/CHANGES.md) for any breaking changes that might impact your project and any special update instructions.
- Download the version you want to install from the [Release List]({{site.repo}}/releases) (use the _Source Code ZIP_ link).
- Deactivate the addon and the Rigify feature set in Blender. 
- Go into the folder where you installed the previous version and delete it. Put the new zip in it's place.
- Re-do the installation from step 2 onwards.
