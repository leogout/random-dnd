import enum
from functools import lru_cache

import json
from typing import Annotated, Union

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from openai import OpenAI
from pydantic import BaseModel
from config import get_settings 

app = FastAPI()

class Race(str, enum.Enum):
    DWARF = "dwarf"
    ELF = "elf"
    HALFLING = "halfling"
    HUMAN = "human"
    GNOME = "gnome"
    HALF_ORC = "half-orc"

class Languages(str, enum.Enum):
    FRENCH = "french"
    ENGLISH = "english"

class Character(BaseModel):
    race: Race
    

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/character")
def read_root(race: Annotated[Race, Query()], language: Annotated[Languages, Query()]):
    client = OpenAI(
        api_key=get_settings().openai_api_key,
    )
    
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": 
f"""You aren't in a conversation with someone. Act like a REST API returning pure JSON, without any formatting. Answer in {language}.
You are a REST API route that generates dungeons and dragons characters. They always have the following attributes:
race
full_name
gender
description (a description of how they look at the moment)
attitude (how they act towards the players)
loot (a list of items with a name and a description)
quest (a quest that this character could give to the players)"""
            },
            {
                "role": "user",
                "content": f"Generate a {race}"
            }
        ]
    )
    
    return json.loads(completion.choices[0].message.content)
