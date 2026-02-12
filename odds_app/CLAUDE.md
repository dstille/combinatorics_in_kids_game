# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational games teaching combinatorics (permutations, combinations, odds) to children through family-themed narratives (cousins, pets). The games use interactive console I/O to walk players through mathematical concepts step by step.

## Running the Games

```bash
# Console games (interactive, require user input)
python pet_herding.py      # Combinations & odds via pet herding scenario
python kid_herding.py      # Two-set variant (Adult Cousins + Kid Cousins)
python horse_game.py       # Permutations via cousin lineup scenarios
python mini_lotto.py       # Permutations vs combinations comparison

# Streamlit web app
streamlit run mini_lotto_app.py

# FastAPI server (Docker)
docker build -t pet_herding .
docker run pet_herding
# Or directly:
python src/main.py
```

No test framework, linter, or build system is configured.

## Architecture

### Class Hierarchy (core math engine)

```
Set                          # Mathematical set with formatting
  └─ Sets                   # Collection of sets, subset matching, difference ops
       └─ Combinatorics     # Base: set iteration + recursive flatten algorithm
            ├─ Combinations  # C(n,k) generation via recursive choose_r()
            │    ├─ ComboBuild   # Step-by-step combination visualization
            │    ├─ ComboBuild2  # Alternative build visualization
            │    └─ Players2     # Single-set game state (pet_herding)
            └─ Permutations  # P(n,k) generation via recursive perm_r()
                 └─ PermBuild    # Step-by-step permutation visualization
```

Key: `Combinations` and `Permutations` use custom recursive algorithms (not `itertools`) to generate all sets, then `flatten()` converts the nested recursive output to flat lists.

### Game Flow Pattern

All games follow: random target selection → generate all combinations/permutations → user guesses odds → display formatted math explanation.

### Module Roles

| Module | Role |
|--------|------|
| `combinatorics.py` | `Set`, `Sets`, `Combinatorics` base classes |
| `combinations.py` | `Combinations`, `ComboValue` (binomial coefficient), `ComboBuild` |
| `permutations.py` | `Permutations`, `PermValue`, `PermBuild` |
| `math_reprs.py` | `Odds`, `Prob`, `Factorial`, `Fraction` (Fraction/Factors incomplete) |
| `players.py` | `Players` (two-set game state), `Players2` (single-set) |
| `game_abc.py` | Input helpers: `get_number_input()` parses "3 in 10" and "0.30" formats |
| `displays.py` | kid_herding display formatting |
| `pet_herding_displays.py` | pet_herding display formatting |
| `horse_displays.py` | horse_game scenario descriptions |

### Multilingual Support

Switch language by changing the import at the top of game files:
- `strings.py` — English
- `es_strings.py` — Spanish
- `pr_strings.py` — Portuguese

### Game Characters

- **Adult Cousins:** Sebastian, Brianna, Bailey, Morgan, Bryelle
- **Kid Cousins:** Anya, Leon, Sawyer, Jade, Mia
- **Pets:** Bentley, Winnie, Luna, Obie, Mocha, Willow, Rex

## Known Incomplete Code

- `Factors.get_prime_factors()` in `math_reprs.py` has undefined variables and is non-functional
- `game_abc.py` defines an ABC base class that no game inherits from
- `translate_strings.py` uses `googletrans` but is not integrated into game flow

## Dependencies

Core: `numpy` (weighted random), `fastapi`/`uvicorn` (server), `streamlit` (mini_lotto web UI). Python 3.10+.
