# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions, OptionSet
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from ..Items import item_name_groups
from typing import Mapping, Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################

class NumberOfBags(Range):
    display_name = "Number of Bags"
    range_start = 1
    range_end = 100
    default = 32
    group: "Set Details"
class NumberOfPages(Range):
    display_name = "Number of Pages"
    range_start = 1
    range_end = 2000
    default = 150  
    group: "Set Details"
class NumberOfBooklets(Range):
    display_name = "Number of Instruction Booklets"
    range_start = 1
    range_end = 4
    default = 1
    group: "Set Details"
class NumberOfMinifigs(Range):
    display_name = "Number of Minifigs"
    range_start = 1
    range_end = 40
    default = 0
    group: "Set Details"
class ProgressiveBags(DefaultOnToggle):
	"""Disabling this will make the build more difficult, but more random. Move to a later book and assemble what you can to get more checks, or otherwise make progress on your build. If your LEGO Set has different builds for each instruction booklet, this is a good setting to disable."""
	display_name = "Require Bags to be released in order"
	group: "Randomization"
class ProgressivePages(DefaultOnToggle):
	"""Disabling this will make the build much more difficult, but more random. Move to a later page and assemble what you can to get more checks, or otherwise make progress on your build."""
	display_name = "Require Pages to be released in order"
	group: "Randomization"
class ProgressiveBooks(DefaultOnToggle):
	"""Disabling this will make the build more difficult, but more random. Move to a later book and assemble what you can to get more checks, or otherwise make progress on your build. If your LEGO Set has different builds for each instruction booklet, this is a good setting to disable."""
	display_name = "Require Books to be released in order"
	group: "Randomization"

class ColorLocke(Toggle):
	"""Get Creative! You can't build with a color until you've unlocked it."""
	display_name = "Require Colors to be Unlocked before you can build with them. Start with a basic palette."
	group: "Colors"
class EnabledColors(OptionSet):
	"""As you build the set, recieve colors and unlock them as you build.
	All Colors are already on the list, remove them easily with the options builder.
	As you build a color, mark it complete and unlock a check.
			
	Enable colors that are present in your LEGO Set.
		-Go to bricklink and search for your set. I.e. https://www.bricklink.com/v2/catalog/catalogitem.page?S=11509-1#T=I.
		-Select 'Set Inventory' tab and color name alphebetically should be default sort.
		-Scroll down the page and remove from this list the colors that are not present in the Set Inventory.

	"""
	display_name="Add Colors to the Item Pool"
	valid_keys=item_name_groups["Colors"]
	default=frozenset(valid_keys)
	group:"Colors"
    
# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
	options["number_of_bags"] = NumberOfBags
	options["number_of_pages"] = NumberOfPages
	options["number_of_booklets"] = NumberOfBooklets
	options["number_of_minifigs"] = NumberOfMinifigs
	options["enabled_colors"] = EnabledColors  # This registers the yaml option as `enabled_colors`
	return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
	# To access a modifiable version of options check the dict in options.type_hints
	# For example if you want to change DLC_enabled's display name you would do:
	# options.type_hints["DLC_enabled"].display_name = "New Display Name"
	
	#  Here's an example on how to add your aliases to the generated goal
	# options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
	# options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

	options.type_hints["Progressive_Bags"] = ProgressiveBags
	options.type_hints["Progressive_Pages"] = ProgressivePages
	options.type_hints["Progressive_Books"] = ProgressiveBooks

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
	# Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
	return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
