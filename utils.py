from entities.entity_type import EntityType
from entities.snake import Snake
from entities.ladder import Ladder

class Utils:
    def load_entity(filepath,entity_type):
        entities = []
        with open(filepath,'r') as f:
            lines = f.readlines()
            for line in lines:
                start, end = line.split(' ')
                if entity_type==EntityType.SNAKE:
                    entities.append(Snake(int(start),int(end)))
                if entity_type==EntityType.LADDER:
                    entities.append(Ladder(int(start),int(end)))
        return entities