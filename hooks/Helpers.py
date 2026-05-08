from typing import Optional, TYPE_CHECKING
from BaseClasses import MultiWorld, Item, Location


if TYPE_CHECKING:
    from ..Items import ManualItem
    from ..Locations import ManualLocation






# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: "ManualItem") -> Optional[bool]: 
    # Remove unwanted colors from the item pool
    if "Colors" in item["category"]:
        from ..Helpers import get_option_value
        enabled_colors = get_option_value(multiworld, player, "enabled_colors")
        return item["name"] in enabled_colors  # True if they're in the yaml, false if they're not
    return None
    
# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    from ..Items import item_name_groups
    if category_name in item_name_groups["Colors"]:
        # This category is the name of a champion
        from ..Helpers import get_option_value
        enabled_colors = get_option_value(multiworld, player, "enabled_colors")
        return category_name in enabled_colors
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location: "ManualLocation") -> Optional[bool]:
    return None
