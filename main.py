import bot_manager


def main():
    bot_manager.bot.run(bot_manager.settings['token'])


if __name__ == '__main__':
    main()
