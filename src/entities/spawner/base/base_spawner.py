from abc import ABC

from  entities.spawner.interfaces import ISpawner


class BaseSpawner(ISpawner, ABC):
    def __init__(self, manager: 'GameFlowManager'):
        self.manager = manager
