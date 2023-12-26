# Blender 3D - Robot Rigger Add-on

## Description
The Robot Rigger add-on for Blender provides a convenient way to automatically rig and unrig objects to bones based on a naming pattern. This tool is designed for quickly rigging robots, mechanical objects, and non-organic items. This is a micro-framework and designed to be non-intrusive to your existing Blender workflow.

## Installation

### Prerequisites
- Blender version 2.80 or later.

### Steps to Install
1. **Download the Add-on**
   - Download the `robot-rigger.py` file from the provided source.

2. **Open Blender**
   - Launch Blender on your computer.

3. **Open Preferences**
   - Navigate to `Edit > Preferences` from the Blender top menu.

4. **Install the Add-on**
   - In the Preferences window, switch to the `Add-ons` tab.
   - Click the `Install` button at the top.
   - Navigate to and select the `robot-rigger.py` file you downloaded.
   - Click `Install Add-on`.

5. **Enable the Add-on**
   - In the Add-ons list, search for "Robot Rigger".
   - Enable the add-on by clicking the checkbox next to its name.

6. **Save Preferences**
   - (older versions of Blender only) To ensure the add-on remains enabled each time Blender is started, click `Save Preferences` at the bottom of the Preferences window if necessary.

## Getting Started

### Where to Find the UI
Once installed and enabled, the Robot Rigger panel can be found in the 3D Viewport's UI sidebar, under the "Edit" tab. It provides functionalities to rig and unrig objects based on the specified naming pattern.

### Rigging Objects

The auto rigger will parent a number of objects to bones based on a naming pattern. The naming pattern is defined by the user and can be customized. The default naming pattern is `.B[BONE]`. For example, an object named `Arm.BArm.L` will be bone parented to a bone named `Arm.L` if the object and bone are selected and the rig button is clicked.

1. Ensure your objects and the bones in your armature have matching names according to the `.B[BONE]` pattern (e.g., an object named `Arm.BArm.L` matches with a bone named `Arm.L`).
2. Select all the objects you want to rig, along with the armature.
3. In the Robot Rigger panel under the "Edit" tab, click the "Rig Objects" button.
4. The selected objects will now be parented to their corresponding bones.

### Unrigging Objects

The auto unrigger uses the same matching pattern as the auto rigger. It will safely unparent ONLY objects that match the bone pattern. This is useful for cleaning up objects that need to be altered without damaging the rig.

1. Select all the objects and the armature that you previously rigged.
2. In the Robot Rigger panel, click the "Unrig Objects" button.
3. The selected objects will be safely unparented from their bones, maintaining their world position.

### Customization

The naming pattern can be altered to match your project needs and is saved to your file.

1. Go to the Robot Rigger panel in the 3D Viewport's UI sidebar, under the "Edit" tab.
2. Locate the field labeled "Pattern."
3. Enter your custom naming pattern (e.g., `CustomPattern[BONE]`).
4. This new pattern will be used for subsequent rigging and unrigging operations.

## Author
- Ash Blue
