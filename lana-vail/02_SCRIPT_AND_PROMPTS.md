# LANA VAIL — "A Whole Person"
Cinematic short, 6 shots, ~34 seconds, 16:9 (optional 2.39:1 letterbox in finishing).

**Logline:** Late night, alone in her apartment with a laptop and a glass of red wine, Lana confesses to the camera that she's been playing with AI, that it's ridiculously easy to make a "whole person", and ends with a wink that makes you wonder whether she's one of them.

**Film look:** warm 35mm print, in the spirit of the night interiors of *Licorice Pizza* (2021): tungsten practicals, creamy skin, soft highlights with halation, fine grain, olive-green shadows, no digital sharpness. LUT: `LANA_WarmPrint35_full.cube`, applied once to the final edit.

---

## 0. Blocks to paste into EVERY image prompt

### IDENTITY (paste first)
```
The woman is exactly the same person as in the reference images: Lana, late 20s, long straight strawberry-blonde hair with soft natural waves and a slightly off-center part, dense natural freckles across her nose, cheeks, chest and shoulders, light green eyes, soft full natural-pink lips, oval face with soft jawline, warm fair skin with real pores and texture, thin gold chain necklace with a small round gold coin pendant. Keep her facial structure, eye shape, nose, lips, brows and freckle pattern identical to the reference images. Natural minimal makeup.
```

### WARDROBE (same in all shots)
```
She wears a short black silk satin slip dress with thin spaghetti straps, a low draped cowl neckline and an open low back, hem at mid-thigh, bare legs, barefoot. Hair loose and slightly tousled, as if she's been home all evening.
```

### SET
```
Her apartment at night: a lived-in modern living room, a grey linen couch with a soft throw blanket, a small brass table lamp with a warm tungsten bulb, a laptop, a glass of red wine, large window with soft out-of-focus city lights, plants on floating shelves, framed black-and-white prints on the wall.
```

### CAMERA & FILM LOOK (paste last)
```
Film still from a Hollywood feature film. Shot on 35mm film, Kodak Vision3 500T, ARRI 435 with Cooke S4 prime lenses, wide open at T2, shallow depth of field, creamy bokeh. Motivated practical lighting: warm tungsten table lamp as key light, soft cool spill from the laptop screen, deep but not crushed shadows. Fine organic film grain, gentle halation around highlights, slightly soft focus roll-off, natural true-to-life colors, real skin texture with visible pores and peach fuzz. Not over-sharpened.
```

### NEGATIVE / AVOID (add at the end of image prompts)
```
Avoid: plastic or airbrushed skin, beauty filter, over-sharpened details, HDR look, oversaturated colors, glossy CGI look, digital video look, ring light, studio backdrop, text, captions, watermark, logos, extra fingers, distorted hands, different face, changed freckle pattern, nudity.
```

**How to generate in Google Flow** (image generation; pick Nano Banana Pro in the model menu if it is offered):
- Upload the images listed for each frame below as **ingredients**, in that order (the first one matters most). If Flow limits how many you can add, keep the first ones in the list.
- Orientation: **landscape 16:9** · outputs: **4** · keep the best face. Download at the highest size Flow offers.
- Don't grade the frames in Flow: the CAMERA block asks for natural colors on purpose, because the LUT goes on the final video.
- Prompt order: `[IDENTITY] + [WARDROBE] + [SET] + [FRAME DESCRIPTION] + [CAMERA & FILM LOOK] + [NEGATIVE]`

---

## 1. Keyframe prompts (start + end for each shot)

