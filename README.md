# ImmersiveMusicControl
Idea for controlling music via OSC commands from within VRChat using in-game controls and such

Essentially, this is an idea I've got to integrate the playing and pausing of music into the action of putting on or taking off headphones on my VRChat avatar.

However, this may expand to controlling music using touch-buttons (contacts) in-game, in-game expression menus, etc. by use of OSC and two-way messaging.

There is a _potential_ to also use this software to list what song is currently playing, playing progress, etc. -- mostly in blind hope to get rid of OSC text box spam with music stuff in various worlds.

---

Parts of this project:

- Outside VRChat
  - interface between music app / service and OSC
    - Music app interface
      - Cider: RPC
      - Spotify: their API stuff
      - other services? (scope creep warning)
    - OSC interface
      - TouchOSC integration templates(?)
      - Direct OSC messaging integration
      - OSC to VRCFury messaging integration option
- Inside VRChat
  - Prefab buttons and such for music controls, info text, etc.
  - Animator functionality to move object in-game by trigger
  - Easy installation scripts (vrcfury?) if desired

---

Documentation to refer to:

- Cider interfacing
  - https://cider.sh/docs/client/rpc
  - What even is RPC? | https://en.wikipedia.org/wiki/Remote_procedure_call
  - RPC to OSC? | https://github.com/robbielyman/zosc
- Spotify interfacing
  - https://developer.spotify.com/documentation/web-api
  - https://developer.spotify.com/documentation/web-playback-sdk/tutorials/getting-started
  - https://engineering.atspotify.com/2022/04/spotifys-player-api/
  - examples:
    - https://github.com/JohnnyCrazy/SpotifyAPI-NET
    - https://github.com/RoguePlanetoid/Spotify-Uwp-Showcase
    - https://github.com/spotipy-dev/spotipy
    - https://spotify.github.io/
    - https://github.com/spotlightify/spotlightify

---

WARNING: scope creep be beyond this point! Ye be warned!

- Music search with [VXMusic](https://github.com/Soapwood/VXMusic), then when it finds the song, show info on panel in-game... and bring up search on spotify / cider
- 