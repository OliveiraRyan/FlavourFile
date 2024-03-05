# FlavourFile

Alternate name: Taste Trove

This is a personal repository of recipes that I like. There are/will be 4 component to this repo:
1. Static storage of the recipes (JSON)
   *  *Progress Pictures* is a list of tuples that contains a step (int) and a link to an image (string)
   *  Experiment with using an ID/Slug as the identifier instead of the name. This allows for duplicate names, eliminates need for names to be descriptive, and allows the keys to be less restrictive in naming
2. Class object to store recipe information within the program once queried (Python)
3. System to select and display/output a recipe by name/ID (Python)
4. System to insert new recipes into the repository (Manually for now -> Some sort of GUI (e.g. React) later)

### Next steps:
* Most likely allow this repository to live somewhere online, probably connected to a personal site, and have some sort of GUI to easily access the information on the go.