> `REF` = `lana_ref_5.jpg, lana_ref_1.jpg, lana_ref_3.jpg, lana_ref_2.jpg` (ref_5 first: it's the clearest face).
> `HERO` = the approved **1A** image (locks wardrobe, set and light for everything after it).

### SHOT 1 — "The confession" · CU · 50mm · 5s
**1A START** · image_urls: `REF`
```
FRAME: Close-up from slightly below eye level, 50mm lens. She sits curled up on the couch, laptop on her knees, eyes down on the screen, typing, the blue-white screen glow on her face mixing with the warm lamp behind her. A glass of red wine on the side table, out of focus. Calm, private, a little mischievous. Mouth closed.
```
**1B END** · image_urls: `1A, ref_5, ref_1`
```
Same shot, same framing, lighting and wardrobe as image 1. Change only: she has lifted her eyes from the laptop and looks straight into the lens with a small knowing smirk, one eyebrow slightly raised. Keep her face identical to the reference images.
```

### SHOT 2 — "Embarrassingly easy" · MS · 35mm · 6s
**2A START** · image_urls: `HERO, ref_5, ref_1, ref_3`
```
FRAME: Medium shot, waist up, 35mm lens, camera at seated eye level. She leans forward towards the laptop on her knees, glass of red wine in her right hand, looking at the screen with amused disbelief. Lamp behind her creates a warm rim on her hair and shoulders.
```
**2B END** · image_urls: `2A, ref_5, ref_1`
```
Same shot, same framing, lighting and wardrobe as image 1. Change only: she has leaned back into the couch cushions, looking into the lens, gesturing loosely with the wine glass, laughing at herself mid-sentence. Keep her face identical to the reference images.
```

### SHOT 3 — "The boyfriend" · tight CU · 85mm · 6s
**3A START** · image_urls: `HERO, ref_5, ref_3, ref_1`
```
FRAME: Tight close-up, 85mm lens, face fills the frame from chin to forehead. She sips red wine, the glass rim at her lips, her green eyes looking at the lens over the glass. Warm lamp key from frame left, soft cool fill from the laptop below. Background fully melted into bokeh.
```
**3B END** · image_urls: `3A, ref_5, ref_1`
```
Same shot, same framing, lighting and wardrobe as image 1. Change only: she has lowered the glass below frame, lips slightly wet from the wine, deadpan half-smile, eyes straight into the lens. Keep her face identical to the reference images.
```

### SHOT 4 — "Then I made a girl" · MWS · 32mm · 6s
**4A START** · image_urls: `HERO, ref_4, ref_1, ref_5`
```
FRAME: Medium-wide shot, 32mm lens, camera low near the coffee table. She is rising from the couch, setting the laptop aside, mid-motion, face visible in three-quarter view, looking toward the big window. The black slip dress catches the lamp light. City lights soft behind the window.
```
**4B END** · image_urls: `4A, ref_5, ref_1`
```
Same location, wardrobe and lighting as image 1, camera at the same position. Change only: she now stands at the window, back three-quarters to the camera showing the open back of the dress, and she glances over her shoulder at the lens with a playful look. Her face is clearly visible in three-quarter profile. Keep her face identical to the reference images.
```

### SHOT 5 — "Competition" · CU · 50mm · 5s
**5A START** · image_urls: `4B, ref_5, ref_3`
```
FRAME: Close-up at the window, 50mm lens. She is in soft profile looking out at the blurred city lights, cool blue night light from the window on one side of her face, warm lamp light on the other. Thoughtful, almost serious.
```
**5B END** · image_urls: `5A, ref_5, ref_1`
```
Same shot, same framing, lighting and wardrobe as image 1. Change only: she has turned her head to face the lens, one eyebrow raised, lips pressed together in mock seriousness, trying not to laugh. Keep her face identical to the reference images.
```

### SHOT 6 — "Which one of us?" · CU → ECU push-in · 50mm · 6s
**6A START** · image_urls: `HERO, ref_5, ref_1, ref_3`
```
FRAME: Close-up, 50mm, centered, she faces the lens directly, standing near the lamp, warm key light, chin slightly lowered, a playful curious look, lips closed.
```
**6B END** · image_urls: `6A, ref_5, ref_1`
```
Same lighting and wardrobe as image 1. Change only: extreme close-up, her eyes and lips fill the frame, she has leaned toward the lens, a sly smile right after a wink, one eye still slightly squinted, freckles sharp and detailed. Keep her face identical to the reference images.
```

---

## 2. Video prompts — `minimax/h3-max/reference-to-video` (primary for every shot)

Why this model: it is the only H3 endpoint that takes her face references **and** a start frame **and** an end frame together. (`minimax/h3-max-turbo/reference-to-video` also exists, but it has no start/end frame inputs, so it can't hold your keyframes.)

Settings for every shot:
- `reference_image_urls`: `[lana_ref_5.jpg, lana_ref_1.jpg, lana_ref_3.jpg]` (same three, same order, every shot)
- `image_url` = start frame from Flow (xA) · `end_image_url` = end frame from Flow (xB)
- `resolution`: `1080P` · `aspect_ratio`: `adaptive` (follows the 16:9 keyframes) · `duration`: as listed
- `prompt_expansion_mode`: `disabled` (keeps the exact wording; switch to `balanced` only if motion feels stiff)
- Do not fill `reference_conditions` (it can't be combined with `reference_image_urls`) and leave `middle_image_url` empty.
- Once a take is good, write down its `seed`.

Add this **prefix** to every video prompt:
```
Image 1, Image 2 and Image 3 show the exact face and identity of the woman. She must look identical to them in every frame: same face shape, green eyes, nose, lips, brows, freckle pattern and strawberry-blonde hair. The video starts on the provided first frame and ends on the provided last frame.
```

Add this **suffix** to every video prompt:
```
Style: 35mm film footage, 24fps motion cadence, natural motion blur, subtle handheld micro-movement, shallow depth of field, organic grain, soft halation, real skin texture. Her face, freckles and features stay exactly the same as in the first and last frames throughout the shot. Sound: quiet late-night apartment room tone, faint distant city traffic, no music.
Avoid: face morphing, identity change, over-sharpened image, smooth plastic skin, slow-motion, jump cuts, camera shake, garbled speech, text on screen, subtitles, extra people.
```

### SHOT 1 · 5s
```
Close-up, static camera with subtle handheld breathing. [0-2s] She types on the laptop, eyes down, screen glow flickering softly on her face. [2-5s] She stops typing, slowly lifts her eyes to the lens and says in a soft, low, amused American voice: "So... I've started playing with AI lately." A small smirk at the end.
```

### SHOT 2 · 6s
```
Medium shot, very slow push-in. [0-2s] She leans toward the laptop, shaking her head in amused disbelief. [2-6s] She falls back into the cushions, gestures loosely with the wine glass and says to the lens, half laughing: "And it's embarrassingly easy. You type a few words... and boom. A whole person."
```

### SHOT 3 · 6s
```
Tight close-up, locked off, very slight drift. [0-1.5s] She takes a slow sip of red wine, eyes on the lens over the glass. [1.5-6s] She lowers the glass and says with dry deadpan timing: "I made a guy. Tall, funny, remembers my birthday." Short pause. "Best relationship I've had all year." A tiny half-smile.
```

### SHOT 4 · 6s
```
Medium-wide shot, camera slowly pans to follow her. [0-3s] She sets the laptop aside, gets up from the couch and walks barefoot to the window, the silk dress moving naturally. [3-6s] She stops at the window, glances back over her shoulder at the lens and says playfully: "Then I made a girl. Red hair, freckles... gorgeous."
```

### SHOT 5 · 5s
```
Close-up, static. [0-1.5s] She looks out at the city lights in profile. [1.5-5s] She turns her head to the lens, raises one eyebrow and says in mock-serious tone: "Too gorgeous. I deleted her." Beat. "Competition." She bites back a laugh.
```

### SHOT 6 · 6s
```
Slow push-in from close-up to extreme close-up as she leans toward the lens. [0-4s] She whispers, intimate and teasing: "Then again... how do you know I'm not one of them?" [4-6s] She winks and lets out a soft breathy laugh. Hold on her eyes.
```

---

## 3. If a shot's face still drifts
- Re-run with a new seed first.
- Make sure the face is large in both xA and xB, and that xB was generated from xA (so the two frames match).
- Shorten the shot to 5 seconds.
- Last resort: `minimax/h3-max-turbo/image-to-video` with the same xA/xB (faster, but no face references).

## 4. Voice consistency (optional)
H3 generates the voice from the prompt, so it can vary between shots. To keep one voice:
1. Generate all six lines with one voice in `fal-ai/elevenlabs/tts/eleven-v3`.
2. Cut each line into its own file (at least 2 seconds; pad with silence).
3. Pass that line as `reference_audio_urls: [line.mp3]` and add to the prompt: `Her voice matches Audio 1 exactly.` (references, images and audio together, max 12 files).
Test on Shot 1 first. If lip-sync is off, keep the native audio and replace only the voice in the edit.

## 5. Edit order
1 → 2 → 3 → 4 → 5 → 6 → black. Trim 6–10 frames from the head and tail of each clip (generated clips often ease in/out). Apply `LANA_WarmPrint35_full.cube` to the whole timeline (CapCut or DaVinci Resolve), then add light grain and softening. With ffmpeg, one command does LUT + softness + halation + grain on the final export: `tools/film_finish.sh final.mp4 final_film.mp4 luts/LANA_WarmPrint35_full.cube` (add `scope` at the end for 2.39:1 bars).
