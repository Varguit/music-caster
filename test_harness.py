from helpers import *
from helpers import get_metadata
from shared import is_already_running, get_running_processes
from music_caster import settings


MUSIC_FILE_WITH_ALBUM_ART = r"C:\Users\maste\OneDrive\Music\6ixbuzz, Pressa, Houdini - Up & Down.mp3"
TEST_MUSIC_FILES = [
    r'C:\Users\maste\OneDrive\Music\deadmau5 - My Pet Coelacanth.mp3',
    r'C:\Users\maste\OneDrive\Music\deadmau5 - Not Exactly.mp3',
    r"C:\Users\maste\OneDrive\Music\deadmau5 - Phantoms Can't Hang.mp3",
    r'C:\Users\maste\OneDrive\Music\deadmau5 - Rio.mp3',
    r'C:\Users\maste\OneDrive\Music\deadmau5 - SATRN.mp3',
    r'C:\Users\maste\OneDrive\Music\deadmau5 - Saved.mp3',
    r'C:\Users\maste\OneDrive\Music\deadmau5 - Slip.mp3',
    r'C:\Users\maste\OneDrive\Music\deadmau5 - So There I Was.mp3',  # DNE
    r'C:\Users\maste\OneDrive\Music\deadmau5 - Sofi Needs a Ladder.mp3',
    r'C:\Users\maste\OneDrive\Music\deadmau5 - Some Kind of Blue.mp3',
    r'C:\Users\maste\OneDrive\Music\deadmau5 - Sometimes Things Get, Whatever.mp3',
    r'C:\Users\maste\OneDrive\Music\deadmau5 - Three Pound Chicken Wing.mp3',
    r'C:\Users\maste\OneDrive\Music\deadmau5 & Kaskade - I Remember.mp3',
    r'C:\Users\maste\OneDrive\Music\deadmau5, Grabbitz - Let Go.mp3',
    r'C:\Users\maste\OneDrive\Music\Diplo, Trippie Redd - Wish.mp3',
    r'C:\Users\maste\OneDrive\Music\Dirty South, Alesso, Ruben Haze - City Of Dreams.mp3',
    r"C:\Users\maste\OneDrive\Music\Dogzilla - Without You (John O'Callaghan Extended Remix).mp3",
    r'C:\Users\maste\OneDrive\Music\Dogzilla - Without You (Ronald van Gelderen Extended Remix).mp3',
    r'C:\Users\maste\OneDrive\Music\Dogzilla - Without You (Will Atkinson Remix).mp3',
    r"C:\Users\maste\OneDrive\Music\Drake - Hold On, We're Going Home.mp3",
    r'C:\Users\maste\OneDrive\Music\Drake - Over (Ayobi Remix).mp3',
    r'C:\Users\maste\OneDrive\Music\Drake - Passionfruit.mp3'
]

LIST_TO_NAT_SORT_1 = ['1. Hello World', '3. Hello World', '10. Hello World', '2. Hello World', '9. Hello World',
                      '11. Hello World', '12. Hello World']
LIST_TO_NAT_SORT_2 = ['C:/Users/maste/OneDrive/Music/1. Hello World', 'C:/Users/maste/OneDrive/Music/3. Hello World',
                      'C:/Users/maste/OneDrive/Music/10. Hello World', 'C:/Users/maste/OneDrive/Music/2. Hello World',
                      'C:/Users/maste/OneDrive/Music/9. Hello World', 'C:/Users/maste/OneDrive/Music/11. Hello World',
                      'C:/Users/maste/OneDrive/Music/12. Hello World']
NAT_SORTED_LIST_1 = ['1. Hello World', '2. Hello World', '3. Hello World', '9. Hello World', '10. Hello World',
                     '11. Hello World', '12. Hello World']
NAT_SORTED_LIST_2 = ['C:/Users/maste/OneDrive/Music/1. Hello World', 'C:/Users/maste/OneDrive/Music/2. Hello World',
                     'C:/Users/maste/OneDrive/Music/3. Hello World', 'C:/Users/maste/OneDrive/Music/9. Hello World',
                     'C:/Users/maste/OneDrive/Music/10. Hello World', 'C:/Users/maste/OneDrive/Music/11. Hello World',
                     'C:/Users/maste/OneDrive/Music/12. Hello World']

GET_METADATA_FROM = [
        r'C:\Users\maste\OneDrive\Music\$teven Cannon - Inxanity.mp3',
        r'C:\Users\maste\OneDrive\Music\6ixbuzz, Pressa, Houdini - Up & Down.mp3',
        r'C:\Users\maste\OneDrive\Music\88GLAM, Lil Yachty - Lil Boat.mp3',
        r'C:\Users\maste\OneDrive\Music\Adam K & Soha - Twilight.mp3'
    ]
