"""
RS 4
zadatak 3
korutine: dohvat podataka o mačkama, dohvat podataka o psima
2024.

"""

import asyncio
import aiohttp


async def get_dog_facts(session) -> list:
    """dohvaćanje podataka o psima"""
    response = await session.get("https://dogapi.dog/api/v2/facts")
    fact_dict = await response.json()
    return fact_dict["data"][0]["attributes"]["body"]


async def get_cat_facts(session) -> list:
    """dohvaćanje podataka o mačkama"""
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return fact_dict["fact"]


async def mix_facts(dog_facts: list, cat_facts: list) -> list:
    """pomiješane činjenice o psima i mačkama, ovisi o duljini"""
    mixed_facts: list = [
        dog_fact if len(dog_fact) > len(cat_fact) else cat_fact
        for dog_fact, cat_fact in zip(dog_facts, cat_facts)
    ]
    return mixed_facts


async def main() -> None:
    """glavna funkcija programa"""
    async with aiohttp.ClientSession() as session:
        cat_fact_tasks = [asyncio.create_task(get_cat_facts(session)) for _ in range(5)]
        dog_fact_tasks = [asyncio.create_task(get_dog_facts(session)) for _ in range(5)]
        dog_cat_facts = await asyncio.gather(*cat_fact_tasks, *dog_fact_tasks)
        cat_facts: list = dog_cat_facts[:4]
        dog_facts: list = dog_cat_facts[5:]
        print("ČINJENICE O PSIMA i MAČKAMA:")
        mixed_dc_facts: list = await mix_facts(dog_facts, cat_facts)
        for fact in mixed_dc_facts:
            print(f"---{fact}")


if __name__ == "__main__":
    asyncio.run(main())
