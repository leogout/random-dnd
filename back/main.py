import json
from typing import Annotated

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from mistralai import Mistral

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from model import Race, Languages
from config import get_settings
import logging

app = FastAPI()

# Database setup
settings = get_settings()

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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

logger = logging.getLogger('uvicorn.error')

@app.get("/v1/liveness", status_code=200)
def liveness():
    pass


@app.get("/v1/readiness", status_code=200)
def readiness():
    pass


@app.get("/api/v1/db-check")
def db_check():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        return {"status": "ok"}
    except Exception as e:
        logger.error(e)
        return {"status": "error"}
    finally:
        db.close()


@app.get("/character")
def read_root(race: Annotated[Race, Query()], language: Annotated[Languages, Query()]):
    client = Mistral(
        api_key=get_settings().llm_api_key,
    )

    logger.info(f"Generating a {race} character...")

    quest_format = """
    {
        "race": "The race that the user gave you",
        "full_name": "The full name of the character",
        "gender": "The gender of the character",
        "description": "A description of how they look at the moment, be creative",
        "attitude": "How they act towards the players",
        "loot": [{
            "name": "The name of the item",
            "description": "The description of the item",
        }],
        "quest": "A quest that this character could give to the players"
    }
    """

    response = client.chat.complete(
        model=get_settings().llm_agent_name,
        messages=[
            {
                "role": "system", 
                "content": 
f"""You aren't in a conversation with someone. Act like a REST API returning pure JSON, without any formatting. No markdown. Answer in {language}.
Be random and original.
You are a REST API route that generates dungeons and dragons characters. They must respect the following format :
{quest_format}
"""
            },
            {
                "role": "user",
                "content": f"Generate a {race}"
            }
        ]
    )

    logger.info(response)
    
    return json.loads(response.choices[0].message.content)
