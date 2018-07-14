# io_scene_osi
A Blender add-on that can import Super Mario Odyssey stages/levels

## Preparing the stage
1. Open the stage (and scenario) you want to import in Odyssey Editor (https://github.com/exelix11/OdysseyEditor/releases) to convert the models in the scene to OBJ files.
2. Extract the stage SZS with SARCExtract (https://github.com/aboood40091/SARCExtract/releases) and convert the stage's main BYML file to an XML file using TheFourthDimension (https://github.com/exelix11/TheFourthDimension/releases).
3. Open the XML file in Notepad++ (https://notepad-plus-plus.org/download) and replace all non-ASCII characters with 0 by setting the "search mode" to "regular expression" and replacing "[^\x00-\x7F]+" with "0"
4. Replace "shift_jis" in the first line with "utf-8", convert the encoding to UTF-8 and save the file.

## Using the add-on
1. Open Blender, import the add-on, set the "RomFS" path to a valid SMO RomFS path and set the "Models" path to the "Models" folder of Odyssey Editor.
2. To import a stage, go to "File"->"Import"->"SMO Stage (.xml)", select a stage XML, set the value of "Scenario" to the scenario you want to load (0-14) and import the stage by clicking on "Import SMO Stage XML".
Note: When the option "Only Main Ground" is checked, only the main ground models will be imported. This option is still in development and only works for some stages.