EXPECTED_METADATA = [
    {'album': 'Inxanity', 'artist': '$teven Cannon', 'explicit': True, 'sort_key': 'inxanity - $teven cannon',
     'title': 'Inxanity', 'track_number': '1'},
    {'album': '6ixupsidedown', 'artist': '6ixbuzz, Pressa, Houdini', 'explicit': True, 'title': 'Up & Down',
     'sort_key': 'up & down - 6ixbuzz, pressa, houdini', 'track_number': '1'},
    {'album': '88GLAM2.5', 'artist': '88GLAM, Lil Yachty', 'explicit': True, 'title': 'Lil Boat',
     'sort_key': 'lil boat - 88glam, lil yachty', 'track_number': '6'},
    {'album': 'Rebirth Classics - Ibiza', 'artist': 'Adam K & Soha', 'explicit': False, 'title': 'Twilight',
     'sort_key': 'twilight - adam k & soha', 'track_number': '4'}
]
EXPECTED_FIRST_ARTIST = ['$teven Cannon', '6ixbuzz', '88GLAM', 'Adam K & Soha']


def test_helpers():

    print('DISPLAY LANGUAGE', get_display_lang())
    for code in ('en', 'es'):
        assert get_lang_pack(code)

    for line in get_lang_pack('en'):
        for code in ('en', 'es', 'de'):
            get_translation(line, code)
    # test get length
    for file in TEST_MUSIC_FILES:
        try:
            assert get_length(file) > 0
        except InvalidAudioFile:
            assert not os.path.exists(file)
    for file in ('audio_player.py', 'file.mp4', 'README.txt'):
        with suppress(InvalidAudioFile):
            # should raise an error but not crash program
            get_length(file)

    LIST_TO_NAT_SORT_1.sort(key=natural_key_file)
    LIST_TO_NAT_SORT_2.sort(key=natural_key_file)
    assert LIST_TO_NAT_SORT_1 == NAT_SORTED_LIST_1
    assert LIST_TO_NAT_SORT_2 == NAT_SORTED_LIST_2

    for code in ('#fff', '#ffffff', '#aaa', '#abc', '#999', '#000', '#010', '#000000', '#999999', '#aaaaaa'):
        assert valid_color_code(code)

    for code in ('fff', '000', 'abcdef', '999999', '.', 'czc/z', '#...', '#/.;ads', '#fff.aa', '#999999a', '#ggg'):
        assert not valid_color_code(code)

    for file, expected_metadata in zip(GET_METADATA_FROM, EXPECTED_METADATA):
        try:
            assert get_metadata(file) == expected_metadata
        except AssertionError as e:
            print('TEST FAILED:', file, get_metadata(file), 'vs.', expected_metadata)
            raise e

    if platform.system() == 'Windows':
        assert fix_path('C:/Users/maste/OneDrive') == r'C:\Users\maste\OneDrive'
    assert fix_path(r'C:\Users\maste\OneDrive', False) == 'C:/Users/maste/OneDrive'

    for file, expected_first_artist in zip(GET_METADATA_FROM, EXPECTED_FIRST_ARTIST):
        try:
            assert get_first_artist(get_metadata(file)['artist']) == expected_first_artist
        except AssertionError:
            print('TEST FAILED', get_first_artist(file), '!=', expected_first_artist)
            raise AssertionError

    print('get_ipv4():', get_ipv4())
    assert get_ipv4().count('.') == 3

    print('get_mac():', get_mac())
    assert get_mac().count(':') == 5

    test_better_shuffle = list(range(10000))
    better_shuffle(test_better_shuffle, 1, -2)
    assert test_better_shuffle[0] == 0
    assert test_better_shuffle[-1] == 9999

    assert isinstance(create_qr_code('2001'), str)
    for process in get_running_processes():
        assert len(process) == 5
        assert isinstance(process['pid'], int)
    assert isinstance(is_already_running(), bool)
    for file in ('.mp3', '.flac', '.m4a', '.mp4', '.aac', '.mpeg', '.ogg', '.opus', '.wma', '.wav'):
        assert valid_audio_file(file)

    for youtube_link in {'https://youtu.be/Dlxu28sQfkE',
                         'https://www.youtube.com/watch?v=Dlxu28sQfkE&feature=youtu.be',
                         'https://www.youtube.com/watch/Dlxu28sQfkE',
                         'https://www.youtube.com/embed/Dlxu28sQfkE',
                         'https://www.youtube.com/v/Dlxu28sQfkE',
                         'https://www.youtube.com/playlist?list=PLRbcUrcJVEmX_eaAsubNOWfE4SlhGqjW4'}:
        try:
            assert parse_youtube_id(youtube_link)
        except AssertionError:
            print('TEST FAILED', youtube_link)
            raise AssertionError

    for option, expected in {None: (REPEAT_OFF_IMG, gt('Repeat All')),
                             True: (REPEAT_ONE_IMG, gt('Repeat Off')),
                             False: (REPEAT_ALL_IMG, gt('Repeat One'))}.items():
        try:
            assert repeat_img_tooltip(option) == expected
        except AssertionError:
            print('TEST FAILED', option)
            raise AssertionError
    assert create_progress_bar_text(30, 300) == ('0:30', '4:30')
    print('Default Audio Device:', get_default_output_device())
    for size in ((125, 425), COVER_MINI, COVER_NORMAL):
        base64data = resize_img(DEFAULT_ART, settings['theme']['background'], new_size=size)
        img_data = io.BytesIO(b64decode(base64data))
        img: Image = Image.open(img_data)
        assert img.size == size


if __name__ == '__main__':
    test_helpers()
