#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""QRainbowStyle default palette."""

# Standard library imports
from collections import OrderedDict

# package imports
from qrainbowstyle.colorsystem import *


class BasePalette:
    """Base class for palettes."""

    # Color
    COLOR_BACKGROUND_1 = ""
    COLOR_BACKGROUND_2 = ""
    COLOR_BACKGROUND_3 = ""
    COLOR_BACKGROUND_4 = ""
    COLOR_BACKGROUND_5 = ""
    COLOR_BACKGROUND_6 = ""

    COLOR_TEXT_1 = ""
    COLOR_TEXT_2 = ""
    COLOR_TEXT_3 = ""
    COLOR_TEXT_4 = ""

    COLOR_ACCENT_1 = ""
    COLOR_ACCENT_2 = ""
    COLOR_ACCENT_3 = ""
    COLOR_ACCENT_4 = ""
    COLOR_ACCENT_5 = ""

    OPACITY_TOOLTIP = 0

    # Size
    SIZE_BORDER_RADIUS = "4px"

    # Borders
    BORDER_1 = "1px solid $COLOR_BACKGROUND_1"
    BORDER_2 = "1px solid $COLOR_BACKGROUND_4"
    BORDER_3 = "1px solid $COLOR_BACKGROUND_6"

    BORDER_SELECTION_3 = "1px solid $COLOR_ACCENT_3"
    BORDER_SELECTION_2 = "1px solid $COLOR_ACCENT_2"
    BORDER_SELECTION_1 = "1px solid $COLOR_ACCENT_1"

    TITLE_BAR_BACKGROUND_COLOR = COLOR_ACCENT_3
    TITLE_BAR_BUTTONS_HOVER_COLOR = COLOR_ACCENT_4
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = COLOR_TEXT_1

    # Paths
    PATH_RESOURCES = "':/qss_icons'"

    @classmethod
    def to_dict(cls, colors_only=False):
        """Convert variables to dictionary."""
        order = [
            "COLOR_BACKGROUND_6",
            "COLOR_BACKGROUND_5",
            "COLOR_BACKGROUND_4",
            "COLOR_BACKGROUND_2",
            "COLOR_BACKGROUND_3",
            "COLOR_BACKGROUND_1",
            "COLOR_TEXT_1",
            "COLOR_TEXT_2",
            "COLOR_TEXT_3",
            "COLOR_TEXT_4",
            "COLOR_ACCENT_1",
            "COLOR_ACCENT_2",
            "COLOR_ACCENT_3",
            "COLOR_ACCENT_4",
            "OPACITY_TOOLTIP",
            "SIZE_BORDER_RADIUS",
            "BORDER_1",
            "BORDER_2",
            "BORDER_3",
            "BORDER_SELECTION_3",
            "BORDER_SELECTION_2",
            "BORDER_SELECTION_1",
            "TITLE_BAR_BACKGROUND_COLOR",
            "TITLE_BAR_BUTTONS_HOVER_COLOR",
            "TITLE_BAR_BUTTONS_DISABLED_COLOR",
            "TITLE_BAR_TEXT_COLOR",
            "PATH_RESOURCES",
        ]
        dic = OrderedDict()
        for var in order:
            value = getattr(cls, var)

            if colors_only:
                if not var.startswith("COLOR"):
                    value = None

            if value:
                dic[var] = value

        return dic

    @classmethod
    def color_palette(cls):
        """Return the ordered colored palette dictionary."""
        return cls.to_dict(colors_only=True)


class Oceanic(BasePalette):
    """Theme variables."""

    COLOR_BACKGROUND_1 = "#263238"
    COLOR_BACKGROUND_2 = "#2f4048"
    COLOR_BACKGROUND_3 = "#34474f"
    COLOR_BACKGROUND_4 = "#394d57"
    COLOR_BACKGROUND_5 = "#3d545f"
    COLOR_BACKGROUND_6 = "#425b67"

    COLOR_TEXT_1 = Gray.B130
    COLOR_TEXT_2 = Gray.B110
    COLOR_TEXT_3 = Gray.B90
    COLOR_TEXT_4 = Gray.B80

    COLOR_ACCENT_1 = "#0a4542"
    COLOR_ACCENT_2 = "#136460"
    COLOR_ACCENT_3 = "#097D74"
    COLOR_ACCENT_4 = "#56BFBA"
    COLOR_ACCENT_5 = "#C4D6DB"

    TITLE_BAR_BACKGROUND_COLOR = COLOR_ACCENT_3
    TITLE_BAR_BUTTONS_HOVER_COLOR = COLOR_ACCENT_4
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = COLOR_TEXT_1

    OPACITY_TOOLTIP = 230


