import os
from sonic_platform_base.sonic_thermal_control.thermal_manager_base import ThermalManagerBase
from sonic_platform_base.sonic_thermal_control.thermal_policy import ThermalPolicy
from sonic_platform.thermal_actions import *
from sonic_platform.thermal_conditions import *
from sonic_platform.thermal_infos import *


class ThermalManager(ThermalManagerBase):
    @classmethod
    def initialize(cls):
        """
        Initialize thermal manager, including register thermal condition types and thermal action types
        and any other vendor specific initialization.
        :return:
        """
        return True

    @classmethod
    def deinitialize(cls):
        """
        Destroy thermal manager, including any vendor specific cleanup. The default behavior of this function
        is a no-op.
        :return:
        """
        return True
