import melee, sys, os

ISO_PATH = os.getenv('ISO_PATH')
SLIPPI_PATH = os.getenv('SLIPPI_PATH')

console = melee.console.Console(
    path=SLIPPI_PATH,
    fullscreen=False
)

controller1 = melee.controller.Controller(
    console,
    port=1,
    type=melee.ControllerType.STANDARD
)

controller2 = melee.controller.Controller(
    console,
    port=2,
    type=melee.melee.ControllerType.STANDARD
)

console.run(iso_path=ISO_PATH)
print("Connecting to console...")
if not console.connect():
    print("ERROR: Failed to connect to the console.")
    sys.exit(-1)
print("Console connected")

print("Connecting controllers to console...")
if not controller1.connect() or not controller2.connect():
    print("ERROR: Failed to connect the controllers.")
    sys.exit(-1)
print("Controllers connected")

gamestate = console.step()


while gamestate.menu_state != melee.Menu.IN_GAME:
    gamestate = console.step()
    if gamestate is None:
        continue

    melee.MenuHelper.menu_helper_simple(
        gamestate=gamestate,
        controller=controller1,
        character_selected=melee.Character.CPTFALCON,
        stage_selected=melee.Stage.BATTLEFIELD,
        connect_code="",
        cpu_level=0,
        costume=0,
        autostart=False,
        swag=False
    )

    melee.MenuHelper.menu_helper_simple(
        gamestate=gamestate,
        controller=controller2,
        character_selected=melee.Character.DK,
        stage_selected=melee.Stage.BATTLEFIELD,
        connect_code="",
        cpu_level=9,
        costume=0,
        autostart=False,
        swag=False
    )