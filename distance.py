# The distances aren't accurate due to the elliptical nature of the orbits
# I've added the average distance between the objects
distance_from_objects = {
    "Earth": { # Distance to object from Earth
        "Sun": 92955807,
        "Moon": 238855,
        "Mercury": 35983610,
        "Venus": 67417330,
        "Mars": 141633260,
        "Jupiter": 483632810,
        "Saturn": 888188000,
        "Uranus": 1783950000,
        "Neptune": 2799658100,
        "Pluto": 3670529300
    },
    "Moon": { # Distance to object from the Moon
        "Sun": 92955807,
        "Earth": 238855,
        "Mercury": 36189210,
        "Venus": 67362980,
        "Mars": 141394160,
        "Jupiter": 483393690,
        "Saturn": 887939145,
        "Uranus": 1783681145,
        "Neptune": 2799380245,
        "Pluto": 3670250445
    },
    "Sun": { # Distance to object from the Sun
        "Earth": 92955807,
        "Moon": 92955807,
        "Mercury": 34269640,
        "Venus": 67234910,
        "Mars": 145936640,
        "Jupiter": 462367930,
        "Saturn": 900702440,
        "Uranus": 1818373240,
        "Neptune": 2776948840,
        "Pluto": 3650321600
    },
    "Mercury": { # Distance to object from Mercury
        "Earth": 35983610,
        "Moon": 36189210,
        "Sun": 34269640,
        "Venus": 31193830,
        "Mars": 105944900,
        "Jupiter": 447952450,
        "Saturn": 847670100,
        "Uranus": 1748551000,
        "Neptune": 2740012700,
        "Pluto": 3611387900
    },
    "Venus": { # Distance to object from Venus
        "Earth": 67417330,
        "Moon": 67362980,
        "Sun": 67234910,
        "Mercury": 31193830,
        "Mars": 75311070,
        "Jupiter": 414019760,
        "Saturn": 798007120,
        "Uranus": 1652436200,
        "Neptune": 2635648000,
        "Pluto": 3506150200
    },
    "Mars": { # Distance to object from Mars
        "Earth": 141633260,
        "Moon": 141394160,
        "Sun": 145936640,
        "Mercury": 105944900,
        "Venus": 75311070,
        "Jupiter": 374262870,
        "Saturn": 709573000,
        "Uranus": 1529667100,
        "Neptune": 2525918700,
        "Pluto": 3391038500
    },
    "Jupiter": { # Distance to object from Jupiter
        "Earth": 483632810,
        "Moon": 483393690,
        "Sun": 462367930,
        "Mercury": 447952450,
        "Venus": 414019760,
        "Mars": 374262870,
        "Saturn": 400757000,
        "Uranus": 960944100,
        "Neptune": 1919732200,
        "Pluto": 2802621100
    },
    "Saturn": { # Distance to object from Saturn
        "Earth": 888188000,
        "Moon": 887939145,
        "Sun": 900702440,
        "Mercury": 847670100,
        "Venus": 798007120,
        "Mars": 709573000,
        "Jupiter": 400757000,
        "Uranus": 741131700,
        "Neptune": 1492880200,
        "Pluto": 2390430000
    },
    "Uranus": { # Distance to object from Uranus
        "Earth": 1783950000,
        "Moon": 1783681145,
        "Sun": 1818373240,
        "Mercury": 1748551000,
        "Venus": 1652436200,
        "Mars": 1529667100,
        "Jupiter": 960944100,
        "Saturn": 741131700,
        "Neptune": 1357636500,
        "Pluto": 1247684500
    },
    "Neptune": { # Distance to object from Neptune
        "Earth": 2799658100,
        "Moon": 2799380245,
        "Sun": 2776948840,
        "Mercury": 2740012700,
        "Venus": 2635648000,
        "Mars": 2525918700,
        "Jupiter": 1919732200,
        "Saturn": 1492880200,
        "Uranus": 1357636500,
        "Pluto": 1146619500
    },
    "Pluto": { # Distance to object from Pluto
        "Earth": 3670529300,
        "Moon": 3670250445,
        "Sun": 3650321600,
        "Mercury": 3611387900,
        "Venus": 3506150200,
        "Mars": 3391038500,
        "Jupiter": 2802621100,
        "Saturn": 2390430000,
        "Uranus": 1247684500,
        "Neptune": 1146619500
    }
}