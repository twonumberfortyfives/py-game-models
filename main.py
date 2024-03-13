import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open('players.json') as config_file:
        config = json.load(config_file)
    for nickname, user_data in config.items():
        user_guild = Guild.objects.create(
            name=user_data['guild']['name'],
            description=user_data['guild']['description']
        )
        user_race = Race.objects.create(
            name=user_data['race']['name'],
            description=user_data['race']['description']
        )
        Player.objects.create(
            nickname=nickname,
            email=user_data['email'],
            bio=user_data['bio'],
            guild_id=user_guild.id,
            race_id=user_race.id,
        )
        user_skill = Skill.objects.create(
            name=user_race['skills']['race'],
            bonus=user_race['skills']['bonus'],
            race_id=user_race.id
        )


if __name__ == "__main__":
    main()
