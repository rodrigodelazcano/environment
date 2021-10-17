from pdb import set_trace as T
import numpy as np
from tqdm import tqdm

from neural_mmo.forge.trinity.env import Env
from neural_mmo.forge.trinity.scripted import baselines

from projekt.config import SmallMultimodalSkills, Debug

DEV_AGENTS  = [baselines.Prospector, baselines.Hunter, baselines.Fisher, baselines.Carver, baselines.Alchemist, baselines.CombatExchange]

#config         = SmallMultimodalSkills()
config         = Debug()
config.AGENTS  = DEV_AGENTS
config.NMOB = 32
config.NENT = 32
config.EVALUTE = True
#config.RENDER  = True

env = Env(config)

env.reset()
for _ in range(256):
   env.render()
   env.step({})

logs = env.quill.packet
for key, vals in logs['Stats'].items():
    print('{}: {}'.format(key, np.mean(vals)))
