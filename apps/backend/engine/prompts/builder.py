from engine.providers.ltx import LTXProvider
from engine.providers.wan import WANProvider

providers = {
    "ltx": LTXProvider(),
    "wan": WANProvider()
}

def generate(provider:str,scene,camera):

    return providers[provider].build_prompt(scene,camera)