class QDarkStyle(BasePalette):
    COLOR_BACKGROUND_1 = "#19232d"
    COLOR_BACKGROUND_2 = "#27323c"
    COLOR_BACKGROUND_3 = "#35414b"
    COLOR_BACKGROUND_4 = "#3e4b55"
    COLOR_BACKGROUND_5 = "#47555f"
    COLOR_BACKGROUND_6 = "#505f69"

    COLOR_TEXT_1 = Gray.B130
    COLOR_TEXT_2 = Gray.B110
    COLOR_TEXT_3 = Gray.B90
    COLOR_TEXT_4 = Gray.B80

    COLOR_ACCENT_1 = "#14506e"
    COLOR_ACCENT_2 = "#145f87"
    COLOR_ACCENT_3 = "#146998"
    COLOR_ACCENT_4 = "#1478b1"
    COLOR_ACCENT_5 = "#148cd2"

    TITLE_BAR_BACKGROUND_COLOR = COLOR_ACCENT_3
    TITLE_BAR_BUTTONS_HOVER_COLOR = COLOR_ACCENT_4
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = COLOR_TEXT_1

    OPACITY_TOOLTIP = 230


class DarkOrange(BasePalette):
    """A dark theme with orange accents."""

    COLOR_BACKGROUND_1 = Gray.B10
    COLOR_BACKGROUND_2 = Gray.B20
    COLOR_BACKGROUND_3 = Gray.B30
    COLOR_BACKGROUND_4 = Gray.B40
    COLOR_BACKGROUND_5 = Gray.B50
    COLOR_BACKGROUND_6 = Gray.B60

    COLOR_TEXT_1 = Gray.B130
    COLOR_TEXT_2 = Gray.B110
    COLOR_TEXT_3 = Gray.B90
    COLOR_TEXT_4 = Gray.B80

    COLOR_ACCENT_1 = "#ce4b01"
    COLOR_ACCENT_2 = "#d66522"
    COLOR_ACCENT_3 = "#de8044"
    COLOR_ACCENT_4 = "#e79b65"
    COLOR_ACCENT_5 = "#efb587"

    TITLE_BAR_BACKGROUND_COLOR = COLOR_ACCENT_3
    TITLE_BAR_BUTTONS_HOVER_COLOR = COLOR_ACCENT_4
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = COLOR_TEXT_1
    OPACITY_TOOLTIP = 230


class GBK(BasePalette):
    """A dark theme with a brown background and orange accents."""

    COLOR_BACKGROUND_1 = "#14130a"
    COLOR_BACKGROUND_2 = "#1f1d15"
    COLOR_BACKGROUND_3 = "#2a2820"
    COLOR_BACKGROUND_4 = "#35322b"
    COLOR_BACKGROUND_5 = "#403d36"
    COLOR_BACKGROUND_6 = "#4b4841"

    COLOR_TEXT_1 = "#f4f4f4"
    COLOR_TEXT_2 = "#d9d9d9"
    COLOR_TEXT_3 = "#bfbfbf"
    COLOR_TEXT_4 = "#a6a6a6"

    COLOR_ACCENT_1 = "#b04228"
    COLOR_ACCENT_2 = "#c24a32"
    COLOR_ACCENT_3 = "#d5523c"
    COLOR_ACCENT_4 = "#e76c51"
    COLOR_ACCENT_5 = "#f38d77"

    TITLE_BAR_BACKGROUND_COLOR = COLOR_ACCENT_3
    TITLE_BAR_BUTTONS_HOVER_COLOR = COLOR_ACCENT_4
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = COLOR_TEXT_1
    OPACITY_TOOLTIP = 230


class LightOrange(BasePalette):
    COLOR_BACKGROUND_1 = Gray.B140
    COLOR_BACKGROUND_2 = Gray.B130
    COLOR_BACKGROUND_3 = Gray.B120
    COLOR_BACKGROUND_4 = Gray.B110
    COLOR_BACKGROUND_5 = Gray.B100
    COLOR_BACKGROUND_6 = Gray.B90

    COLOR_TEXT_1 = Gray.B10
    COLOR_TEXT_2 = Gray.B20
    COLOR_TEXT_3 = Gray.B50
    COLOR_TEXT_4 = Gray.B70

    COLOR_ACCENT_1 = "#ce4b01"
    COLOR_ACCENT_2 = "#d66522"
    COLOR_ACCENT_3 = "#de8044"
    COLOR_ACCENT_4 = "#e79b65"
    COLOR_ACCENT_5 = "#efb587"

    TITLE_BAR_BACKGROUND_COLOR = COLOR_ACCENT_3
    TITLE_BAR_BUTTONS_HOVER_COLOR = COLOR_ACCENT_4
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = COLOR_TEXT_1

    OPACITY_TOOLTIP = 230


