# Marcode

> Marcode (Mr. Code in Hebrew), Ineed your help!
> I got a movie but I cant see it. It hypnotizes me.
> please help me!
> yours,
> Gveretcode (Mrs. Code in Hebrew)
>
> P.S.
> change NOXCTF to noxCTF.
> https://drive.google.com/open?id=1GkalBntU1s6d_sw_S5I4GinD8hBrh-C-

We get a video which is flashing images of QR Codes.
First i used ffmpeg to extract all the frames from the video:

`ffmpeg -i Marcode.mp4 -r 25 -f image2 frames/frame-%04d.png`

![image](frames/frame-0001.png)

This script will decode every QR Code and print the data

```python
from pyzbar.pyzbar import decode
from PIL import Image
import sys

for i in range(1,3490):
    print decode(Image.open('frames/frame-'+str(i).zfill(4)+'.png'))[0].data
```

```
$ python marcode.py >> links.txt
$ awk '!x[$0]++' links.txt > unique_links.txt
```

I extracted all the unique google drive links and we will see they're the 26 letters of the alphabet + `_` and `?`.

```python
from pyzbar.pyzbar import decode
from PIL import Image
import sys

links = open('unique_links.txt').read().split('\n')
text = 'THE_WOMNAPRDUF?YSILCQGZBKXVJ'
solution = ''

for i in range(1,3491):
    l = decode(Image.open('frames/frame-'+str(i).zfill(4)+'.png'))[0].data
    for x in range(len(links)):
        if l == links[x]:
            solution += text[x]
            
print solution
```

Next i mapped the letters to the links and decoded every QR Code again to check them against the links and then create a text.

