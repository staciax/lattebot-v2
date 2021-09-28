import discord
import os
from discord.ext import commands

#thanks for stella_bot
def reading_recursive(root: str, /) -> int:
    for x in os.listdir(root):
        if os.path.isdir(x):
            yield from reading_recursive(root + "/" + x)
        else:
            if x.endswith((".py", ".json")):
                with open(f"{root}/{x}" , encoding="utf-8") as r:
                    yield len(r.readlines())


def count_python(root: str) -> int:
    return sum(reading_recursive(root))