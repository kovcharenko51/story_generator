import pytest
import bot_manager
import story_creator


TEST_STORY = "Test story"


class Context:
    def __init__(self):
        self.text = ""
        self.tts = False

    async def send(self, *args, **kwargs):
        self.text = args[0]
        self.tts = kwargs['tts']


@pytest.mark.asyncio
async def test_text_message(monkeypatch):
    monkeypatch.setattr(story_creator, 'gen_story', lambda: TEST_STORY)
    context = Context()
    await bot_manager.story(context)
    assert context.text == TEST_STORY


@pytest.mark.asyncio
async def test_tts_message(monkeypatch):
    monkeypatch.setattr(story_creator, 'gen_story', lambda: TEST_STORY)
    context = Context()
    await bot_manager.read(context)
    assert context.text == TEST_STORY
    assert context.tts is True


@pytest.mark.asyncio
async def test_file_write(monkeypatch, tmp_path):
    context = Context()
    path_to_file = tmp_path / "base.txt"
    print(path_to_file)
    monkeypatch.setattr(bot_manager, 'path_to_file', path_to_file)
    await bot_manager.tell(context, TEST_STORY)
    with open(path_to_file, "r") as base_file:
        assert base_file.read() == TEST_STORY + "\n"
    assert context.text == "Ахахахахаха. Смешно"