```
THE_TWO_MEN_APPEARED_OUT_OF_NOWHERE?_A_FEW_YNARDS_APART_IN_THE_NARROW?_MOONLIT_LANE?_FOR_A_SECOND_THEY_STOOD_QUITE_STOILL?_WANDS_DIRECTED_AT_EACH_OTHER?S_CHESTS?_THEN?_RECOGNIZING_EACH_OTHER?_THEY_STOWED_THEIR_WANDS_BENEATH_THEIR_CLOAKS_AND_STARTED_WALKING_BRISKLY_IN_THE_SAME_DIRECTION?_?NEWS??_ASKED_THE_TALLEXR_OF_THE_TWO?_?THE_BEST??_REPLIED_SEVERUS_SNAPE?_THE_LANE_WAS_BORDERED_ON_THE_LEFT_BY_WILD?_LOW?GROWING_BRAMBLES?_ON_THE_RIGHT_BY_A_HICGH?_NEATLY_MANICURED_HEDGE?_THE_MEN?S_LONG_CLOAKS_FLAPPED_AROUND_THEIR_ANKLES_AS_THEY_MARCHED?_?THOUGHT_I_MIGHTT_BE_LATE??_SAID_YAXLEY?_HIS_BLUNT_FEATURES_SLIDING_IN_AND_OUT_OF_SIGHT_AS_THE_BRANCHES_OF_OVERHANGING_TREES_BROKE_THE_MOONLIGHT?_?IT_WAS_A_LITTLE_TRICKIER_THAN_I_EXPECTEFD?_BUT_I_HOPE_HE_WILL_BE_SATISFIED?_YOU_SOUND_CONFIDENT_THAT_YOUR_RECEPTION_WILL_BE_GOOD??_SNAPE_NODD?ED?_BUT_DID_NOT_ELABORATE?_THEY_TURNED_RIGHT?_INTO_A_WIDE_DRIVAEWAY_THAT_LED_OFF_THE_LANE?_THE_HIGH_HEDGE_CURVED_INTO_THEM?_RUNNIVNG_OFF_INTO_THE_DISTANCE_BEYOND_THE_PAIR_OF_IMPAOSING_WROUGHT?IRON_GATES_BARRING_THE_MEN???S_WAY?_NEITDHER_OF_THEM_BROKE_STEP?_IN_SILENCE_BOTH_RAISED_THEIR_LEFT_ARMS_IN_A_KIND_OF_SALAUTE_AND_PASSED_STRAIGHT_THROUGH?_AS_THOUGH_THE_DARK_METAL_WAS_SMOKE?_THE_YEW_HEDGES_MUFFLED_THE_SOKUND_OF_THE_MEN???S_FOOTSTEPS?_THERE_WAS_A_RUSTLE_SOMEWHERE_TO_THEIR_RIGHT?_YAXLEY_DREW_HIS_WAND_AGAIN_POINTING_IT_OVER_HIS_COMPANION???S_HEAD?_BUT_THE_SOURCE_OF_THE_NOISE_PROVED_TO_BE_NOTHING_MORE_THAN_A_PURE?WHITE_PEACOCK?_STERUTTING_MAJESTICALLY_ALONG_THE_TOP_OF_THE_HEDGE?_???HE_ALWAYS_DID_HIMSELF_WELL?_LUCIUS?_PEACOCKS??????_YAXLEY_THRUST_HIS_WAND_BADCK_UNDER_HIS_CLOAK_WITH_A_SNORT?_A_HANDSOME_MANOR_HOUSE_GREW_OUT_OF_THE_DARKNESS_AT_THE_END_OF_THE_STRAIGHT_DRIVE?_LIGHTS_GLINTING_IN_THE_DIAMOND_PANED_DOWNSTAAIRS_WINDOWS?_SOMEWHERE_IN_THE_DARK_GARDEN_BEYOND_THE_HEDGE_A_FOUNTAIN_WAS_PLAYING?_GRAVEL_CRACKLED_BENEATH_THEIR_FEET_AS_SNAPE_AND_YAXLEY_SPED_TOWARD_THE_FRONT_DOOR?_WHICH_SWUNG_INWARD_AT_THEIR_APPROACH?_THOUGH_NOBODY_HAD_VISIBLY_OPENED_VIT?_THE_HALLWAY_WAS_LARGE?_DIMLY_LIT?_AND_SUMPTUOUSLY_DECORATED?_WITH_A_MAGNIFICENT_CARPET_COVERING_MOST_OF_THE_STONE_FLOOR?_THE_EYES_OF_THE_PALE?FACED_PORTRAITS_ON_THE_WALL_FOLLOWED_SNAPE_AND_YAXLEY_AS_THEY_STRODE_PAST?_THE_TWO_MEN_HALTED_AT_A_HEAVY_WOODEN_DOOR_LEADING_INTO_THE_NEXT_ROOM?_HESITATED_FOR_THE_SPACE_OF_A_HEARTBEAT?_THEN_SNAPE_TURNED_THE_BRONZE_HANDLE?_THE_DRAWING_ROOM_WAS_FULL_OF_SILENT_PREOPLE?_SITTING_AT_A_LONG_AND_ORNATE_TABLE?_THE_ROOM???S_USUAL_FURNITURE_HAD_BEEN_PUSHED_CARELESSLY_UP_AGAINST_THE_WALLS?_ILLUMINATION_CAME_FROM_A_ROARING_FIRE_BENEATH_A_HANDSOME_MARBLE_MANTELPIECE_SURMOUNTED_BY_A_GILDED_MIRROR?_SNAPE_AND_YAXLEY_LINGERED_FOR_A_MOMENT_ON_THE_THRESHOLD?_AS_THEIR_EYES_GREW_ACCUSTOMED_TO_THE_LACK_OF_LIGHT?_THEY_WERE_DRAWN_UPWARD_TO_THE_STRANGEST_FEATURE_OF_THE_SCENE?_AN_APPARENTLY_UNCONSCIOUS_HUMAN_FIGURE_HANGING_UPSIDE_DOWN_OVER_THE_TABLE?_REVOLVING_SLOWLY_AS_IF_SUSPENDED_BY_AAN_INVISIBLE_ROPE?_AND_REFLECTED_IN_THE_MIRROR_AND_IN_THE_BARE?_POLISHED_SURFACE_OF_THE_TABLE_BELOW?_NONE_OF_THE_PEOPLE_SEATED_UNDERNEATH_THIS_SINGULAR_SIGHT_WERE_LOOKING_AT_IT_EXCEPT_FOR_A_PALE_YOUNG_MAN_SITTING_ALMOST_DIRECTLY_BELOW_IT?_HE_SEEMED_UNABLE_TO_PREVENT_HIMSELF_FROM_GLANCING_UPWARD_EVERY_MINUTE_OR_SO?_???YAXLEY?_SNAPE????_SAID_A_HIGH?_CLEAR_VOICE_FROM_THE_HEAD_OF_THE_TABLE?_???YOU_ARE_VERY_NEARLY_LATE????_THE_SPEAKER_WAS_SEATED_DIRECTLY_IN_FRONT_OF_THE_FIREPLACE?_SO_THAT_IT_WAS_DIFFICULT?_AT_FIRST?_FOR_THE_NEW_ARRIVAL?S_TO_MAKE_OUT_MORE_THAN_HIS_SILHOUETTE?
```

This text is a segment from the Harry Potter books and to find the flag we have to read through it. We will notice that some characters are out of place, the first one is here `A_FEW_YNARDS_APART`.
Read through it and find all out of place characters.
The final flag is: `noxCTF{AVADAKEDAVRA}`