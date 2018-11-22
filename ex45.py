# Cave of Wonders Version 2
#
# The game will have different rooms which will be classes.
# At each room you can either go North , South, West, East .
# You can also either Search and Use Item
# The game will also have a combat system.
#
# Object of the game is to get to the island and go through the portal. But you
# can only go to the island on boat, and you have to find the boat with the key.
#
from sys import exit
from random import randint
from textwrap import dedent

class Player(object):

    inventory = []

    def add_inventory(self, item):
        print (dedent("""Adding item to your bag."""))
        self.inventory.append(item)
        print(dedent("""\n You have these items in your bag: \n"""))
        print(self.inventory)

    def remove_inventory(self, item):
        print (dedent("""Removing item from your bag."""))
        self.inventory.remove(item)
        print(dedent("""\n You have these items in your bag: \n"""))
        print(self.inventory)

    def you_see(self, room):

        if not room.items:
            print(" ")
        else:
            print(dedent("You see: "))
            print(", ".join(room.items))

        print("\n")
        print("Obvious exits:")
        print(", ".join(room.exits))





class Scene(object):

    def enter (self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):

#engine should have all the scenes in the game
    def __init__(self, scene_map):

        self.scene_map = scene_map
        # print(">> after self.scene_map = scene_map = ", scene_map)
        # print(">> before self.scene_map = ", self.scene_map)

    def play(self):
        # print(">>> play")

        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        # print("^^ before while current_scene=", current_scene, "last_scene= ", last_scene)
        while current_scene != last_scene:
            # print("^ top of while current_scene=", current_scene, "last_scene= ", last_scene)


            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            # print("^ end of while current_scene=", current_scene, "last_scene= ",
            #     last_scene, "next_scene_name = ", next_scene_name)

        #be sure to print out the last scene
        # print("<<<<< end of play: current_scene= ", current_scene)
        current_scene.enter()



class Death(Scene):

    death_sentences = [
        "You died. You're not really good at this.",
        "Maybe, you're just not cut out for this.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes.",
        "Dam, you just have bad luck.",
        "Sometimes you win, sometimes you lose.",
    ]

    def enter(self):
        print(Death.death_sentences[randint(0,len(self.death_sentences)-1)])
        exit(1)

class CaveOpening(Scene):

    exits = ['south']

    items = ['rocks', 'twigs']

    def enter(self):
        print(dedent("""
            This is a large cave opening, and the ceiling is very high.
            The cave is very dark, and there are large and small boulders around
            the area. There are many small rocks, and twigs around. Some burnt
            marks are visible throughout the floor.

            Sounds of water dripping premeate throughout the cave. Animal noises
            are heard all over the place.

            To the south, there is an opening.
        """))


        a_player.you_see(CaveOpening)
        action = input("> ")

        if action == "go south" or action == "south":

            return 'damp_wet_area'

        elif action =="take rocks":
            a_player.add_inventory('rocks')
            self.items.remove('rocks')
            return 'cave_opening'

        elif action =="take twigs":
            a_player.add_inventory('twigs')
            self.items.remove('twigs')
            return 'cave_opening'

        else:
            print("DOES NOT COMPUTE!")
            return 'cave_opening'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'

class DampWetArea(Scene):

    items = []
    exits = ['north', 'east', 'south']

    def enter(self):
        print(dedent("""
            A damp wet area, with large ceiling. It is illuminated by
            a blue light. The light seems to be coming from flowers that are
            growing from the ceiling.  There are puddles all over this area,
            the sound of water dripping permeates through the whole area.
        """))

        a_player.you_see(DampWetArea)

        action = input("> ")

        if action == "go north" or action == "north":
            return 'cave_opening'

        elif action == "go east" or action == "east":
            return 'long_tall_grass'

        elif action == "go south" or action == "south":
            return 'beach'

        else:
            print("YOU CAN'T DO THAT!")
            return 'damp_wet_area'


class LongTallGrass(Scene):

    items = []
    exits = ['north', 'south', 'west', 'east']

    def enter(self):
        print(dedent("""
            Long tall grass is everywhere. The sounds of cicadas are in the
            background. It is very breezy as the wind is blowing. It is night
            time and there are thousands of stars in the sky. It looks like the
            milkyway. To the north there seems to be a large forest.
            To the south, there seems to be a door in the middle of the field.
            And directly east seems to be another small opening to another area.
        """))

        a_player.you_see(LongTallGrass)

        action = input("> ")

        if action == "go north" or action == "north":
            return 'forest'

        elif action == "go east" or action == "east":
            return 'western_town'

        elif action == "go south" or action == "south":
            return 'space'

        elif action == "go west" or action == "west":
            return 'damp_wet_area'

        else:
            print("YOU CAN'T DO THAT!")
            return 'long_tall_grass'


