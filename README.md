# rkim.dev

## Adding/Editing Portfolio Content

The _Portfolio_ is divided into three major _subcomponents_: "Research", "Work Experience", and "Projects". These are each placed as their own directories inside of the `portfolio/` directory.

When making changes, there are **two** places you need to pay attention to:

1. `_quarto.yaml`: In the root directory, this file manages all navigation links
2. `portfolio/<research|work_experience|projects>/items.yaml`: For each subcomponent of the portfolio, you manage that subcomponent's items through their yaml file

Whenever you add a new portfolio item, make sure to add that item's `index.qmd` path to their respective subcomponent inside of `_quarto.yaml`. You also need to add details about that portfolio item inside that subcomponent's `items.yaml` file.

Each portfolio item has the following general structure:

```
- id: Same as the item's folder name
  title: Printed in the subcomponent's page
  dates:
    - year: This respresents the LATEST date
      month: Months go from 1-12
    - year: If a second date, then the second date represents the START, and the first date represents the END
      month: Months go from 1-12
  category: Research|Work|Projects
  subcategory: null|VR|Web|Game|Hardware|etc.
  links:
    - name: printed text
      href: url
  collaborators:
    - name: name - position
      links: 
        - name: printed text
          href: null|url
        - name: email w/ no mailto
          href: null
  media:
    - name: figcaption
      href: url|local path rel. to current `index.qmd`
      type: figure|iframe
  details:
    - name: label name
      contents:
        - item 1
        - item 2
```

Modifying each portfolio item's entry in the `items.yaml` file controls how they appear in the subcomponent's summary page. The "Projects" page is the only one so far that uses the `subcategory` label to distinguish between different project types. If you need to add subcategories to other subcomponent summary pages, then just follow the formula established by the "Projects" page

Your job does not end there, though. In each individual portfolio item's `index.qmd` page, you have to pay attention to the following:

- The YAML data at the top controls the following:
    - `title`: The portfolio item's text in the sidebar nav window
    - `subtitle`: Can be longer than the `title`, usually as either a full position/description or some additional context
- The first Python code segment controls extra details that appear right after the title, **Make sure to adjust the `details` line so that `item['id']==<YAML ID>` where `YAML_ID` is the `id` you've set for that portfolio item in that subcomponent's `items.yaml`.
- Each portfolio item has tabs! Be cognizant of what tabs you are adding!
    - Each tab is represented by an `## TAB NAME` inside of `::: {.panel-tabset}`.
    - Try to keep `TAB NAME` short, for mobile
    - You can't make the appearance of tabs dynamic by printing `<h2>TAB NAME</h2>` via Python; because of how Quarto works, this will print the `h2` inside of a `div` and thus won't be counted as a tab.

## Publishing to Github Pages

To publish this website to Github Pages, proceed with the following instructions, as defined in <https://quarto.org/docs/publishing/github-pages.html>:

1. Make sure you are on the `main` channel.
2. Render your webpage using `quarto render`.
3. Push all changes to Github.
4. Input the following command: `quarto publish gh-pages` 