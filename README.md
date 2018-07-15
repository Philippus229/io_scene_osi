# io_scene_osi (Odyssey Stage Importer)
A Blender add-on that can import Super Mario Odyssey stages/levels

## Preparing the stage
1. Open the stage (and scenario) you want to import in Odyssey Editor (https://github.com/exelix11/OdysseyEditor/releases) to convert the models in the scene to OBJ files.

## Importing the stage
1. Open Blender, import the add-on, set the "RomFS" path to a valid SMO RomFS path and set the "Models" path to the "Models" folder of Odyssey Editor.
2. To import a stage, go to "File"->"Import"->"SMO Stage (.byml/.szs)", select a stage BYML/SZS, set the value of "Scenario" to the scenario you want to load (0-14) and import the stage by clicking on "Import Stage".
Note: When the option "Only Main Ground [WIP]" is checked, only the main ground models will be imported. This option is still in development and only works for some stages.
