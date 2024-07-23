from special_entity import SpecialEntity
from entity_type import EntityType

class Snake(SpecialEntity):
    def __init__(self,start,end) -> None:
        super().__init__(start,end)
        self._entity_type = EntityType.SNAKE