class QDarkStyle3Light(BasePalette):
    COLOR_BACKGROUND_1 = Gray.B140
    COLOR_BACKGROUND_2 = Gray.B130
    COLOR_BACKGROUND_3 = Gray.B120
    COLOR_BACKGROUND_4 = Gray.B110
    COLOR_BACKGROUND_5 = Gray.B100
    COLOR_BACKGROUND_6 = Gray.B90

    COLOR_TEXT_1 = Gray.B10
    COLOR_TEXT_2 = Gray.B20
    COLOR_TEXT_3 = Gray.B50
    COLOR_TEXT_4 = Gray.B70

    COLOR_ACCENT_1 = Blue.B130
    COLOR_ACCENT_2 = Blue.B100
    COLOR_ACCENT_3 = Blue.B90
    COLOR_ACCENT_4 = Blue.B80
    COLOR_ACCENT_5 = Blue.B70

    TITLE_BAR_BACKGROUND_COLOR = COLOR_ACCENT_3
    TITLE_BAR_BUTTONS_HOVER_COLOR = COLOR_ACCENT_4
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = COLOR_TEXT_1

    OPACITY_TOOLTIP = 230


class QDarkStyle3(BasePalette):
    COLOR_BACKGROUND_1 = Gray.B10
    COLOR_BACKGROUND_2 = Gray.B20
    COLOR_BACKGROUND_3 = Gray.B30
    COLOR_BACKGROUND_4 = Gray.B40
    COLOR_BACKGROUND_5 = Gray.B50
    COLOR_BACKGROUND_6 = Gray.B60

    COLOR_TEXT_1 = Gray.B130
    COLOR_TEXT_2 = Gray.B110
    COLOR_TEXT_3 = Gray.B90
    COLOR_TEXT_4 = Gray.B80

    COLOR_ACCENT_1 = Blue.B20
    COLOR_ACCENT_2 = Blue.B40
    COLOR_ACCENT_3 = Blue.B50
    COLOR_ACCENT_4 = Blue.B70
    COLOR_ACCENT_5 = Blue.B80

    TITLE_BAR_BACKGROUND_COLOR = COLOR_ACCENT_3
    TITLE_BAR_BUTTONS_HOVER_COLOR = COLOR_ACCENT_4
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = COLOR_TEXT_1

    OPACITY_TOOLTIP = 230


class PWRDark(BasePalette):
    """A dark theme with orange accents."""

    COLOR_BACKGROUND_1 = Gray.B10
    COLOR_BACKGROUND_2 = Gray.B20
    COLOR_BACKGROUND_3 = Gray.B30
    COLOR_BACKGROUND_4 = Gray.B40
    COLOR_BACKGROUND_5 = Gray.B50
    COLOR_BACKGROUND_6 = Gray.B60

    COLOR_TEXT_1 = Gray.B130
    COLOR_TEXT_2 = Gray.B110
    COLOR_TEXT_3 = Gray.B90
    COLOR_TEXT_4 = Gray.B80

    COLOR_ACCENT_1 = Red.B20
    COLOR_ACCENT_2 = Red.B40
    COLOR_ACCENT_3 = "#b32216"
    COLOR_ACCENT_4 = Red.B70
    COLOR_ACCENT_5 = Red.B80

    TITLE_BAR_BACKGROUND_COLOR = COLOR_ACCENT_3
    TITLE_BAR_BUTTONS_HOVER_COLOR = COLOR_ACCENT_4
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = COLOR_TEXT_1

    OPACITY_TOOLTIP = 230


class PWRLight(BasePalette):
    COLOR_BACKGROUND_1 = Gray.B140
    COLOR_BACKGROUND_2 = Gray.B130
    COLOR_BACKGROUND_3 = Gray.B120
    COLOR_BACKGROUND_4 = Gray.B110
    COLOR_BACKGROUND_5 = Gray.B100
    COLOR_BACKGROUND_6 = Gray.B90

    COLOR_TEXT_1 = Gray.B10
    COLOR_TEXT_2 = Gray.B20
    COLOR_TEXT_3 = Gray.B50
    COLOR_TEXT_4 = Gray.B70

    COLOR_ACCENT_1 = Red.B130
    COLOR_ACCENT_2 = Red.B100
    COLOR_ACCENT_3 = "#b32216"
    COLOR_ACCENT_4 = Red.B80
    COLOR_ACCENT_5 = Red.B70

    TITLE_BAR_BACKGROUND_COLOR = COLOR_ACCENT_3
    TITLE_BAR_BUTTONS_HOVER_COLOR = COLOR_ACCENT_4
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = Gray.B130

    OPACITY_TOOLTIP = 230


