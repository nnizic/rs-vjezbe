"""
RS 4
zadatak 2
2 korutine: dohvata podataka o mačkama, filter podataka koji sadrže cat ili cats
2024.

"""

import asyncio
import aiohttp


async def get_cat_facts(session) -> list:
    """dohvaćanje podataka o mačkama"""
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return fact_dict["fact"]


async def filter_cat_facts(fact_list: list) -> list:
    """filtriranje riječi cat/s iz liste"""
    result: list = [macka for macka in fact_list if "cat" in macka.lower()]
    return result


async def main() -> None:
    """glavna funkcija programa"""
    async with aiohttp.ClientSession() as session:
        cat_fact_tasks = [
            asyncio.create_task(get_cat_facts(session)) for _ in range(20)
        ]
        actual_cat_facts = await asyncio.gather(*cat_fact_tasks)
        macke: list = await filter_cat_facts(actual_cat_facts)
        print("ČINJENICE O MAČKAMA:")
        for macka in macke:
            print(f"---{macka}")


if __name__ == "__main__":
    asyncio.run(main())