class Beach(Scene):
    items = ['boat']
    exits = ['north']

    def enter(self):
        print(dedent("""
            There is a large vast beach, the extends to the horizon. It is very
            surprising, because the cave entrance in the beginning was 5 kms
            below the surface. It is strange that there is a beach here.  In the
            distance, there is the sunset. In the distance, there is an island with
            a lighthouse.

            At the bottom of the light house, there is a blue shining portal.
            The beach has a small boat, near the shore. It looks like it could be
            used to go to the small island.
        """))

        a_player.you_see(Beach)

        action = input("> ")


        if action == "go north" or action == "north":
            return 'damp_wet_area'


        elif (action == "use boat" or action == "boat" or action == "take boat")\
         and ('boat key' in a_player.inventory) :

            print(dedent("""
                The boat looks pretty old, but it seems to have a motor. You put
                the boat key into the ignition and it starts the motor. You take the
                boat to the small island in the distance.

            """))
            return 'small_island'

        elif (action == "use boat" or action == "boat" or action == "take boat")\
         and ('boat key' not in a_player.inventory):
            print(dedent("""
                YOU DON'T HAVE THE BOAT KEY!. So you can't turn on the boat engine.
                You need to find the boat key.
            """))
            return 'beach'






        else:
            print("YOU CAN'T DO THAT!")
            return 'beach'




class Forest(Scene):
    items = []
    exits = ['south']
    forest_animals = 'alive'
    def enter(self):
        print(dedent("""
            The forest is lit up with many trees that have leaves that glow in
            the dark. The sky is dark, and there are millions of stars in the
            sky. It looks like the milky way but instead of band of stars, you
            see a spirling pinwheel shape of all the stars.
        """))
        if self.forest_animals == "alive":
            print(dedent("""
                You hear the sound of a large roar and thousands of rumbling
                footsteps, in the distance there are figures of animals rushing
                towards you. If only, you had a large weapon or something to use.
            """))
        else:
            print(dedent("""
            """))


        a_player.you_see(Forest)

        action = input("> ")



        if action == "go south" or action == "south":
            return 'long_tall_grass'

        elif action == "use rocket launcher" and 'rocket launcher' in a_player.inventory:
            print(dedent("""
                You take out out the rocket launcher from your bag, and shoot
                in the direction of the stampede of animals. The animals explode
                into pieces.
            """))
            self.forest_animals =='dead'

        else:
            (print(dedent("""
                You try to hide behind a tree, but the animals are too many, and
                they stampede you to death.
            """)))
            return 'death'




class Space(Scene):
    items = []
    exits = ['north', 'east']

    def enter(self):
        print(dedent("""
            The earth is rotating slowly below. In the distance, the sun is
            shining brightly. You feel weightlessness, and can for some reason
            can still breathe. The view is majestic, knowing that humans live
            on such a planet. There are no borders, no countries, just one planet.

            There seems to be two portals. One, is where you can see the field with the
            tall grass. The other, is where you can see buddist statutes.
        """))

        a_player.you_see(Space)

        action = input("> ")

        if action == "go north" or action == "north":
            return 'long_tall_grass'

        elif action == "go east" or action == "east":
            return 'buddist_temple'

        else:
            print("YOU CAN'T DO THAT!")
            return 'space'


class WesternTown(Scene):
    items = []
    exits = ['north west', 'north east', 'south west', 'south east', 'west']

    def enter(self):
        print(dedent("""
            There is a large town, and looks like an old western town in those
            old western movies. There are several buildings in this town. One
            has a large drink billboard, looks like its a bar. There is another
            building that has guns lined up in the windows, looks like a weapons
            shop.  There is a small house that is painted purple . And finally,
            there is a toy house at the end of the street. In the windows of the
            toy house, you see many toys being sold.
        """))

        a_player.you_see(WesternTown)

        action = input("> ")

        if action == "go north west" or action == "north west":
            return 'bar'

        elif action == "go north east" or action == "north east":
            return 'weapons_shop'

        elif action == "go south west" or action == "south west":
            return 'purple_house'

        elif action == "go south east" or action == "south east":
            return 'toy_shop'

        else:
            print("YOU CAN'T DO THAT!")
            return 'western_town'


class Bar(Scene):
    items = ['beer', 'wine', 'coke', 'water']
    exits = ['south']

    def enter(self):
        print(dedent("""
            The bar is empty.  There looks like several bottles on the bar table,
            and there are numerous tables and chairs around. The place smells
            pretty old. At the main counter, there is a cup of beer, wine, coke
            and water.
        """))

        a_player.you_see(Bar)

        action = input("> ")

        if action == "go south" or action == "south":
            return 'western_town'

        elif (action == "drink beer") or (action == "drink wine") \
            or (action == "drink coke") or action == "drink water":
            print(dedent("""
                You take a sip, and realize that its old. You start to feel
                really sick, and cough out blood.  Suddenly, you feel kinda of
                dizzy. And you fall and hit your head on the table and die.
            """))
            return 'death'

        else:
            print("YOU CAN'T DO THAT!")
            return 'bar'