class AIK(BasePalette):
    """A refined, luxury AIK theme for professional interfaces."""

    # Surfaces - The "Black Army" Base
    COLOR_BACKGROUND_1 = "#121212"  # Deep Onyx (Navigation)
    COLOR_BACKGROUND_2 = "#1A1A1B"  # Charcoal (Main Window)
    COLOR_BACKGROUND_3 = "#242426"  # Graphite (Cards/Widgets)
    COLOR_BACKGROUND_4 = "#333333"  # Border/Dividers
    COLOR_BACKGROUND_5 = "#3D3D3E"  # Hovered Items
    COLOR_BACKGROUND_6 = "#4d4d4d"

    # Text - Softened for eye comfort
    COLOR_TEXT_1 = "#EFEAE0"  # Pearl (Primary Text)
    COLOR_TEXT_2 = "#C7C4BD"  # Silver-Gray (Secondary Text)
    COLOR_TEXT_3 = "#8C8A84"  # Muted Gray
    COLOR_TEXT_4 = "#79766e"

    # Accents - The "Gold Standard"
    COLOR_ACCENT_1 = "#8C7343"  # Deep Gold (Success/Active Toggle)
    COLOR_ACCENT_2 = "#A0895B"  # Burnished Gold (Primary Buttons)
    COLOR_ACCENT_3 = "#FFD200"  # Bright Yellow (Critical Alerts Only)
    COLOR_ACCENT_4 = "#ffda33"
    COLOR_ACCENT_5 = "#ffe166"

    # UI Elements
    TITLE_BAR_BACKGROUND_COLOR = "#0D0D0D"  # Darker than body for focus
    TITLE_BAR_BUTTONS_HOVER_COLOR = "#FFD200"
    TITLE_BAR_BUTTONS_DISABLED_COLOR = COLOR_ACCENT_1
    TITLE_BAR_TEXT_COLOR = "#A0895B"  # Gold Title

    OPACITY_TOOLTIP = 245


class Djurgarden(BasePalette):
    """A refined, professional Djurgården theme based on the 1891 colors."""

    # Surfaces - Deep Navy Foundation
    COLOR_BACKGROUND_1 = "#001A3D"  # Deepest Navy (Sidebar)
    COLOR_BACKGROUND_2 = "#002557"  # Secondary Navy (Main BG)
    COLOR_BACKGROUND_3 = "#003366"  # Slightly lighter navy (Cards/Panels)
    COLOR_BACKGROUND_4 = "#004080"  # Hovered surfaces
    COLOR_BACKGROUND_5 = "#7AB2E1"  # The "Stripe" Light Blue (Accents/Borders)
    COLOR_BACKGROUND_6 = "#0E223F"  # Inactive/Muted surface

    # Text - High Legibility
    COLOR_TEXT_1 = "#FFFFFF"  # Primary White
    COLOR_TEXT_2 = "#B0C4DE"  # Light Steel Blue (Secondary text, less eye strain)
    COLOR_TEXT_3 = "#FFD200"  # Yellow for specific highlighted labels
    COLOR_TEXT_4 = "#5C7691"  # Muted blue-gray for disabled text

    # Accents - The "Crest" Palette
    COLOR_ACCENT_1 = "#E31B23"  # The "D.I.F. Red" (Use for Active Tabs/Primary Buttons)
    COLOR_ACCENT_2 = "#7AB2E1"  # Sky Blue (Secondary Buttons/Selection)
    COLOR_ACCENT_3 = "#FFD200"  # Golden Yellow (Attention/Warnings/Highlights)
    COLOR_ACCENT_4 = "#FFE166"  # Lighter yellow for hover
    COLOR_ACCENT_5 = "#990000"  # Darker red for error states

    # Title Bar - The "Gold" Frame influence
    TITLE_BAR_BACKGROUND_COLOR = "#000E21"  # Very dark navy
    TITLE_BAR_BUTTONS_HOVER_COLOR = "#FFD200"  # Yellow glow
    TITLE_BAR_BUTTONS_DISABLED_COLOR = "#5C7691"
    TITLE_BAR_TEXT_COLOR = "#FFFFFF"

    OPACITY_TOOLTIP = 250
