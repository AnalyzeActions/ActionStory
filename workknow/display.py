"""Display messages in the terminal window."""

from workknow import configure
from workknow import constants
from workknow import debug


def display_tool_details(
    debug_level: debug.DebugLevel = debug.DebugLevel.ERROR,
):
    """Display the details about the tool."""
    # STEP: setup the console and the logger and then create a blank line for space
    console, logger = configure.setup(debug_level)
    # STEP: display the messages about the tool
    console.print()
    console.print(
        constants.workknow.Emoji + constants.markers.Space + constants.workknow.Tagline
    )
    console.print(constants.workknow.Website)
    console.print()
