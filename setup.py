import cx_Freeze

executables = [cx_Freeze.Executable("Serpent.py")]

cx_Freeze.setup(
    name="Veg Serpent",
    options = {"build_exe":{"packages":["pygame"],"include_files":["apple.png","snakehead.png","snake_cup.png"]}},
    description = "Veg Serpent Tutorial",
    executables = executables
    )
