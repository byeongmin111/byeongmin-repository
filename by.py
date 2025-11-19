from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()




player = FirstPersonController(speed=20)
player.y = 3


score = 0
score_text = Text(text=f'score: {score}', position=(-0.85, 0.45), scale=2)


ground = Entity(
    model='plane',
    scale=100,
    position=(0, 0, 0),
    collider='mesh',
    texture='grass'
)


sky=Sky()


block = Entity(
    model='cube',
    scale=2,
    color=color.gold,
    position=(0, 1, 20),
    collider='box'
)


def block1():
    X=random.randint(-20, 20)
    Z=random.randint(-20, 20)
    new_block = Entity(
        model='cube',
        scale=2,
        color=color.gold,
        position=(X, 1, Z),
        collider='box'
    )
    return new_block


def input(key):
    global score, block
    if key == 'escape':
        app.quit()
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=10, traverse_target=scene)
        if hit_info.hit and hit_info.entity == block:
            destroy(block)
            score += 1
            score_text.text = f'score: {score}'
            block = block1()

            
            
app.run()



        




      







       
