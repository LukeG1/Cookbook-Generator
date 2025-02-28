## Recipe YAML Format Documentation (Enhanced)

This document outlines a YAML format for structuring recipes. It's designed to be simple and intuitive, allowing you to easily convert your favorite recipes into this format.

### Top-Level Structure

A recipe YAML file consists of several top-level keys:

- **`meta`**: Contains metadata about the recipe.
- **`sections`**: Defines the named sections of the recipe (e.g., batter, topping, etc.).
- **`ingredients`**: Lists all ingredients used in the recipe.
- **`steps`**: Provides the step-by-step instructions for preparing the recipe.

### `meta` Section

The `meta` section stores metadata about the recipe. It's a dictionary (or map) with only the following keys:

- **`title` (required)**: The name of the recipe (string).
- **`preamble` (optional)**: An introductory paragraph or description (string).
- **`author` (required)**: The author of the recipe (string).
- **`attribution` (optional)**: Credit to the source of the recipe (string).
- **`category` (optional)**: The culinary category of the recipe (string).
- **`notes` (optional)**: A list of additional notes or tips (list of strings).
- **`step_format` (optional)**: Specifies the format for displaying steps (string, either `"ol"` for ordered list or `"ul"` for unordered list, defaults to `"ol"`).
- **`tags` (optional)**: A list of tags for categorization or searching (list of strings).

**Example:**

```yaml
meta:
  title: Chorizo Potato Tacos
  preamble: This recipe is a delightful mix of spicy chorizo and crispy potatoes.
  author: Luke Gabel
  attribution: no one really
  category: mexican
  notes:
    - I always use mini tortillas for this.
    - Green salsa or lime is a must.
  step_format: ol
  tags:
    - spicy
    - easy
    - taco
```

### `sections` Section

The `sections` section optionally defines the named sections used in the `steps` section. It's a list of section names (strings). Note that `main` is the default section, to be used when a recipe only has one section (you can't use the main section if you have named ones). The order of this list detirmines the order that the steps and ingredients will be displayed in.

**Example:**

```yaml
sections:
  - batter
  - topping
```

### `ingredients` Section

The `ingredients` section lists all ingredients used in the recipe. It's a dictionary where each key is the ingredient's name, and the value is a dictionary with ingredient details.

Ingredient details can include:

- **`name` (required)**: The name of the ingredient (string).
- **`quantity` (optional)**: The amount of the ingredient (number or string).
- **`unit` (optional)**: The unit of measurement (string).
- **`note` (optional)**: Additional note about the ingredient (string).
- **`section` (optional)**: The section of the recipe where the ingredient is used (string).

**Example (no sections):**

```yaml
ingredients:
  - chorizo:
    name: chorizo
    quantity: 1/2
    unit: lbs
  - potato:
    name: potato
    quantity: 1
  - olive_oil:
    name: olive oil
  - vinegar:
    name: vinegar
```

**Example (sections):**

```yaml
ingredients:
  - bananas:
      quantity: 3
      name: Bananas
      note: extra ripe
      section: topping
  - flour:
      quantity: 2
      unit: cups
      name: Bananas
      section: filling
```

### `steps` Section

The `steps` section contains the step-by-step instructions for preparing the recipe. It is a dictionary of named sections, each containing a list of steps. If you have no sections then all steps should go under the main section.

**Step Format:**

- Each step is a string.
- Use `{ingredient}` to refrence an ingredient, this will be replaced with that ingredient's name
- Use `{#ingredient}` to reference an ingredient and include its quantity, for example `{#flour}` may turn into 'All Purpose Flour[3 cups].
- Use `{ingredient|nickname}` to reference an ingredient with a nickname, this will refrence the ingredient, but call it by something else in this instance, useful when joined with the quantity. It is good practice to refrence the ingredient any time you are going to mention it, even if you use a nickname.
- Use `{^ingredient}` to capitalize the first letter, useful when you want to refrence an ingredient as the first word in a sentence.
- Use `{$ingredient}` to pluralize it, useful when you want to refrence multiple of an ingredient but named it singularly.
- modifiers like `#` and `^` can be chained, for example: `{^#bananas}` could turn into 'Bananas[3]'
- Steps support single line markdown formatting.

**Example (List of Steps):**

```yaml
steps:
  main:
    - Set a medium pot of water to boil.
    - Chop the {#potato} into chunks.
    - Put the chopped {potatoes} in the water and add a splash of {vinegar}.
    - Put your {#chorizo} in a cold pan and set the heat to medium - medium high.
    - Cook the {chorizo} and use a spatula to break it up into bite-sized pieces.
    - When the {potatoes} are just able to be pierced by a fork with some pressure, move the chorizo to a plate, drain the potatoes and add them back to the pan with the chorizo fat.
    - Cook the potatoes, moving them around until all sides are dark and crispy.
    - Once the potatoes are almost crispy enough to your liking, add back in the chorizo and let it all cook together to warm back up.
    - Plate to your liking, I recommend a layer of sour cream to hold everything together, then the mixture, then some green salsa.
    - "Here is a **bold** sentance"
```

**Example (Steps by Section):**

```yaml
steps:
  batter:
    - peel the {#bananas|b-dogs}
    - add the {Bananas}
  topping:
    - add the {#flour} to the thing
```
