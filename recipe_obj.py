import json

class Recipe:
    def __init__(self, slug:str):
        self.slug = slug
        self.name = ""
        self.image = ""
        self.description = ""
        self.ingredients = []
        self.steps = []
        self.progress_pictures = []
        self.prep_time = 0
        self.cook_time = 0
        self.servings = 0
        self.populate_values()
        # TODO: Add some protection if the recipe (slug) does not exist
        # TODO: Search for slugs by parial match

    def __repr__(self):
         return "Recipe(slug:str)"
    
    def __str__(self):
        # Formats the lists into strings with newlines for prettier printing. Also adds numbers prefixing each step.
        formatted_ingredients = '\n\t'.join(['\t']  + self.ingredients)
        formatted_steps = '\n\t'.join(['\t']  + [str(i+1) + '. ' + self.steps[i] for i in range(len(self.steps))])

        return f"""    
    {self.name}
    {self.description}

    Ingredients:{formatted_ingredients}
    
    Steps:{formatted_steps}

    Prep time: {self.prep_time} minutes
    Cook time: {self.cook_time} minutes
    Servings: {self.servings}
    """
    
    def populate_values(self):
        with open('recipes.json') as file:
            recipe = json.load(file)[self.slug]

        self.name = self.slug # may be subject to change
        self.image = recipe['Image']
        self.description = recipe['Description']
        self.ingredients = recipe['Ingredients']
        self.steps = recipe['Steps']
        self.progress_pictures = recipe['Progress Pictures']
        self.prep_time = recipe['Prep Time']
        self.cook_time = recipe['Cook Time']
        self.servings = recipe['Servings']

    # TODO: This whole function (super low - negative priority)
    def convert_servings(self, value:int, mode='r'):
        # This is basically a setter that will change the ratios of the ingredients based on a new serving quantity
        # There will be 5 modes: r/a/s/m/d (replace, add, subtract, multiply, divide) with r being default
        # This is essentially a bunch of string comprehension with some twists. Definitely not needed but could be a cool nice-to-have
        # Changes can always be undone by calling populate_values() again.
        pass

    def get_recipe(self):
        # Returns a tuple of all the attributes of this object.
        # TODO: Should probably return a dict or smth instead though.
        return self.name, self.image, self.description, self.ingredients, self.steps, self.progress_pictures, self.prep_time, self.cook_time, self.servings

    def get_name(self) -> str:
        # Returns the Recipe's name.
        return self.name
    
    def get_image(self) -> str:
        # Returns the Recipe's main image.
        return self.image
    
    def get_description(self) -> str:
        # Returns the Recipe's description.
        return self.description
    
    def get_ingredients(self) -> list[str]:
        # Returns the Recipe's ingredients.
        return self.ingredients
    
    def get_steps(self) -> list[str]:
        # Returns the Recipe's steps.
        return self.name
    
    def get_progress_pictures(self) -> list[tuple[int, str]]:
        # Returns the Recipe's progress pictures corresponding to specified steps.
        return self.progress_pictures
    
    def get_prep_time(self) -> int:
        # Returns the Recipe's prep time.
        return self.prep_time
    
    def get_cook_time(self) -> int:
        # Returns the Recipe's cook time.
        return self.cook_time
    
    def get_servings(self) -> int:
        # Returns the Recipe's servings.
        return self.servings
    


# for testing purposes:
# r = Recipe("Pancakes")
# print(r)