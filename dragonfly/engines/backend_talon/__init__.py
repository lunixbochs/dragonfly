#
# This file is part of Dragonfly.
# (c) Copyright 2007, 2008 by Christo Butcher
# Licensed under the LGPL.
#
#   Dragonfly is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Dragonfly is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with Dragonfly.  If not, see
#   <http://www.gnu.org/licenses/>.
#

"""
SR back-end package for Talon
============================================================================

"""


# Module level singleton instance of this engine implementation.
_engine = None


def is_engine_available(**kwargs):
    """
        Check whether Talon is available.

        :param \\**kwargs: optional keyword arguments passed through to the
            engine for engine-specific configuration.
    """
    import talon.experimental.dragonfly
    return True


def get_engine(**kwargs):
    """
        Retrieve the Talon back-end engine object.

        :param \\**kwargs: optional keyword arguments passed through to the
            engine for engine-specific configuration.
    """
    global _engine
    if not _engine:
        from .engine import TalonEngine
        _engine = TalonEngine(**kwargs)
    return _engine