class PurpleHouse(Scene):
    items = ['boat key', 'envelope', 'weird wooden figure']
    exits = ['north', 'south']

    def enter(self):
        print(dedent("""
            It's a normal looking house on the inside.
            You see the kitchen, and also the living room. You walk around the
            house, and see some pictures of a man in his 40s on a boat with his
            two daughters.

            There's also a table right next to the front door.

            On the table, there are some items. You see a boat key, envelope,
            a weird wooden figure.

            There are two doors that you can see. The door to the south, you can see
            a buddist temple, and the door to the north, you can see the western town.
        """))

        a_player.you_see(PurpleHouse)

        action = input("> ")

        if action == "go north" or action == "north":
            return 'western_town'

        elif action == "go south" or action == "south":
            return 'buddist_temple'

        elif action == "take boat key" :
            a_player.add_inventory('boat key')
            self.items.remove('boat key')
            return 'purple_house'

        elif action == "take envelope" :
            a_player.add_inventory('envelope')
            self.items.remove('envelope')
            return 'purple_house'

        elif action == "take weird wooden figure" :
            a_player.add_inventory('weird wooden figure')
            self.items.remove('weird wooden figure')
            return 'purple_house'



        else:
            print("YOU CAN'T DO THAT!")
            return 'purple_house'


class BuddistTemple(Scene):
    items = []
    exits = ['north', 'south', 'west', 'east']

    def enter(self):
        print(dedent("""
            The buddist statutes are painted with a red colour. And they look really creepy.
            The entrance of the buddist temple is very large, and the opening reaches to the ceiling.
            The buddist temple is very traditional, there seems to be a monk kneeling
            in front of a large budda statute with his back facing you.

            Maybe you should talk to the monk.
        """))

        a_player.you_see(BuddistTemple)

        action = input("> ")

        if action == "go north" or action == "north":
            return 'purple_house'

        elif action == "go west" or action == "west":
            return 'space'

        elif action == "talk to the monk" or action == "talk monk" or action == "talk to monk":
            print(dedent("""
                You say 'Hello', and the monk turns around with alarm and surprise on his
                face. He yells 'You should not be here, GRASP HEART!'.
                You feel a tightness in your chest, and start to feel weak
                in the knees. You collapse and die.
            """))
            return 'death'

        else:
            print("YOU CAN'T DO THAT!")
            return 'buddist_temple'


class WeaponsShop(Scene):
    items = ['rocket launcher']
    exits = ['south']

    def enter(self):
        print(dedent("""
            There are several weapons hanging from the wall. There is only one
            that looks like it still works. It is the rocket launcher.
        """))

        a_player.you_see(WeaponsShop)

        action = input("> ")

        if action == "go south" or action == "south":
            return 'western_town'

        elif action == "take rocket launcher":
            print(dedent("""
                You take the rocket launcher, and it is suprisingly light.
            """))

            a_player.add_inventory('rocket launcher')
            self.items.remove('rocket launcher')
            return 'weapons_shop'

        else:
            print("YOU CAN'T DO THAT!")
            return 'weapons_shop'


class ToyShop(Scene):
    items = ['toy car', 'toy bear', 'toy sword']
    exits = ['north']

    def enter(self):
        print(dedent(f"""
            The toy store looks abandoned and old. There are broken tables, and
            broken pieces of toys scattered on the floor. The toys that are whole
            are only a few.

        """))

        a_player.you_see(ToyShop)

        action = input("> ")

        if action == "go north" or action == "north":
            return 'western_town'


        else:
            print("YOU CAN'T DO THAT!")
            return 'toy_shop'


class SmallIsland(Scene):


    def enter(self):
        print(dedent("""
            The island is very quiet. You reach the portal, and go through it .

            You are finally at the entrance of the cave, where you started.
            The whole experience was crazy, and noone will believe you.  You
            vowed to write a story about it, and call it :

            THE CAVE OF WONDERS.

        """))
        return 'finished'


class Map(object):

    scenes = {
        'cave_opening': CaveOpening(),
        'damp_wet_area': DampWetArea(),
        'long_tall_grass': LongTallGrass(),
        'beach': Beach(),
        'forest': Forest(),
        'space': Space(),
        'western_town': WesternTown(),
        'bar': Bar(),
        'purple_house': PurpleHouse(),
        'buddist_temple': BuddistTemple(),
        'weapons_shop': WeaponsShop(),
        'toy_shop': ToyShop(),
        'small_island': SmallIsland(),
        'death': Death(),

        'finished': Finished(),

    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_map = Map('cave_opening')
a_game = Engine(a_map)
a_player = Player()
a_game.play()


