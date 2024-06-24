# baseline's modified Z-S Overview

Is this too much work for a stupid overview? Absolutely. But whenever an expansion comes out I keep making stupid mistakes when updaing my overviews so I'm making this to organize my thoughts and design philosophy.

## Overview Types

Single Window is for one overview window. **Currently not updated.**

Multi-Window is meant for 3 as pictured below
<details>
  <summary>Multi window example</summary>

  ![multi window](images/Multi_Window.png)
</details>


## Other Files

`colors.txt` saves common coloring tags

Files in the `Group Parsing` folder has python scripts that process filter groups.

* Combine: c + p filter groups in `oringnal.txt`, run the script, and they will appear sorted with removed dupes in `result.txt`
* Remove: c + p a filter group in `original.txt`, and another filter group in `remove.txt` that you'd like to take out from the original. For example:

      original = [1, 2, 3, 4, 5]
      remove = [2, 4]
      ->
      final = [1, 3, 5]

`Grouped Types.yaml` saves all groups within a category in each filter, e.g. everything under the "Asteroid" filter lists groups in the "Asteroid" type from the filters tab. This is just to make c + p and manual yaml editing a bit easier.

* Also saves common groupings, such as (and not limited to):
  * Drones and fighters
  * Immediate threats, such as bombs and probes
  * Containers


## Window Organization:

Refer to multi window image

### Filters i.e. stuff you see in the overview:

#### ︽ Top window to show warpables and relevant celestials i.e. stuff off grid

* Travel: Displays all major warp-tos and system-wide affects, including most of the types below in this category
* Celestials: All warpable objects in space
* Docks: Anything you can potentially dock in
* FW/SOV: Faction warfare and nullsec sovereignty points

#### ✜ Middle main window to show immediate contacts of interest or threats i.e. stuff on grid with you

    All filters here will include immediate threats, such as bombs, probes, and certain deployables

* All Targets: All combat-related entities relevant to immediate grid awareness
* PvE: Ditto, including krabbing activities
* Ships only: As name implies for minimal clutter
* ✥ Target [Group]: Specific types to display, like tackle and ewar. Note that because T1 ships are not separated by bonus types there will be some overlap, e.g. all frigates in "tackle". Unneeded info > no info

#### Bottom window to show all non-immediate stuff on grid

* ✪ Friendly All: All allies, excluding FW militia due to FRAT awoxing
* ✪ Friendly Fleet: Fleet members only. Meant for logi and NPSI
* ✜ Covops Collidables: Anything that can decloak you
* ✜ Salvage/Loot: This one's for Brave. Includes MTUs and depos

### ⌘ Bracket Filters i.e. stuff you see in space:

* Combat (+Dro): All combat-related entities that can damage you and vise versa.
* Combat (-Dro): Ditto, but no drones and fighters. **Not recommended for regular use**, this is meant for large fleet battles to reduce clutter
* PvE: Mostly the same as above but includes krabbing activities like PI, asteroids, etc.

---

Keep calm and /open_overview_settings