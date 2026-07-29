# PokeShell Keyboard LEDs

## Project

- **Name:** PokeShell Keyboard LEDs
- **Status:** Idea / prototype
- **Priority:** Later
- **Related Epic:** `01-linux`

## Mission

- Explore themed Pokémon displays on Corsair keyboard LEDs.
- Start with a sprite-to-keyboard preview, then test a real ckb-next LED export path.

## Current Context

- Current task: turn Pokémon sprites into themed keyboard layouts.
- Current blocker: the real ckb-next hardware path is not yet wired into the prototype.
- Next action: map one sprite to a fixed key grid and verify the visual result on the keyboard.
- Estimated time: 1-2 focused sessions

## Backlog

- [ ] define the key-grid mapping for the K60 layout
- [ ] pick a small sprite set to test first
- [ ] write a ckb-next export path or profile helper
- [ ] compare preview output across Pikachu, Charmander, Bulbasaur, and Squirtle

## Validation

- How will I know it works?
- A Pokémon-themed layout renders clearly in preview.
- A real keyboard lighting change matches the selected themed sprite.

## Decisions

- What choice was made?
- Use a simple coarse grid first instead of chasing detailed pixel art.
- Why was it chosen?
- The keyboard has limited resolution, so themed silhouettes and blocky shapes will be more readable.

## Reflection

- What worked?
- A virtual keyboard preview demo already proved the concept is worth testing.
- What did not?
- The existing ckb-next GUI only exposes coarse brightness control.
- What should change next?
- Move from preview-only rendering to a hardware-facing LED mapping experiment.
